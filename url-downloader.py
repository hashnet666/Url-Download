"""
Author: Hydra Hashnet
Date: 2025-08-12
"""

import sys
import subprocess
import os

# ANSI escape codes for colors
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def display_logo():
    """Display the author's ASCII art logo with yellow and red colors."""
    logo = f"""
{Colors.YELLOW}{Colors.BOLD}╔═════¦✵𝗛𝘆𝗱𝗿𝗮 𝗡𝗮𝘁𝗶𝗼𝗻✵¦═════╗
░▒▓█»»ᑌᖇᒪ ᗪOᗯᑎ𝗟𝗢𝗔𝗗𝗘ᖇ««██▓▒░
╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤╧╤
◤║▌║▌║HTTPS://T.ME/REDSMOKER2 ║▌║▌◥
╚═════¦✵𝗟𝗲𝗲𝗰𝗵𝗯𝗼𝘁 𝘂𝗿𝗹✵¦═════╝{Colors.RESET}
"""
    print(logo)

def leechbot(url, output_path="."):
    """
    Downloads a video from a given URL using the yt-dlp command-line tool.

    Args:
        url (str): The URL of the video to download.
        output_path (str, optional): The directory to save the video.
                                     Defaults to the current directory.
    """
    try:
        # Ensure the output directory exists.
        os.makedirs(output_path, exist_ok=True)

        # Build the command to download the video.
        command = [
            "yt-dlp",
            url,
            "-o", f"{output_path}/%(title)s.%(ext)s",
            "--no-check-certificate",  # Bypass SSL verification.
        ]

        # Check for a cookies.txt file in the same directory and add it to the command.
        if os.path.exists("cookies.txt"):
            command.extend(["--cookies", "cookies.txt"])
            print(f"{Colors.GREEN}[*] Found and using cookies.txt for authentication.{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}[*] Downloading video from: {url}...{Colors.RESET}")
        
        # Run the command and wait for it to complete.
        subprocess.run(command, check=True)
        print(f"{Colors.GREEN}[*] Download completed successfully!{Colors.RESET}")

    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}[!] An error occurred during download: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}This may be due to the video being private or an invalid URL.{Colors.RESET}")
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Error: 'yt-dlp' was not found. Please ensure it is installed and in your system's PATH.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] An unexpected error occurred: {e}{Colors.RESET}")

def download_file(url, output_path="."):
    """
    Downloads a generic file from a URL using the wget command-line tool.

    Args:
        url (str): The URL of the file to download.
        output_path (str, optional): The directory to save the file.
                                     Defaults to the current directory.
    """
    try:
        # Ensure the output directory exists.
        os.makedirs(output_path, exist_ok=True)

        print(f"\n{Colors.CYAN}[*] Downloading file from: {url}...{Colors.RESET}")

        # Build the wget command to download the file.
        command = ["wget", "-P", output_path, url]

        # Run the command and wait for it to complete.
        subprocess.run(command, check=True)
        print(f"{Colors.GREEN}[*] Download completed successfully!{Colors.RESET}")

    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}[!] An error occurred during file download: {e}{Colors.RESET}")
    except FileNotFoundError:
        print(f"{Colors.RED}[!] Error: 'wget' was not found. Please ensure it is installed.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] An unexpected error occurred: {e}{Colors.RESET}")


# --- Main Execution Block ---
if __name__ == "__main__":
    display_logo()
    
    # Prompt the user for the URL.
    url_to_download = input(f"{Colors.BLUE}{Colors.BOLD}Enter the URL to download:{Colors.RESET} {Colors.YELLOW}")
    sys.stdout.write(Colors.RESET) # Reset color after input

    # Check if the user entered a URL.
    if not url_to_download:
        print(f"{Colors.RED}[!] No URL provided. Exiting.{Colors.RESET}")
        sys.exit(1)

    # Prompt the user for the storage path.
    default_android_path = "/storage/emulated/0/Download"
    output_path_input = input(f"{Colors.BLUE}{Colors.BOLD}Enter the storage path (or press Enter for default: {default_android_path}):{Colors.RESET} {Colors.YELLOW}")
    sys.stdout.write(Colors.RESET) # Reset color after input

    if not output_path_input:
        output_path = default_android_path
    else:
        output_path = output_path_input

    # Simple logic to decide which tool to use.
    if "youtube.com" in url_to_download or "facebook.com" in url_to_download or "youtu.be" in url_to_download:
        leechbot(url_to_download, output_path)
    else:
        download_file(url_to_download, output_path)