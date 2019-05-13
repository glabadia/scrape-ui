from abc import ABC, abstractmethod


class DataScraping(ABC):
    @abstractmethod
    def scrape(self):
        pass


class StandardScrape(DataScraping):
    def scrape(self):
        print("Data Collection w/ images start..")


class FastScrape(DataScraping):
    def scrape(self):
        print("Fast Data Collection Start..")


fs = FastScrape()
ss = StandardScrape()


def control(scrapers):
    for scraper in scrapers:
        scraper.scrape()


control([fs, ss])
