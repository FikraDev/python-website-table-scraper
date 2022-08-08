from unittest import result
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import schedule
import time


url = input('Enter the URL of the site you wish to scrape: ')

sites = []

sites.append(url)

def checkSite():

    try:
        for site in sites:
            r = requests.get(site)

        if r.status_code != 200:
            print('Site Down***', r.url, r.status_code)
            logfile = open("logfile.txt", 'a')
            logfile.write(
                '{} - {} is Down***. Error Code {} \n'.format(datetime.now(), r.url, r.status_code))
            logfile.close()
        else:
            read_url = pd.read_html(site)
            scraped = list(read_url) #create a list from the data pulled from the site

            print(datetime.now())
            df = pd.DataFrame(scraped[0]) #scrapes the top 25 items
            df.to_csv('scraped_data.csv', index=False) #convert the list to csv
            print("Scrape Complete!!")
            
    except ValueError as e:
        print(e)
        schedule.clear()

schedule.every(0).seconds.do(checkSite)
# schedule.clear() #remove if you want it continue checking

while True:
    schedule.run_pending()
    time.sleep(1)
