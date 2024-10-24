import numpy as np
import pandas as pd
file_path = "C:\\Users\Pc\Downloads\\State_Region_corrected.csv"

df = pd.read_csv(file_path)

s = (df.dtypes == 'object')
object_cols = list(s[s].index)
df1 = df.copy()
df2 = df.copy()
for col in object_cols:
    unique_vals = df1[col].unique()
    for val in unique_vals:
        new_col_name = f'{col}_{val}'
        df1[new_col_name] = np.where(df1[col] == val, 1, 0)  # we create a new column in df1 that get filled with np.where function
    df1 = df1.drop(col,axis = 1)
print(df1)
mapping = {}
for col in object_cols:
        unique_vals = np.unique(df2[col])
        mapping[col] = {val: idx for idx, val in enumerate(unique_vals)}
        df2[col] = df2[col].map(mapping[col])
print(mapping)
print(df2)