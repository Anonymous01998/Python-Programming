#NAME - Goutham Selvakumar
#DATE - 02/16/2022
#LINK - "https://www.loom.com/share/ed94ac8f656e4ceaae8334318a6094f9"
# "I have not given or recieved any unauthorized assistance on this assignment."


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
from collections import Counter
import re

depth = 0
visited = set()
dictionary = {}

def crawl_fn(url):
    global depth
    global visited
    global dictionary
    visited.add(url)
    depth += 1
  
    links = analyze(url)
      # analyze() returns a list of hyperlink URLs in web page url
    if (depth <= 3):
        for link in links:
            if link not in visited and \
                    ('https://law.depaul.edu/Pages/default.aspx' in link) and \
                    ('Course' not in link) and \
                    ('library' not in link):
                try:
                    crawl_fn(link)   # Calls crawl_fn recursively
                except:
                    pass

def analyze(url):
    '''this function will accept the url and calls the collector class'''

    print('\n\nVisiting', url)   # obtain links in the web page
    content = urlopen(url).read().decode().lower()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()        # gets list of links
    collector.handle_data(content)     
    content = collector.getData()      
    freq(content)                       # Get dictionary with words and count

    return urls

class Collector(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = []

    def handle_starttag(self, tag, attrs):
        '''Collects hyperlink URLs in their format'''

        if tag == 'a':
            for x in attrs:
                if x[0] == 'href':
                    absolute = urljoin(self.url, x[1])  
                    if absolute[:4] == 'http': 
                        self.links.append(absolute)

    def getLinks(self):
        '''returns hyperlinks URLs in their absolute format'''

        return self.links

    def handle_data(self, content):
        '''Handling the data'''

        if 'script' != self.lasttag and 'style' != self.lasttag:
            for x in re.findall(r'[a-zA-Z]+[^.:;_?=#/]*', content):
                self.data.append(x)

    def getData(self):
        return self.data

def dictCount(x, y):
    '''this function will store all the words and the count in a dictionary'''

    my_Dict = {**x, **y}
    for key, values in my_Dict.items():
        if key in x and key in y:
            my_Dict[key] = sum([values, x[key]])
    order_Dic = {k: v for k,
                          v in sorted(my_Dict.items(),
                                      key = lambda item: item[1],
                                      reverse = True)}  # Sorting the items in dictionary in order
    return order_Dic

global order_Dic

def freq(content):
    '''this function will give the frequency of the content '''

    global dictionary
    count = Counter(content)
    dictionary = dictCount(dictionary, count)

def main():

    crawl_fn('https://law.depaul.edu/Pages/default.aspx')
    i = 0
    for words in dictionary.items():
        if i <= 25:
            print(words) # Prints top 25 most repeated words
            i += 1

main()
