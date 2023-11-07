from parsel import Selector
import requests


class NewsScraper:
    URL = "https://wotpack.ru/cat/stat-i/novosti/"
    LINK_XPATH = '//article[@class="jeg_post jeg_pl_md_1 format-standard"]/div/a/@href'
    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        print(links)

        return links[:5]


if __name__ == '__main__':
    scraper = NewsScraper()
    scraper.parse_data()