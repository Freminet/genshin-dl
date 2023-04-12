from bs4 import BeautifulSoup
import requests

url = "https://genshin-impact.fandom.com/wiki/Hu_Tao/Voice-Overs" # URL to voice over
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = [link.get("href") for link in soup.find_all("a", {"class": "internal"}, recursive=True)]

for link in links:
    print(link)
    resp = requests.get(link)
    with open(link.split("VO_")[1].split(".ogg")[0] + ".mp3", "wb") as f:
        f.write(resp.content)
