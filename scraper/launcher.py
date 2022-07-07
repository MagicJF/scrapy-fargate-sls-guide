import sys
import json

from my_sls_scraper.crawl import crawl


def scrape(event={}, context={}):
    crawl(**event)

if __name__ == "__main__":
    try:
        event = json.loads(sys.argv[1])
        print ("This is the name of the script: ", sys.argv[0])
        print ("Number of arguments: ", len(sys.argv))
        print ("The arguments are: " , str(sys.argv))
    except IndexError:
        event = {}
    scrape(event)
