import time, itertools
from colorama import Fore, Style

def print_status(status, color="normal", delay=.3):
    colors = {
        "normal": Fore.GREEN,
        "warning": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "error": Fore.RED
    }
    color_code = colors.get(color.lower(), "")

    print(f"{color_code}[{' '}] {status}", end="", flush=True)  # Initial status message

    time.sleep(delay)  # Delay before updating the status

    print("\b" * (len(status) + 4), end="", flush=True)  # Move cursor back and clear previous content
    print(f"{color_code}[✓] {status}{Style.RESET_ALL}")  # Print updated status with a tick mark

