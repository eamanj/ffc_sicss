#!/usr/bin/python

import argparse
from collections import defaultdict
import pandas as pd
import numpy as np
import sys
import requests

CATEGORICAL_UNIQ_VALS = 7

def main():
  meta_file = "./FFChallenge_v5/FFMetadata20180221.csv"
  meta_data = pd.read_csv(meta_file)
  cont_vars = meta_data.loc[meta_data['type'] == 'cont', 'new_name']
  categ_vars = meta_data.loc[meta_data['type'].isin(['oc', 'uc', 'string']), 'new_name']
  bin_vars = meta_data.loc[meta_data['type'] == 'bin', 'new_name']

  input_file = "./FFChallenge_v5/background.csv"
  input_data = pd.read_csv(input_file, sep=',')
 
  cont_data = input_data[cont_vars]
  categ_data = input_data[categ_vars]
  bin_data = input_vars[bin_vars]

  challenge_id = input_data["challengeID"]
  cont_data = cont_data.fillna(cont_data.mean()) 
  categ_data = categ_data.apply(lambda x:x.fillna(x.value_counts().index[0]))
  bin_data = bin_data.apply(lambda x:x.fillna(x.value_counts().index[0]))
  
  









  numeric_cols = input_data.select_dtypes(include=['float64', 'int64']).columns.values

  categ_vars = num_uniq_vals[num_uniq_vals < CATEGORICAL_UNIQ_VALS].index.values
  cont_vars = num_uniq_vals[num_uniq_vals >= CATEGORICAL_UNIQ_VALS].index.values
  categ_data = input_data[categ_vars]
  cont_data = input_data[cont_vars]
  
  cont_data = cont_data.fillna(cont_data.mean())



if __name__ == "__main__":
  main()
