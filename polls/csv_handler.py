import csv
import pandas as pd

def red_negative_color(val):
    color = 'red' if val < 0 else 'black'
    return 'color:%s' %color


def csv_to_html(path):
    df = pd.read_csv(path)
    print (df.columns)
    return df.to_html