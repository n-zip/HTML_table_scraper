import requests
from bs4 import BeautifulSoup as soup

page = requests.get('https://www.w3schools.com/html/html_tables.asp')

print('Status code:', page.status_code)

src = page.content

soup = soup(src, 'lxml')
table = soup.find('table')

# Makes a 2D list of the table
info = []
row = 0
for tr in table.find_all('tr'):
    info.append([])
    if tr.find_all('td') == []:
        for th in tr.find_all('th'):
            info[row].append(th.text)
        row = row + 1
        continue
    for td in tr.find_all('td'):
        info[row].append(td.text)
    row = row + 1

# Gets longest str for each cloumn
maxLen = []
for tr in info:
    for column, td in enumerate(tr):
        maxLen.append(0)
        if len(td) > maxLen[column]: maxLen[column] = len(td)

# Extends all strings in each column to be the same length
for row, tr in enumerate(info):
    for column, td in enumerate(tr):
        info[row][column] = td + ' ' * (maxLen[column] - len(td))
    print(' | '.join(tr))