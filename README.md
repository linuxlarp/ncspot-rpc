# ncspot-rpc
> Discord Rich Presence (RPC) adapter for [ncspot](https://github.com/hrkfdn/ncspot)

A simple, lightweight, python based extension to display [ncspot](https://github.com/hrkfdn/ncspot) data from a socket to your Discord Profile using Discords RPC Protocol and PyPresence.


## Why?
By default, ncspot does not interact with the Discord RPC, nor does it natively support it. This program acts a middleman and adapter for that missing bridge. For people who want to show what their playing to their friends on Discord, this program also serves as a replacement for several similar projects that are no longer supported or outdated. 

The program acts a daemon you launch from a command-line. We recommend you put it in your `.xinitrc` (for X11) or `~/.config/hypr/hyprland.conf` as an `exec-once` entry (Hyprland), or as your system requires.

## Prerequisites
- [Discord Client](https://discord.com) or [Vesktop/Vencord](https://vencord.dev)
- [ncspot](https://github.com/hrkfdn/ncspot)
- **Linux** or Unix Based System *(Linux is the only platform we currently support, future compatibility expected in another update)*

## Examples
![Example 1](https://github.com/linuxlarp/ncspot-rpc/blob/main/docs/static/showcase1.png)
![Example 2](https://github.com/linuxlarp/ncspot-rpc/blob/main/docs/static/showcase2.png)

![Example 3 **Now with customization options...**](https://github.com/linuxlarp/ncspot-rpc/tree/main/docs/static)

## Installation
A PyPI package is in the works, hang with us while we get it up.

## Documentation
To view the documentation we currently have available, use the hyperlinks below.

**WIP**

## Credits
The following resources, and repositories contributed, helped or served as inspiration to the development of this project:

- [PyPresence](https://github.com/qwertyquerty/pypresence)
- [RichSpot (original idea)](https://github.com/M1ndo/RichSpot/tree/main)
