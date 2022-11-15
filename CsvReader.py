from bs4 import UnicodeDammit
import pandas as pd

from system import FileManager

class CsvReader():
    def __init__(self,filename):
        self.filename = filename
        with open(filename, 'rb') as file:
            content = file.read()
            suggestion = UnicodeDammit(content)
            self.encodingData = suggestion.original_encoding

    def check_encoding_type(self):
        try:
            with open(self.filename, encoding=str(self.encodingData), errors='replace') as file:
                fd = pd.read_csv(file)
                print(f"Encoding: {self.encodingData} Readable: Yes")
                return {"encoding": self.encodingData}
        except Exception as ex:
            print(str(ex))

filemanager = FileManager()


# detect encoding
csv_reader = CsvReader(filename='data/Item List VM-MD365NAV2017_NAV2017USER 2022-10-28T21_42_45.csv')

# retrive encoding details
encc = csv_reader.check_encoding_type()

# convert the file into UTF-8 Standered
filemanager.utf_8_file_converter('data','Item List VM-MD365NAV2017_NAV2017USER 2022-10-28T21_42_45.csv',encoding_type=encc['encoding'])