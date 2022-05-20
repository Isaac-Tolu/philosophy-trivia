import re
import requests
from argparse import ArgumentParser
from bs4 import BeautifulSoup

parser = ArgumentParser(description='Fastest Road to Philosophy')
parser.add_argument('page', help='Valid Wikipedia page')
args = parser.parse_args()

regex = re.compile('^(/wiki/)((?!:).)*$')

def main():
    wikiUrl = f'/wiki/{args.page}'

    philosophyCheck = False     # What if random page is philosophy?
    while not philosophyCheck:
        print(wikiUrl[6:])
        page = getPage(f'http://en.wikipedia.org/{wikiUrl}')
        soup = prepareSoup(page)
        firstLink = findFirstLink(soup)
        wikiUrl = firstLink
        philosophyCheck = performChecks(firstLink)
    print('\nFound Philosophy')

def getPage(url):
    res = requests.get(url)
    return res.text

    # Exceptions
    #   - Page does not exist or internal server error
    #   - Wikipedia is down thus server is nor found (URL error)

def prepareSoup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def findFirstLink(soup):
    firstParagraph = soup.find('div', attrs={'id': 'bodyContent'}) \
        .find('p', attrs={'class': None})

    # Exceptions
    #   - Tags are not found: None or Attribute Error
    
    # It cannot yet check for parenthesized links
    for link_tag in firstParagraph.find_all('a', href=regex):
        if link_tag.find_parent().name != 'i':
            return link_tag.attrs['href']

        # What if a main link is not in the first paragraph

def performChecks(link):
    if link == '/wiki/Philosophy':
        return True
    return False

    # Assumption: Every page gets to philosphy
    # Other Checks:
    #   - A red link: Page doesn't yet exist or has been deleted
    #   - A loop occurs

# Functions
#   - 

if __name__ == '__main__':
    main()