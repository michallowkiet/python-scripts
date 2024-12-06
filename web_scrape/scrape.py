import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
r = requests.get(url)
html_doc = r.text

soup = BeautifulSoup(html_doc, "html.parser")

submissions = soup.select(".submission")

subtext = soup.select(".subtext")


def create_custom_hn(submissions, subtext):
    hn = []

    for i, link in enumerate(submissions):
        title = link.find("span", class_="titleline").find("a").getText()
        news_id = link.get("id")
        href = link.find("span", class_="titleline").find("a").get("href")

        vote = int(subtext[i].find("span", class_="score").getText().split(" ")[0])
        hn.append({"news_id": news_id, "title": title, "link": href, "votes": vote})
    return hn


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k["votes"], reverse=True)


hn = create_custom_hn(submissions, subtext)
hn = sort_stories_by_votes(hn)

for item in hn:
    print(item["title"], "\n")
    print(item["link"], "\n")
    print(item["votes"], "\n")
    print("\n")
