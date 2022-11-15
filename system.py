"""
This is a System Class having helper methos for file convertion
"""

# import OS module
import os
import pandas as pd
from datetime import datetime

class FileManager():
    def directory_file_scanner(self,directory_name=''):
        try:
            dir_list = os.listdir(directory_name)
            return dir_list
        except Exception as ex:
            print(str(ex))

    def utf_8_string_converter(self, string_data):
        try:
            string_data.encode(encoding = 'UTF-8', errors = 'ignore')
            return string_data
        except Exception as ex:
            print(str(ex))
            return ''

    def utf_8_file_converter(self, directory_name, filename,encoding_type):
        try:
            with open(f'{directory_name}/{filename}', encoding=encoding_type, errors='ignore') as file:

                fd = pd.read_csv(f'{directory_name}/{filename}', encoding=encoding_type, delimiter=',')
                list_of_column_names = list(fd.columns)

                # dataset to export as converted file
                dataset={}

                # create the heads for data
                for headers in list_of_column_names:
                    dataset[headers] = []
                
                # get each line converted
                for i in range(len(fd)):
                    for col in list_of_column_names:
                        data = (str(fd[col][0]).encode(encoding = 'UTF-8', errors = 'ignore')).decode()
                        if data in ['nan','NaN']:
                            data = ' '
                        dataset[col].append(data)
                
                # putting the data into data frame
                dataFrame = pd.DataFrame(dataset)
                dataFrame.to_csv(f"{filename}_converted_{str(datetime.now())[0:10]}.csv")
                print("Converted and saved!")
        except Exception as ex:
            print(str(ex))