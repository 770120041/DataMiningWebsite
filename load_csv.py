
from polls.models import DataFrameModel
from polls.csv_handler import *
import pandas as pd



CSV_PATH = {
        "1": "polls\\data\\1_3cweka.csv",
        "2": "polls\\data\\2_chinese_stock.csv",
        "3": "polls\\data\\3_license_plate.csv",
        "4": "polls\\data\\4_hapiness.csv"
    }

for key in CSV_PATH.keys():
    try:
        go = DataFrameModel.objects.get(data_frame_name=key)
        # print("already_exist")
    except DataFrameModel.DoesNotExist:
        kwargs = {
            "data_frame_name": key,
            "data_frame_path": CSV_PATH[key],
        }
        csv = DataFrameModel(**kwargs)
        csv.save()
