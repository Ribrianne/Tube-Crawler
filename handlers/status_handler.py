import time
from colorama import Fore, Style

def print_status(status, color="normal", delay=0.5):
    colors = {
        "normal": Fore.GREEN,
        "warning": Fore.YELLOW,
        "error": Fore.RED
    }
    color_code = colors.get(color.lower(), "")

    spinner = ["|", "/", "-", "\\"]
    spinner_index = 0

    print(f"{color_code}[{' '}] {status}", end="", flush=True)  # Initial status message

    for _ in range(5):  # Simulate spinner animation for five iterations
        time.sleep(delay)  # Delay between spinner frames
        print("\b" * (len(status) + 4), end="", flush=True)  # Move cursor back and clear previous content
        spinner_index = (spinner_index + 1) % len(spinner)  # Get next spinner frame
        print(f"{color_code}[{spinner[spinner_index]}] {status}", end="", flush=True)  # Print updated spinner and status

    print(Style.RESET_ALL)  # Reset console color at the end

