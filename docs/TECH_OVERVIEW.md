# Technical Overview

All application code is in `src/`. The entry point is `src/main.py`, with all core logic split across modules in `src/core/`. 

## How It Works

ncspot writes playback state to a UNIX socket at `/run/user/1000/ncspot/ncspot.sock`. ncspot-rpc connects to that socket, reads the JSON payloads it emits, and forwards the relevant track data to Discord via the RPC protocol.

```
ncspot > UNIX socket > ncspot-rpc > Discord RPC > your profile
```

## Module Breakdown

| Module | Role |
|---|---|
| `main.py` | Entry point, bootstraps config, logger, and starts the socket daemon |
| `core/config.py` | Loads `config.toml`, auto creates it on first run, exposes settings as a `Basic` instance |
| `core/socket.py` | Connects to the ncspot UNIX socket, reads payloads in a loop, handles reconnection |
| `core/rpc.py` | Manages the Discord RPC connection via `pypresence`, translates track data into activity updates |
| `core/models.py` | Pydantic models describing the JSON structure ncspot emits |
| `core/logs.py` | Coloured console logger, debug output gated behind `DEBUG = true` in config |


## Data Flow

1. `ListenerSocket` reads raw bytes from the ncspot socket
2. JSON is parsed and matched against pause/stop/finish states
3. If playing: a `SpotifyResponse` model is constructed and passed to `RPC.update_track()`
4. `RPC` calculates timestamps from epoch values in `ModeDetails` and calls `pypresence` to update the Discord activity
5. If paused/stopped: `RPC.clear()` is called to remove the activity

# Developer Experience
When working on the codebase, please enable debug logging in `~/.config/ncspot-rpc/config.toml`

```toml 
[general]
DEBUG = true
```

This enables all `debug()` log calls acrross every module, giving you a full trace of socket events, recieved payloads, RPC updates and config reseloution.

## Resilience

Both `socket.py` and `rpc.py` are designed to handle their respective processes not being available at startup or dropping mid-session. `inotify` watches are used throughout so the process blocks efficiently rather than polling.
