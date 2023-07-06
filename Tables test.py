import requests
from bs4 import BeautifulSoup as soup

word = 'test'
page = requests.get(f'https://prirucka.ujc.cas.cz/?slovo={word}')

print('Status code:', page.status_code)
#print(page.headers)

src = page.content
#print(src)

soup = soup(src, 'lxml')
table = soup.find('table', attrs={'class':'para'})

info = []
row = 0
for tr in table.find_all('tr'):
    info.append([])
    for td in tr.find_all('td'):
        if td.a != None: td.a.decompose()
        info[row].append(td.text)
    row = row + 1

maxLen = []
for tr in info:
    column = 0
    for td in tr:
        maxLen.append(0)
        if len(td) > maxLen[column]: maxLen[column] = len(td)
        column += 1

row = 0
for tr in info:
    column = 0
    for td in tr:
        info[row][column] = td + ' ' * (maxLen[column] - len(td))
        column += 1
    row += 1
    print(' | '.join(tr))
