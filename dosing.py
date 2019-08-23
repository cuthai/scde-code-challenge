import pandas as pd
from Scripts import data_filter

def main(csv_files, columns_to_merge, columns_to_filter, output_columns, output_file_name):
    df_list = data_filter.data_import(csv_files)
    df = data_filter.data_merge(df_list, columns_to_merge)
    df = data_filter.data_filter(df, columns_to_filter)

    data_filter.data_output(df, output_columns, output_file_name)

if __name__ == '__main__':
    # Ideally these come from some spec doc or command line. Hard coding for now
    csv_files = ["t2_registry 20190619", "t2_ec 20190619"]
    columns_to_merge = ["RID", "VISCODE"]
    columns_to_filter = [{"variable": "VISCODE", "filter": "w02", "is": True},
                         {"variable": "SVDOSE", "filter": "Y", "is": True},
                         {"variable": "ECSDSTXT", "filter": 280, "is": False}]
    output_columns = ["ID", "RID", "USERID", "VISCODE", "SVDOSE", "ECSDSTXT"]
    output_file_name = "results"

    # Run Main
    main(csv_files, columns_to_merge, columns_to_filter, output_columns, output_file_name)