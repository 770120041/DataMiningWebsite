import pandas as pd
import numpy as np
import random, string
import re
import math
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def do_association_rule(df):
    frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)
    print(frequent_itemsets)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)
    print(rules)

    return frequent_itemsets,rules