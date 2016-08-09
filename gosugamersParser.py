import urllib
import re
from HTMLParser import HTMLParser

class MyParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.nested = 0
        self.container = []
        self.reg1 = re.compile("([A-Za-z0-9]+|\([0-9]+\%\))");
        self.reg2 = re.compile("bet-percentage bet[1-2]")
        self.boxCounter = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'table' and attrs:
            if attrs[0][0] == 'class' and attrs[0][1] == 'simple matches':
                self.boxCounter += 1
        if tag == 'span' and attrs and self.boxCounter < 3:
            if attrs[0][0] == 'class' and attrs[0][1] == 'opp opp1':
                self.nested += 1
            if attrs[0][0] == 'class' and attrs[0][1] == 'opp opp2':
                self.nested += 2
            if attrs[0][0] == 'class' and self.reg2.match(attrs[0][1]):
                self.nested += 1

    def handle_endtag(self, tag):
        if tag == 'span' and self.nested:
            self.nested -= 1

    def handle_data(self, data):
        if self.nested and self.reg1.match(data):
            self.container.append(data)


class PageData:

    def __init__(self):
        self.parser = MyParser()
        self.response = urllib.urlopen('http://www.gosugamers.net/counterstrike/gosubet')
        self.html = self.response.read()
        self.parser.feed(self.html)
        self.packedData = []
        self.__PackData()

    def __PackData(self):
        i = 0
        while i < len(self.parser.container) - 3:
            self.packedData.append((self.parser.container[i], self.parser.container[i + 1],
                                    self.parser.container[i + 2], self.parser.container[i + 3]))
            i += 4


    def PrintData(self):
        for i in self.packedData:
            print i