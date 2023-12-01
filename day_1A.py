import pandas as pd
import numpy as np
import math

# Read data into a dataframe, one column with raw data
data = pd.read_csv('data/day1.csv', header = None, skip_blank_lines = False)
data.columns = ['raw']

# Step by step to make it easy:
# Remove non-numbers, get first and last, combine them, turn into integer
data['clean'] = data['raw'].str.replace('\D', '', regex = True)
data['first'] = data['clean'].str[0]
data['last'] = data['clean'].str[-1]
data['combo'] = data['first'] + data['last']
data['combo_number'] = data['combo'].apply(int)

# Sum integers and voila.
print(data.combo_number.sum())
