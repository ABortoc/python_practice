import requests
from bs4 import BeautifulSoup
import pprint

links = []
subtext = []

for page_num in range(1, 3):
    response = requests.get(f"https://news.ycombinator.com/news?p={page_num}")
    soup_object = BeautifulSoup(response.text, "html.parser")
    links += soup_object.select(".storylink")
    subtext += soup_object.select(".subtext")


def filter_news(links, subtext):
    hacker_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hacker_news.append({"title": title, "link": href, "votes": points})
    return sorted(hacker_news, key=lambda k: k["votes"], reverse=True)


pprint.pprint(filter_news(links, subtext))
