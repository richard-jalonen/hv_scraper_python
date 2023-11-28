import requests
from bs4 import BeautifulSoup


class HvScraper:
    hv_url = "https://foorum.hinnavaatlus.ee/"

    def get_topics(self, keyword):
        search_params = "{}search.php?search_keywords={}&search_terms=any&search_author=&search_forum=-1&search_time=0&search_fields=all&search_cat=3&sort_by=0&sort_dir=DESC&show_results=topics&return_chars=200&search_hv_pref%5B%5D=M&search_price="

        URL = search_params.format(self.hv_url, keyword)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        topics = soup.find_all("span", class_="topictitle")
        return topics

    def generate_answer_string(self, keyword):
        topics = self.get_topics(keyword)
        result = ""
        for topic in topics:
            result += topic.text + " \n"
            result += "<" + self.hv_url + topic.a["href"] + "> \n"
        if len(result) == 0:
            return "Ei leidnud miskit, mine poodi"
        return result
