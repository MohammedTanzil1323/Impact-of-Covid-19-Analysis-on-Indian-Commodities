import os 
import pandas as pd
# let's make a list comprehension for all the data in the folder
files = [file for file in os.listdir("feb 1-29 ds")] 
# let's make a pandas DataFrame
all_months_data = pd.DataFrame()
# makes a loop for concat the data
for file in files:
    data = pd.read_excel("feb 1-29 ds" + file)
    all_months_data = pd.concat([all_months_data, data])
