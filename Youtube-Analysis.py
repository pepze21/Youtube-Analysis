

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_excel('Youtube-data.xlsx', sheet_name = 0, header = 0)
df = df.drop(index = 0, axis = 0)
df = df.drop(columns = ['동영상', '동영상 제목', '동영상 게시 시간'])

print(df.head())
print(df.tail())


