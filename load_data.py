from polls.models import DataFrameModel

# load_csv file
CSV_PATH = {
        "cweka": "1_3cweka.csv",
        "chinese_stock": "2_chinese_stock.csv",
        "license_plate": "3_license_plate.csv",
        "hapiness": "4_hapiness.csv"
    }

for key in CSV_PATH.keys():
    # if exist delete
    try:
        go = DataFrameModel.objects.get(df_description=key)
        go.delete()
        # print("already_exist")
    except DataFrameModel.DoesNotExist:
        pass
    kwargs = {
        "df_description": key,
        "df_stroed_name": CSV_PATH[key],
    }
    csv = DataFrameModel(**kwargs)
    csv.save()

# load method database