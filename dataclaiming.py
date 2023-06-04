import csv
import pandas as pd
data = pd.read_csv("dwarf_stars.csv")
# print(data.shape) # 4284 , 85

# del data['hyperlink']
# print(data.shape)
data = data[data['column_name'].notna()]
# print(data.shape)
data.to_csv('bright_stars.csv')

