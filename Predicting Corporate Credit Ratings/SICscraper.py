import urllib
import csv
from matplotlib.pyplot import table
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from sphinx import RemovedInNextVersionWarning
from sympy import beta

# create  an URL object
url = 'https://www.sec.gov/corpfin/division-of-corporation-finance-standard-industrial-classification-sic-code-list'

# create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
soup

# obtain information from table class
table1 = soup.find("table", {"class": "sic bordered-table"})
table1

# obtain title of columns under the tag <th>
headers = []  # store headers in a list
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

# print(headers)

# create a dataframe
sicdata = pd.DataFrame(columns=headers)

# fill data into the dataframe from the table under the tag <tr> under <td>
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(sicdata)
    sicdata.loc[length] = row

# export to csv
sicdata.to_csv('sicdata.csv', index=False)

# read the csv
sic_ddf = pd.read_csv('sicdata.csv')
