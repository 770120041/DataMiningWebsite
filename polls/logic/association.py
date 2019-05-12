import pandas as pd
import numpy as np
import random,string
import re
import math
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# volume: volume increases regardless if it is a buy or sell order.
# number of buys plus number of sells
# amount: volume * price

# df.columns: the column name
# associate rules needs true of false? Or 0 and 1
# how to pre process??


"""
    This functions generated padded data,
    full size
"""

def generate_clean_data():
    clean_csv = open('data/retail.csv', 'w')

    # clean csv is padded to fixed width
    with open("data/retail.dat.txt") as fp:
        max_col_number = 0
        for line in fp:
            line_element = re.split(r"\s+",line)
            # print(line_element)
            max_col_number = len(line_element) if len(line_element) > max_col_number else max_col_number
        print(max_col_number)

        # add header here:
        header_line = list(map(str, range(1,max_col_number+1)))
        clean_csv.write(",".join(header_line) + "\n")

        # read file again
        for line in fp:
            line_element = list(filter(None, re.split(r"\s+", line)))
            line_element = np.array(list(map(int, line_element)))
            # add 1 means number the item from 1
            line_element = np.add(np.ones(line_element.shape), line_element)
            # line_element = np.concatenate((line_element, np.array((max_col_number - len(line_element))*[0]))).astype(int)
            new_line = ",".join(str(elements) for elements in line_element)
            clean_csv.write(new_line + "\n")

    clean_csv.close()


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# This function return a dict that map number to random_name

def get_random_name_dict(item_size):
    character_size = int(math.pow(item_size, 1/26.0)+2)
    name_set = set()

    # generate item_size new name into name_set
    for i in range(item_size):
        condition = True
        while condition:
            # new_name = "No." + str(i + 1)
            new_name = str(i+1) + random_word(character_size)
            condition = new_name in name_set
        name_set.add(new_name)

    return dict(zip(range(item_size), name_set))


def get_numbered_name_dict(item_size):
    name_list = []
    for i in range(item_size):
        name_list.append("No."+str(i))
    return dict(zip(range(item_size), name_list))


def get_true_false_line(line_list, name_dict):
    true_false_value = []
    for i in range(len(name_dict)):
        if i in line_list:
            true_false_value.append(True)
        else:
            true_false_value.append(False)
    return ",".join([str(x) for x in true_false_value])




"""
    This function can generated two kinds of data:
     1.random name stands for an item
     2. No.item_number stands for an item
     
    It generated a True_false matrix at last stands for if a customer buys one kinds of item
    Each line stands for a customer's order
    Each column stands for a kind of an item, and position [i,j] stands for customer i buys item j or not.
"""


def generate_filtered_data(item_size = 500, data_line_num = 5000, item_name_method = "numbered"):
    clean_csv = open('data/filtered_retail.csv', 'w')

    Swither = {
       "numbered": get_numbered_name_dict,
        "random": get_random_name_dict
    }
    name_dict_fecter = Swither.get(item_name_method)
    name_dict = name_dict_fecter(item_size)

    # add header here:
    header_line = [name_dict[x] for x in range(item_size)]
    clean_csv.write(",".join(header_line) + "\n")

    with open("data/retail.dat.txt") as fp:
        data_line_cnt = 0
        for line in fp:
            # only select elements less than item_size
            line_listed = np.array([ x for x in np.array(list(map(int, filter(None, re.split(r"\s+", line))))) if x < item_size])
            # map this list to a line of True and False
            new_line = get_true_false_line(line_listed, name_dict)
            clean_csv.write(new_line + "\n")

            data_line_cnt += 1
            if data_line_cnt == data_line_num:
                break

    clean_csv.close()


if __name__ == '__main__':
    """
        data set from: http://fimi.uantwerpen.be/data/
        process the raw data: http://fimi.uantwerpen.be/data/retail.dat
        to csv
    """
    # generate_clean_data()

    generate_filtered_data(100, 1000)

    df = pd.read_csv("data/filtered_retail.csv")

    # print(df)

    frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)
    print(frequent_itemsets)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)
    print(rules)
