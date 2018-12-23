#!/usr/bin/env python3
"""
Name:   Craig Opie
Class:  CENT110
File:   webscrapper.py

Algorithm:
Allow the user to specify a stock symbol and return the current price or
price at closing.

1) Import the requests module to retrieve the data from the website.
2) Import BeautifulSoup to allow allow the data to be parsed
3) Create a loop to allow multiple inquiries before quiting.
4) Take the input from the user or allow them to exit the program.  The value
is then placed in a format the website is expecting.
5) If the user types exit then the program quits.
6) Retrieve data from Yahoo Finance using the user provided stock symbol.
7) Parse the data using BeautifulSoup.
8) Sort throught the soup to find the correct division tag.
9) Sort throught the division tag information to find the correct information.
10) Print the Stock symbol and value for the user to see.
"""
import requests
from bs4 import BeautifulSoup

loop_condition = True
while(loop_condition == True):
    # Get the stock symbol to lookup from the user
    symbol = input("Please enter the stock symbol you want to check (type \
'exit' to exit): ").upper().replace(" ", "")

    # Allows the user to exit the loop
    if symbol == "EXIT":
        loop_condition = False

    else:
        # Get the data
        data = requests.get('https://finance.yahoo.com/quote/' + symbol + '/')

        # Load data into BeautifulSoup
        soup = BeautifulSoup(data.text, 'html.parser')

        # Refine soup down to the correct div tag
        div = soup.find('div', { 'data-reactid': '13' })

        # Refine div down to the correct span tag and return the text info
        value = div.find('span', { 'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) \
Fz(36px) Mb(-4px) D(b)' }).text.strip()

        # Return value to the user
        print(symbol + " == " + str(value))
