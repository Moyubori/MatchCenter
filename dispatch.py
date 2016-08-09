import esportliveParser
import gosugamersParser
import sportowefaktyParser

class Dispatcher():

    def __init__(self):
        self.config = []
        self.__ReadConfig()
        self.parsedData = []
        self.__GetActivePages()


    def __GetActivePages(self):
        parser1 = esportliveParser.PageData()
        parser2 = gosugamersParser.PageData()
        parser3 = sportowefaktyParser.PageData()

        file = open('conkyrc.extension', 'w')

        i = 0
        if self.config[0] != '0':
            file.write('${color orange}ESPORTSLIVE${hr 2}' + '\n')
        while i < int(self.config[0]):
            file.write('${color white}' + str(parser1.packedData[i][0]) + '${color cyan} - ${color white}' + str(parser1.packedData[i][1]) + '${color cyan} - ${color white}' + str(parser1.packedData[i][2]) + '\n')
            i += 1

        i = 0
        if self.config[1] != '0':
            file.write('\n' + '${color orange}GOSUGAMERS${hr 2}' + '\n')
        while i < int(self.config[1]):
            file.write('${color white}' + str(parser2.packedData[i][0]) + '${color cyan} : ${color white}' + str(parser2.packedData[i][1]) + ', ' + str(parser2.packedData[i][2]) + '\n')
            i += 1

        i = 0
        if self.config[2] != '0':
            file.write('\n' + '${color orange}SPORTOWEFAKTY${hr 2}' + '\n')
        while i < int(self.config[2]):
            file.write('${color white}' + str(parser3.packedData[i][0]) + '${color cyan} : ${color white}' + str(parser3.packedData[i][1]) + ', ' + str(parser3.packedData[i][2]) + '\n')
            i += 1

        file.close()

    def __ReadConfig(self):
        with open('config.conf', 'r') as file:
            for line in file:
                (key, value) = line.split()
                self.config.append(value)

d = Dispatcher()


