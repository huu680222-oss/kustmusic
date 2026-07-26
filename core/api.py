import asyncio
import logging
import os
import time

import yt_dlp

from config import COOKIES_FILE

logger = logging.getLogger(__name__)


async def fetch_youtube_link(query, is_video=False):
    # Determine if query is a URL or a search phrase
    if not (query.startswith("http://") or query.startswith("https://")):
        search_query = f"ytsearch1:{query}"
    else:
        search_query = query

    ydl_opts = {
        "format": "best[height<=720]/best" if is_video else "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "extract_flat": False,
        "skip_download": True,
        "js_runtimes": {"deno": {}, "node": {}},
        "remote_components": ["ejs:github"],
    }

    try:
        loop = asyncio.get_event_loop()

        def _extract(opts):
            with yt_dlp.YoutubeDL(opts) as ydl:
                return ydl.extract_info(search_query, download=False)

        info = None
        # Try with cookies first
        if COOKIES_FILE and os.path.exists(COOKIES_FILE):
            opts_with_cookies = dict(ydl_opts)
            opts_with_cookies["cookiefile"] = COOKIES_FILE
            try:
                info = await loop.run_in_executor(None, _extract, opts_with_cookies)
            except Exception as e:
                logger.warning(f"Extraction with cookies failed: {e}. Retrying without cookies...")

        # Fallback to no cookies if needed
        if not info:
            info = await loop.run_in_executor(None, _extract, ydl_opts)

        if not info:
            return None

        if "entries" in info:
            entries = info["entries"]
            if not entries:
                return None
            video = entries[0]
        else:
            video = info

        title = video.get("title")
        url = video.get("webpage_url") or video.get("url")
        if not url and video.get("id"):
            url = f"https://www.youtube.com/watch?v={video.get('id')}"

        duration = video.get("duration", 0)

        thumbnail = video.get("thumbnail")
        if not thumbnail and video.get("thumbnails"):
            thumbnail = video["thumbnails"][-1].get("url")

        return {
            "title": title,
            "link": url,
            "stream_url": video.get("url"),
            "duration": duration,
            "thumbnail": thumbnail,
        }
    except Exception as e:
        logger.warning(f"yt-dlp search/extract failed for '{query}': {e}")
        return None


def _yt_download(youtube_url, output_template, use_cookies=True):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "js_runtimes": {"deno": {}, "node": {}},
        "remote_components": ["ejs:github"],
    }
    if use_cookies and COOKIES_FILE and os.path.exists(COOKIES_FILE):
        ydl_opts["cookiefile"] = COOKIES_FILE
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


async def download_song(youtube_url):
    try:
        unique = str(time.time())
        output_template = f"downloads/{unique}.%(ext)s"
        final_path = f"downloads/{unique}.mp3"
        loop = asyncio.get_event_loop()

        # Try with cookies first
        try:
            await loop.run_in_executor(None, _yt_download, youtube_url, output_template, True)
        except Exception as e:
            logger.warning(f"Download with cookies failed: {e}. Retrying without cookies...")
            # Try without cookies
            await loop.run_in_executor(None, _yt_download, youtube_url, output_template, False)

        if os.path.exists(final_path):
            return final_path
        for ext in ["m4a", "webm", "opus", "ogg"]:
            alt = f"downloads/{unique}.{ext}"
            if os.path.exists(alt):
                return alt
        return None
    except Exception as e:
        logger.warning(f"yt-dlp failed: {e}")
        return None
