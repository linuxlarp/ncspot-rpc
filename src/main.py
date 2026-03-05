from importlib.metadata import version

from colorama import Fore

import core.config as config
import core.logs as logger
from core import socket

logs = logger.Logger()


def banner():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    banner = r"""
    $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$$$\      $$$$$$$\  $$$$$$$\   $$$$$$\
    $$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\__$$  __|     $$  __$$\ $$  __$$\ $$  __$$\
    $$$$\ $$ |$$ /  \__|$$ /  \__|$$ |  $$ |$$ /  $$ |  $$ |        $$ |  $$ |$$ |  $$ |$$ /  \__|
    $$ $$\$$ |$$ |      \$$$$$$\  $$$$$$$  |$$ |  $$ |  $$ |$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |
    $$ \$$$$ |$$ |       \____$$\ $$  ____/ $$ |  $$ |  $$ |\______|$$  __$$< $$  ____/ $$ |
    $$ |\$$$ |$$ |  $$\ $$\   $$ |$$ |      $$ |  $$ |  $$ |        $$ |  $$ |$$ |      $$ |  $$\
    $$ | \$$ |\$$$$$$  |\$$$$$$  |$$ |       $$$$$$  |  $$ |        $$ |  $$ |$$ |      \$$$$$$  |
    \__|  \__| \______/  \______/ \__|       \______/   \__|        \__|  \__|\__|       \______/
    """
    logs.info("Welcome to...")
    for i, line in enumerate(banner.split("\n")):
        print(f"{colors[i % len(colors)]}{line}{Fore.RESET}")


def main():
    banner()

    logs.info(
        "Welcome to ncspot-rpc, The compatability layer for ncspot to Discord RPC."
    )

    try:
        __version__ = version("ncspot-rpc")
        logs.info(f"Application Version: {__version__}")
    except:
        logs.tip(
            "Unable to find most current application version, ensure package is installed/updated via PyPi."
        )

    sock = socket.ListenerSocket()
    sock.start_sock()  ## Let it rip


if __name__ == "__main__":
    main()
