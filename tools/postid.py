import re
import os
import platform

def clear_console():
    # Clear the console based on the operating system
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def extract_userid_postid(link, content_type):
    # Define regex patterns for posts and videos
    if content_type == "post":
        pattern = r'https://www\.facebook\.com/(\d+)/posts/(\d+)'
    elif content_type == "video":
        pattern = r'https://www\.facebook\.com/(\d+)/videos/(\d+)'
    else:
        return "Invalid content type"

    match = re.search(pattern, link)
    
    if match:
        userid = match.group(1)
        postid = match.group(2)
        return f"{userid}_{postid}"
    else:
        return "Invalid link"

# ANSI escape codes for text color
class TextColor:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'  # Yellow color
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Simple logo using ASCII art
logo = r"""
  
             ██████╗ ███████╗ ██████╗██████╗ 
             ██╔══██╗██╔════╝██╔════╝██╔══██╗
             ██████╔╝█████╗  ██║     ██████╔╝
             ██╔══██╗██╔══╝  ██║     ██╔═══╝ 
             ██║  ██║██║     ╚██████╗██║     
             ╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  [V1.0]
              ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ʟᴇɪɴᴀᴛʜᴀɴ ᴏʀᴇᴍᴏʀ
"""

# Clear the console before running
clear_console()

# Print the logo
print(TextColor.OKGREEN + logo + TextColor.ENDC)

while True:
    # Prompt the user for content type
    content_type = input(TextColor.OKGREEN + "Do you want to extract from a 'post' or 'video'? " + TextColor.WARNING).strip().lower()
    # Prompt the user to input a link
    link = input(TextColor.OKGREEN + "Please enter the Facebook link: " + TextColor.WARNING)
    result = extract_userid_postid(link, content_type)

    if result.startswith("Invalid"):
        print(TextColor.FAIL + result + TextColor.ENDC)
    else:
        print(TextColor.OKGREEN + "Extracted User ID and Post ID: " + result + TextColor.WARNING)

    # Ask if the user wants to extract more
    more = input(TextColor.OKGREEN + "Do you want to extract more? (yes/no): " + TextColor.WARNING).strip().lower()
    if more == 'no':
        break

# Final prompt to exit
input(TextColor.OKGREEN + "Press Enter to exit..." + TextColor.ENDC)
