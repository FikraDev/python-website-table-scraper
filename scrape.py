from time import time
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests
import time
import os
from dotenv import load_dotenv
import smtplib
import ssl

load_dotenv()

url = requests.get('https://www.jamstockex.com/trading/trade-quotes/')

scrape = BeautifulSoup('url.text', 'html.parser')

result = pd.read_html(url.text)

# print(dfs)
# index number indicates the first table on the page
dframe = pd.DataFrame(result[1])
curr_time = datetime.fromisoformat(datetime.now().isoformat())
dframe.to_csv(r"./scraped_data.csv", index=False)
time.sleep(2)
os.rename('./scraped_data.csv', 'scraped_data.csv_' +
                    str(datetime.now().strftime("%Y%m%d%H%M")))
chkfile = os.scandir('./')

print(str(chkfile))

if scraped in chkfile:

    '''Send Email'''
    '''For password you have to enable 2-factor on gmail and then set a
        App Password for mail - Other'''
     port = 465  # For SSL
     smtp_server = "smtp.gmail.com"
     sender_email = os.getenv('SENDER_EMAIL')  # Enter your address
     receiver_email = "sachel.campbell@gmail.com"  # Enter receiver address
     password = os.getenv('PASSWORD')
     message = """\
             Subject: New Web Scrape (Alert!!!)

             This message is to inform you that your scrape was successful.
             The scrape occured at: """ + str(datetime.now())

     context = ssl.create_default_context()
     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message)
 else:
     print("Error")
