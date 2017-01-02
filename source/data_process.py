#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import ast
import csv

def process(path, final_path):
    for city in os.listdir(path):
        df = pd.read_csv(path + city)
        keep_col = ['trip_path_detail']
        new_f = df[keep_col]
        new_f.to_csv(final_path + city, index=False)


if __name__ == '__main__':
    path = 'tripdetail_dataset/'
    final_path = 'final_dataset/'
    process(path, final_path)
