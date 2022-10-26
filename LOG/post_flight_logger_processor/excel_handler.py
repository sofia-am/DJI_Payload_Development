import pandas as pd

def open_excel_file():
    # path = input("Write the path to the .csv file\n")
    data = pd.read_csv('/home/juanmagil/Escritorio/dji_log.csv')
    print(data[3,5])
    
open_excel_file()