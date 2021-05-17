from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
from loguru import logger
from colorama import init as colorama_init, deinit, Fore, Style
colorama_init()

BASE_URL = 'https://nightvale.fandom.com{pg_suff}'
TRANSCRIPT_URL = 'https://nightvale.fandom.com/wiki/Category:Year_{year}_transcripts'


@dataclass
class Quote:
    text: str
    year: str
    episode: str


def init():
    pass


def fetch():
    quotes_lst = []
    _ctr = 1
    while True:
        url = TRANSCRIPT_URL.format(year=_ctr)
        logger.debug(url)
        response = requests.get(url)
        logger.debug(response.status_code)
        if response.status_code > 299:
            break
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if not href or 'wiki/Transcript:' not in href:
                continue
            pg_url = BASE_URL.format(pg_suff=href)
            logger.debug(pg_url)
            response = requests.get(pg_url)
            logger.debug(response.status_code)

            pg_soup = BeautifulSoup(response.text, 'html.parser')
            for p in pg_soup.select('div.mw-parser-output p'):
                quote = Quote(
                    text=p.get_text(),
                    year=f'Year {_ctr}',
                    episode=pg_soup.select(
                        'div.mw-parser-output div b')[0].get_text()
                )
                # print(Fore.RED + Style.BRIGHT + quote.text)
                # print(Fore.GREEN + Style.BRIGHT + quote.text)
                # print(Fore.YELLOW + Style.BRIGHT + quote.text)
                # print(Fore.BLUE + Style.BRIGHT + quote.text)
                # print(Fore.MAGENTA + Style.BRIGHT + quote.text)
                print(Fore.CYAN + Style.BRIGHT + quote.text)
                # print(Fore.WHITE + Style.BRIGHT + quote.text)
                quotes_lst.append(quote)

        _ctr += 1

    return quotes_lst


def main():
    pass


if __name__ == '__main__':
    # main()
    quotes_lst = fetch()


deinit()
