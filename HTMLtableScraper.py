import requests
from bs4 import BeautifulSoup as bs

#Denester functions
#----------------------------------------------------------

def _listMaker(row: int, tr: bs, table2D: list):
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

def _longestStr(tr: bs, maxLen: list):
    '''
    Finds longest str in each tr and updates the list
    '''

    for column, td in enumerate(tr):
        maxLen.append(0)
        if len(td) > maxLen[column]: maxLen[column] = len(td)

def _tableRow(y: int, tr: list, table2D: list, maxLen: list):
    '''
    Makes each table row right size and prints it
    '''

    for x, td in enumerate(tr):
        table2D[y][x] = td + ' ' * (maxLen[x] - len(td))

    print(' | '.join(tr))

#----------------------------------------------------------

#Main function
#----------------------------------------------------------
def tableScraper(url: str, attributes = {}):
    '''
    Scrapes url for tables matching dictionary, default attributes empty using requests and BeautifulSoup. \n
    Prints in a neat, easy to see way

    Example usage:
    >>> from HTMLtableScraper import tableScraper
    >>> tableScraper('https://www.w3schools.com/html/html_tables.asp', {"id": "customers"})
    >>> Status code: 200

            Company                      | Contact          | Country\n
            Alfreds Futterkiste          | Maria Anders     | Germany\n
            Centro comercial Moctezuma   | Francisco Chang  | Mexico\n
            Ernst Handel                 | Roland Mendel    | Austria\n
            Island Trading               | Helen Bennett    | UK\n
            Laughing Bacchus Winecellars | Yoshi Tannamuri  | Canada\n
            Magazzini Alimentari Riuniti | Giovanni Rovelli | Italy\n
    '''

    if type(url) is not str:
        raise TypeError("Url must be a string!")
    
    elif type(attributes) is not dict:
        raise TypeError("Attributes must be a dictionary!")

    page = requests.get(url)

    print('\nStatus code:', page.status_code, end="\n\n")

    src = page.content

    soup = bs(src, 'lxml')
    tables = soup.find_all('table', attributes)

    if tables == []:
        print("No tables found!")

    # Makes a 2D list of each table and prints the whole table
    for index in range(len(tables)):
        table2D = []
        row = 0

        for tr in tables[index].find_all('tr'):
            row = _listMaker(row, tr, table2D)

        # Gets longest str for each cloumn
        maxLen = []
        for tr in table2D:
            _longestStr(tr, maxLen)

        # Extends all strings in each column to be the same length
        for row, tr in enumerate(table2D):
            _tableRow(row, tr, table2D, maxLen)
        print()

#----------------------------------------------------------
