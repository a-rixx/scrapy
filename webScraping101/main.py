import requests
from bs4 import BeautifulSoup as BS
# import pdb

baseurl = 'https://books.toscrape.com/catalogue/page-{}.html'
allFivers = []

for page in range(1, 50+1):
    # format url for current value of page
    res = requests.get(baseurl.format(page))
    # load content of a page
    soup = BS(res.text, 'lxml')
    # select all books from the page (took idea from page outline)
    books = soup.select("article.product_pod")
    # sequentially selecting element from the list of books(article tag objects)
    for book in books:
        # checking condition for Five star
        if len(book.select('.star-rating.Five')) != 0:
            # append it in out list and we are done
            allFivers.append(book.select('a')[1]['title'])

for fiver in allFivers:
    print(fiver)
