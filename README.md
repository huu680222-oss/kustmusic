<div align="center">

<pre>
 ██╗  ██╗██╗   ██╗███████╗████████╗
 ██║ ██╔╝██║   ██║██╔════╝╚══██╔══╝
 █████╔╝ ██║   ██║███████╗   ██║
 ██╔═██╗ ██║   ██║╚════██║   ██║
 ██║  ██╗╚██████╔╝███████║   ██║
 ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

     🎵 <b>ZOLVID MUSIC BOT</b> 🎵

  ⚡ <b>Highly Advanced Instant Streaming Speed (Under 1 Second)</b>
  🤖 <b>Premium Multi-Bot Clone System</b>
  🎨 <b>gorgeous Custom UI Layout Design</b>
</pre>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Courier+New&weight=700&size=18&duration=4000&pause=500&color=00D4FF&center=true&vCenter=true&width=600&lines=🎧+Premium+Telegram+VC+Music+Bot;⚡+Instant+Direct+Streaming+Engine;🤖+Multi-Bot+Clone+System;🚀+Powered+by+Zolvid" alt="typing animation" />
</p>

<p align="center">
<a href="https://t.me/zolvid"><img src="https://img.shields.io/badge/Powered%20By-Zolvid-00D4FF?style=for-the-badge&logo=telegram" alt="Zolvid Channel"/></a>
<a href="https://t.me/zolvid"><img src="https://img.shields.io/badge/Support-Zolvid-orange?style=for-the-badge&logo=telegram" alt="Support"/></a>
</p>

</div>

---

## ⚡ Highly Advanced Instant Playback Engine

Traditional music bots take **17 to 18 seconds** to download, process, and transcode audio before playing it in the voice chat.

**Zolvid Music Bot** uses a **highly advanced direct-streaming engine**:
- **0-1 Second Start Time:** Fetches direct audio streams via `yt-dlp` and passes them directly to `pytgcalls` via `MediaStream` objects.
- **Zero Disk I/O Bottlenecks:** No files are downloaded to disk, ensuring maximum system speed and longevity for your VPS/Cloud host.
- **Direct Stream URL Re-resolution:** Automatically re-resolves expired streaming URLs on the fly during queue transitions.

---

## 🎨 Best Premium Design Features

This bot has been fully redesigned to offer a breathtaking visual experience:
- **🖼️ 5 Randomized Start Images:** Displays a random high-quality visual banner from a pool of premium images every single time `/start` is executed.
- **💬 Collapsible Interactive Help Menu:** Smoothly transition between help categories (**🎵 Music**, **🛡️ Admin**, and **⚙️ System**) with inline callback buttons, editing the existing message without spamming your chats.
- **📊 Premium Playback Controls:** Gorgeous, clean quote formatting with modern fonts, dynamic progress updates, and permanent custom buttons linking to **Zolvid** (`t.me/zolvid`).

---

## 📜 All Bot Commands

### 👥 Everyone Commands
| Command | Description | Command Aliases |
|---|---|---|
| `/start` | Starts the bot and displays premium custom interactive interface with random banners. | `/start` |
| `/play <song>` | Instantly streams a search query or YouTube URL in the VC. | `/play`, `/p` |
| `/ping` | Displays bot's real-time latency and detailed VPS/server system metrics. | `/ping`, `/alive` |
| `/clone <token>`| Clones a new independent bot instance on the fly from BotFather. | `/clone` |

### 🛡️ Group Admin Commands
| Command | Description | Command Aliases |
|---|---|---|
| `/skip` | Skips the current playing song and proceeds with the next queue item. | `/skip` |
| `/stop` | Stops the voice chat playback and clears the active music queue. | `/stop`, `/end` |
| `/pause` | Pauses the active music streaming. | `/pause` |
| `/resume`| Resumes the paused music streaming. | `/resume` |
| `/clear` | Clears all the queued songs except the currently playing one. | `/clear`, `/clean` |
| `/kick` | Kicks a member from the group (by reply). | `/kick` |
| `/ban` | Bans a member from the group (by reply). | `/ban` |
| `/unban`| Unbans a member from the group (by reply). | `/unban` |
| `/mute` | Mutes a member in the group chat (by reply). | `/mute` |
| `/unmute`| Unmutes a member in the group chat (by reply). | `/unmute` |

### 👑 Main Owner Commands
| Command | Description | Command Aliases |
|---|---|---|
| `/active`| Lists all active cloned bot instances and their respective hosts. | `/active` |

---

## 🚀 Key Features Overview

| Feature | Description |
|---|---|
| 🎧 **Direct VC Playback** | Stream music directly into Telegram voice chats with high audio parameters. |
| ⚡ **Highly Advanced Speed** | Bypasses slow downloads. Streams in under 1 second using raw streaming pipelines. |
| 🍪 **Cookie Support** | Supports custom YouTube cookies to bypass rate limits and age restrictions. |
| 🤖 **Interactive Multi-Bot Cloner** | Clone unlimited bot instances with a single `/clone` command. |
| 🛡️ **Group Moderation Suite** | Comprehensive moderating tools (ban, kick, mute) integrated out of the box. |
| 📊 **Dynamic Progress Updates** | Auto-updating player interface with elapsed time, custom slider bar, and control keyboard. |
| 🔄 **Intelligent Queue System** | Advanced in-memory queuing logic that auto-plays next tracks instantly. |
| 🌱 **Pure Memory Footprint** | Zero database required. Runs purely on lightning-fast python in-memory states. |

---

## 📁 Project Structure

```
├── main.py              ← Entry point, starts all services
├── config.py            ← All environment variables
├── state.py             ← In-memory state (queues, clients)
├── clients.py           ← Pyrogram + PyTgCalls client setup
├── server.py            ← Dummy HTTP server for Render/Koyeb
├── kust.env             ← Environment variable template
├── requirements.txt     ← Python dependencies
├── core/
│   ├── api.py           ← YouTube search + direct streaming URL extractor
│   ├── guards.py        ← Admin check + rate limiting
│   ├── helpers.py       ← Formatting utilities & font mappers
│   └── playback.py      ← Music direct streaming core logic
└── handlers/
    ├── router.py        ← Registers all command handlers
    ├── music.py         ← /play, /stop, /skip, /pause, /resume
    ├── admin.py         ← /kick, /ban, /mute, /unmute
    ├── system.py        ← /start, /ping, /clone, /active
    └── callbacks.py     ← Interactive collapsible menu handlers
```

---

## 🛠️ Quick Installation (VPS / Local Hosting)

1. **Update and upgrade your system:**
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

2. **Install system dependencies:**
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/kustbots/kustmusic && cd kustmusic
   ```

4. **Install Python packages:**
   ```bash
   pip3 install -U -r requirements.txt
   ```

5. **Setup environment variables:**
   ```bash
   cp kust.env .env
   nano .env
   ```
   *Fill in your `BOT_TOKEN`, `API_ID`, `API_HASH`, and `ASSISTANT_SESSION`.*

6. **Run the bot:**
   ```bash
   python3 main.py
   ```

---

## 👤 Support & Credits

Zolvid Music Bot is designed and optimized for **supreme speed and layout elegance**.

- **Owner Link:** [t.me/zolvid](https://t.me/zolvid)
- **Updates Channel:** [t.me/zolvid](https://t.me/zolvid)

<b>Made with ❤️ by <a href="https://t.me/zolvid">Zolvid</a></b>
