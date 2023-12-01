import pandas as pd
import numpy as np
import math

# Read data into a dataframe, one column with raw data
data = pd.read_csv('data/day1.csv', header = None, skip_blank_lines = False)
data.columns = ['raw']

# Ugly way to clean data properly.
# Need to replace like this so a string like 'eightwo' results in both 8 and 2 showing up,
# instead of just whichever replacement I execute first.

data['clean'] = data['raw']
data['clean'] = data['clean'].str.replace('one', 'one1one', regex = True)
data['clean'] = data['clean'].str.replace('two', 'two2two', regex = True)
data['clean'] = data['clean'].str.replace('three', 'three3three', regex = True)
data['clean'] = data['clean'].str.replace('four', 'four4four', regex = True)
data['clean'] = data['clean'].str.replace('five', 'five5five', regex = True)
data['clean'] = data['clean'].str.replace('six', 'six6six', regex = True)
data['clean'] = data['clean'].str.replace('seven', 'seven7seven', regex = True)
data['clean'] = data['clean'].str.replace('eight', 'eight8eight', regex = True)
data['clean'] = data['clean'].str.replace('nine', 'nine9nine', regex = True)
data['clean'] = data['clean'].str.replace('\D', '', regex = True)

# Step by step to make it easy:
# Then again get first and last, combine them, turn into integer
data['first'] = data['clean'].str[0]
data['last'] = data['clean'].str[-1]
data['combo'] = data['first'] + data['last']
data['combo_number'] = data['combo'].apply(int)

# Sum integers and voila.
print(data.combo_number.sum())
