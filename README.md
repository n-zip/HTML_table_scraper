# HTML-table-scraper
    Requires requests and bs4 packages.
    Scrapes url for tables matching dictionary, default attributes are empty using requests and BeautifulSoup. \n
    Prints in a neat, easy to see way

##    Example usage:
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
