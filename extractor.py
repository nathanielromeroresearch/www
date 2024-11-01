import re

def extract_userid_contentid(url, link_type):
    # Define regex patterns for post and video formats
    if link_type == 'post':
        pattern = r"https://www\.facebook\.com/(\d+)/post/(\d+)/\?mibex"
    elif link_type == 'video':
        pattern = r"https://www\.facebook\.com/(\d+)/video/(\d+)/\?mibex"
    else:
        return None

    match = re.search(pattern, url)
    
    if match:
        userid = match.group(1)
        contentid = match.group(2)
        return f"{userid}_{contentid}"
    else:
        return None

# Prompt the user to choose the type of link
link_type = input("Enter the type of link (post/video): ").strip().lower()
url = input("Enter the Facebook link: ")

result = extract_userid_contentid(url, link_type)

if result:
    print(f"Extracted: {result}")  # Output: {userid}_{contentid}
else:
    print("No match found")
