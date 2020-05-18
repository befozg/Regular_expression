import os
import logging
import time
import unicodedata
import graphyte
from selenium import webdriver
from bs4 import BeautifulSoup

logging.getLogger().setLevel(logging.INFO)
BASE_URL = 'https://yandex.ru/'
GRAPHITE_HOST = 'graphite'

COVID_DATA = [
    'today',
    'total'
]

def parse_yandex_page(page):
    covid_blocks = page.findAll('span', {'class': 'covid-speed__description-number'})
    print('spaaaaaan',covid_blocks[0].text)
    covid_data = []
    covid_data.append(('today', int(covid_blocks[0].text.replace('+\u2009', ''))))
    covid_data.append(('total', int(covid_blocks[1].text.replace('\xa0', ''))))
    return covid_data

def send_metrics(covid_data):
    sender = graphyte.Sender(GRAPHITE_HOST, prefix='covid')
    for covid in covid_data:
        sender.send(covid[0], covid[1])

def main():

    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True}
    )

    driver.get('https://yandex.ru')
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    metric = parse_yandex_page(soup)
    send_metrics(metric)

    driver.quit()

    logging.info('Accessed %s ..', BASE_URL)
    logging.info('Page title: %s', driver.title)

if __name__ == '__main__':
    main()