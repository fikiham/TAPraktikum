import requests
from bs4 import BeautifulSoup
import smtplib, time

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
second = 'Title (Price)'
authentication = "https://www.tokopedia.com/"
loopAfter = False

openSourceText = open('source/source.txt', 'r+')
stringLink = openSourceText.read().split(';')
myEmail = 'secreted from github'
myPass = 'secreted from github'


def check_price(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="css-1wtrxts").get_text()
    if len(title) > 40:
        realTitle = title[0:40] + "..."
    else:
        realTitle = title
    price = soup.find(class_="price").get_text()[2:]
    return realTitle, price


def check_then_mail(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="css-1wtrxts").get_text()
    price = soup.find(class_="price").get_text()[2:]
    return URL, title, price


def send_mail(body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(myEmail, myPass)

    subject = "Hello You, This is YOUR Daily Dose of Copium"
    msg = f'Subject : {subject}\n\n{body}'

    server.sendmail(
        myEmail,
        'laztnamed@gmail.com',
        msg
    )
    print("Email Sent")
    server.quit()
