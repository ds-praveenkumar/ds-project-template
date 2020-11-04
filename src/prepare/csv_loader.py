#
# Created on Thu Nov 05 2020 1:29:10 AM
#
# author: Praveen Kumar
#
# github url: https://github.com/ds-praveenkumar/
#
# filename: csv_loader.py
#

"""
Loads the csv data from data/raw dir
"""
import pandas as pd
import sys
sys.path.append(".")
from config import config


class CSVLoader:
    """ loades all the csv files in a folder """

    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.data_dict = {}

    def read_csv(self):
        """ Reads all the csv files"""

        print("reading csv files...")
        for file_path in self.ROOT.glob("*.csv"):
            print(file_path.name)
            df_name = "df_"+str(file_path.name).split(".")[0]
            self.data_dict[df_name] = pd.read_csv(file_path)
        if self.data_dict:
            print("dataframes created:\n")
            print(self.data_dict.keys())
            return self.data_dict
        else:
            print(f"No .csv files present in {self.ROOT.as_posix()}")


if __name__ == "__main__":
    main = CSVLoader(config.Config.RAW_DATA)
    main.read_csv()
