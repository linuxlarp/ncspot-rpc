# ncspot-rpc
![PyPI Version](https://img.shields.io/pypi/v/ncspot-rpc)
![Python Version](https://img.shields.io/pypi/pyversions/ncspot-rpc)
![License](https://img.shields.io/github/license/linuxlarp/ncspot-rpc)
![Stars](https://img.shields.io/github/stars/linuxlarp/ncspot-rpc)

> Discord Rich Presence Client (RPC) adapter for [ncspot](https://github.com/hrkfdn/ncspot)

A simple, semi-lightweight, python based extension to display [ncspot](https://github.com/hrkfdn/ncspot) data from a socket to your Discord Profile using Discords RPC Protocol and PyPresence.

## Why?
By default, ncspot does not interact with the Discord RPC, nor does it natively support it. This program acts a middleman and adapter for that missing bridge. For people who want to show what their playing to their friends on Discord, this program also serves as a replacement for several similar projects that are no longer supported or outdated. 

The program acts a daemon you launch from a command-line using `ncspot-rpc`. We recommend you put it in your `.xinitrc` (for X11) or `~/.config/hypr/hyprland.conf` as an `exec-once` entry (Hyprland), or as your system requires.

## Prerequisites
- [Discord Client](https://discord.com) or [Vesktop/Vencord](https://vencord.dev)
- [ncspot](https://github.com/hrkfdn/ncspot)
- **Linux** or Unix Based System *(Linux is the only platform we currently support, future compatibility expected in another update)*

## Examples
![Higlight](https://raw.githubusercontent.com/linuxlarp/ncspot-rpc/refs/heads/main/docs/static/concept.png)
![Example](https://raw.githubusercontent.com/linuxlarp/ncspot-rpc/refs/heads/main/docs/static/showcase3.png)
![Example Fullscreen](https://raw.githubusercontent.com/linuxlarp/ncspot-rpc/refs/heads/main/docs/static/showcase1.png)


## Installation

We recommend installing via [pipx](https://pipx.pypa.io/latest/installation/) for the best experience.

```bash
pipx install ncspot-rpc
```

> Other installation methods are not officially supported at this time.

## Documentation
To view the documentation we currently have available, use the hyperlinks below.

- ![**Configuration Guide**](https://github.com/linuxlarp/ncspot-rpc/blob/main/docs/SETTING_CONFIG.md)
- ![**Custom Discord Client**](https://github.com/linuxlarp/ncspot-rpc/blob/main/docs/CUSTOM_CLIENT.md)
- ![**Tech Overview**](https://github.com/linuxlarp/ncspot-rpc/blob/main/docs/TECH_OVERVIEW.md)

## Credits
The following resources, and repositories contributed, helped or served as inspiration to the development of this project:

- [PyPresence](https://github.com/qwertyquerty/pypresence)
- [RichSpot (original idea)](https://github.com/M1ndo/RichSpot/tree/main)
