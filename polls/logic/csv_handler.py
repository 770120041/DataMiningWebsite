import csv
import pandas as pd
import numpy as np

import os

def get_root_path():
    abs_path = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.dirname(os.path.dirname(abs_path))
    # root_path = os.path.dirname(app_path)
    return root_path


def df_to_html(df):
    return df.to_html


def save_csv_file(df, path):
    final_path = path
    print("at csv_handler, save_csv_file, file_path:",path)
    df.to_csv(final_path)


def read_csv_file(path):
    # print("path is :"+path)
    df = pd.read_csv(path)
    return df


def drop_na(df):
    # drop na data at first
    df = df.dropna()
    return df


def char_to_digit(df):
    """
    This function changes columns containing non_digit to a digit
    :param df:
    :return: df that changes non-numerical columns to digit
    """
    col_names = df.columns
    bad_col_name = []
    for col_name in col_names:
        if np.issubdtype(df[col_name].dtype, np.number) != True:
            bad_col_name.append(col_name)

    # show_df is only used for shown purpose
    # df is used to remove the non_numeric

    show_df = df.copy(deep=True)
    for col in bad_col_name:
        # starts from 1, uniques is not used now
        labels, uniques = pd.factorize(df[col])
        show_df[col + "_digit"] = pd.Categorical(labels + 1)

    df = show_df.drop(columns=bad_col_name)

    return df