import pandas as pd

# Method to pull in specified files
def data_import(csv_files):
    df_list = []

    for csv in list(csv_files):
        df_list.append(pd.read_csv(f"Data/{csv}.csv"))

    return df_list

# Method to merge data
def data_merge(df_list, columns_to_merge, merge_type = "left"):
    df = df_list[0].merge(df_list[1], how = merge_type, on = columns_to_merge)

    # Not specified which ID/UserId to return, defaulting to left column named x
    df.rename(columns = {"ID_x": "ID", "USERID_x": "USERID"}, inplace = True)

    return df

# Method to filter data
def data_filter(df, columns_to_filter):
    for column_filter in columns_to_filter:
        if column_filter["is"] == True:
            df = df.loc[df[column_filter["variable"]] == column_filter["filter"]]
        else:
            df = df.loc[df[column_filter["variable"]] != column_filter["filter"]]

    return df

# Output method
def data_output(output_df, columns_to_output, output_file_name):
    df = output_df[columns_to_output]
    df.to_csv(f"Output\{output_file_name}.csv", index = False)