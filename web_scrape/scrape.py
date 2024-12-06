import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"


def create_custom_hn(submissions, subtext):
    hn = []

    for i, link in enumerate(submissions):
        title = link.find("span", class_="titleline").find("a").getText()
        news_id = link.get("id")
        href = link.find("span", class_="titleline").find("a").get("href")

        vote = int(subtext[i].find("span", class_="score").getText().split(" ")[0])
        hn.append({"news_id": news_id, "title": title, "link": href, "votes": vote})
    return hn


def get_page():
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    submissions = soup.select(".submission")
    subtext = soup.select(".subtext")
    next_page_url = soup.select(".morelink")[0].get("href")
    return {"hn": create_custom_hn(submissions, subtext), "next_page_url": f"{url}{next_page_url}"}


def get_next_page(next_page_url):
    res = requests.get(f"{url}{next_page_url}")
    html_doc = res.text
    soup = BeautifulSoup(html_doc, "html.parser")
    submissions = soup.select(".submission")
    subtext = soup.select(".subtext")
    return create_custom_hn(submissions, subtext)


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k["votes"], reverse=True)


hn = get_page()
hn_sorted = sort_stories_by_votes(hn["hn"])

for item in hn_sorted:
    print(item["title"], "\n")
    print(item["link"], "\n")
    print(item["votes"], "\n")
    print("\n")
print(hn["next_page_url"])
