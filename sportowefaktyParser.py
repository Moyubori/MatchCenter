import urllib
import re
from HTMLParser import HTMLParser

class MyParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.nested = 0
        self.container = []
        self.reg1 = re.compile("(([0-9]|[1-2][0-9]|3[0-1]) [a-z]+|[0-3] : [0-3]|godz\. ([0-9]|[0-9]{2}):[0-9]{2}|[A-Za-z]+ \- [A-Za-z]+)")
        self.newsBox = 0
        self.q = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'span' and attrs:
            if attrs[0][0] == 'itemprop' and attrs[0][1] == 'name':
                self.nested = 1
        if tag == 'time':
            self.nested = 1
        if tag == 'a':
            self.nested = 1
        if tag == 'ul' and attrs:
            if attrs[0][0] == 'class' and attrs[0][1] == 'list list-news':
                self.newsBox += 1
        if tag == 'td' and attrs:
            if attrs[0][0] == 'colspan' and attrs[0][1] == '2':
                self.q += 1


    def handle_data(self, data):
        if self.nested and not self.newsBox and self.reg1.match(data) and self.q == 2:
            self.container.append(data)
            self.nested = 0


class PageData:

    def __init__(self):
        self.parser = MyParser()
        self.response = urllib.urlopen('http://sportowefakty.wp.pl/siatkowka/kalendarz/')
        self.html = self.response.read()
        self.parser.feed(self.html)
        self.packedData = []
        self.__PackData()

    def __PackData(self):
        i = 0
        while i < len(self.parser.container):
            self.packedData.append((self.parser.container[i + 1], self.parser.container[i], self.parser.container[i + 2]))
            i += 3


    def PrintData(self):
        for i in self.packedData:
            print i