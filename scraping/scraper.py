import requests
from bs4 import BeautifulSoup
import time
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Fetch the webpage
url = "https://www.literotica.com/new/stories?page=" + str(1)
response = requests.get(url, headers=headers)

time.sleep(1)
# Regular expression to ffilter
pattern = re.compile(r".*/s/.*")

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all links
links = soup.find_all("a", href=pattern)

for link in [links[0]]:
    href = link.get("href")
    response = requests.get(href, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text()

    marker = "Followers"
    marker_index = page_text.find(marker)

    if marker_index != -1:
        # Extract text after the marker
        text_after_marker = page_text[marker_index + len(marker) :].strip()
        print(text_after_marker)
    else:
        print(page_text)

# Print href attributes
"""
for link in links:
    print(link.get("href"))
"""
