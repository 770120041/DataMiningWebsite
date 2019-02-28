import csv
import pandas as pd

def red_negative_color(val):
    color = 'red' if val < 0 else 'black'
    return 'color:%s' %color


def csv_to_html(path):
    # print("path is :"+path)
    df = pd.read_csv(path)
    return df.to_html