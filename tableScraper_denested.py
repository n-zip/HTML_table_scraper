import requests
from bs4 import BeautifulSoup as bs

#Denester functions
#----------------------------------------------------------

def listMaker(row: int, tr: bs, table2D: list):
    '''
    Makes the 2D list for a table
    '''

    table2D.append([])
    tabledata = tr.find_all('td')

    if tabledata == []:
        for th in tr.find_all('th'):
            table2D[row].append(th.text)

        return row + 1
    
    for td in tabledata:
        table2D[row].append(td.text)

    return row + 1

def longestStr(tr: bs, maxLen: list):
    '''
    Finds longest str in each tr and updates the list
    '''

    for column, td in enumerate(tr):
        maxLen.append(0)
        if len(td) > maxLen[column]: maxLen[column] = len(td)

def tableRow(y: int, tr: list, table2D: list, maxLen: list):
    '''
    Makes each table row right size and prints it
    '''

    for x, td in enumerate(tr):
        table2D[y][x] = td + ' ' * (maxLen[x] - len(td))

    print(' | '.join(tr))

#----------------------------------------------------------

#Main function
#----------------------------------------------------------
def tableScraper(url: str, atrrs: dict):
    '''
    Scrapes url parameter for tables matching attrs dictionary using requests and BeautifulSoup

    '''
    page = requests.get(url)

    print('\nStatus code:', page.status_code, end="\n\n")

    src = page.content

    soup = bs(src, 'lxml')
    tables = soup.find_all('table', atrrs)

    # Makes a 2D list of each table and prints the whole table
    for index in range(len(tables)):
        table2D = []
        row = 0

        for tr in tables[index].find_all('tr'):
            row = listMaker(row, tr, table2D)

        # Gets longest str for each cloumn
        maxLen = []
        for tr in table2D:
            longestStr(tr, maxLen)

        # Extends all strings in each column to be the same length
        for row, tr in enumerate(table2D):
            tableRow(row, tr, table2D, maxLen)
        print()

#----------------------------------------------------------

tableScraper('https://www.w3schools.com/html/html_tables.asp', {})