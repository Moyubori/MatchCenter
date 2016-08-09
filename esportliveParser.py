import urllib
import re
from HTMLParser import HTMLParser

class MyParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.nested = 0
        self.container = []
        self.titles = []
        self.reg1 = re.compile("(\\r+.+)|(\\n+.+)")
        self.reg2 = re.compile("l_pl_e_[0-9]+-.+")

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            for name, value in attrs:
                if name == 'class' and value == 'event-time init-click-done':
                    self.nested += 1
        if tag == 'a':
            if attrs[0][0] == 'href' and self.reg2.match(attrs[0][1]):
                self.titles.append(attrs[1][1])

    def handle_endtag(self, tag):
        if tag == 'td' and self.nested:
            self.nested -= 1

    def handle_data(self, data):
        if self.nested:
            if not self.reg1.match(data):
                self.container.append(data)


class PageData:

    def __init__(self):
        self.parser = MyParser()
        self.response = urllib.urlopen('http://esportlivescore.com/l_pl_g_csgo.html')
        self.html = self.response.read()
        self.parser.feed(self.html)
        self.packedData = []
        self.__PackData()

    def __PackData(self):
        j = 0
        for i in range(len(self.parser.titles)):
            j = 3 * i
            self.packedData.append((self.parser.titles[i], self.parser.container[j], self.parser.container[j + 1]))
        self.__SortData()

    def PrintData(self):
        for i in self.packedData:
            print i

    def __Compare(self, arg1, arg2):
        date1 = arg1[2].split("/", 1)
        date2 = arg2[2].split("/", 1)
        if date1[1] > date2[1]:
            return 1
        elif date1[1] == date2[1] and date1[0] > date2[0]:
            return 1
        elif date1[1] < date2[1]:
            return -1
        elif date1[1] == date2[1] and date1[0] < date2[0]:
            return -1
        elif date1[1] == date2[1] and date1[0] == date2[0]:
            time1 = arg1[1].split(":", 1)
            time2 = arg2[1].split(":", 1)
            if time1[0] > time2[0]:
                return 1
            elif time1[0] == time2[0] and time1[1] > time2[1]:
                return 1
            elif time1[0] == time2[0] and time1[1] == time2[1]:
                return 0
            else:
                return -1

    def __SortData(self):
        self.packedData = sorted(self.packedData, cmp=lambda x,y: self.__Compare(x,y))
































