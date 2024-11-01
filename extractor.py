import re

def extract_userid_postid(url):
    # Define the regex pattern for the new format
    pattern = r"https://www\.facebook\.com/(\d+)/post/(\d+)"
    match = re.search(pattern, url)
    
    if match:
        userid = match.group(1)
        postid = match.group(2)
        return f"{userid}_{postid}"
    else:
        return None

# Example usage
url = "https://www.facebook.com/123456789/post/987654321"
result = extract_userid_postid(url)
if result:
    print(result)  # Output: 123456789_987654321
else:
    print("No match found")
