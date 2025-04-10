import pandas as pd
import numpy as np

data = [1,2,3,
        4,5]

df = pd.DataFrame(data)

series = pd.Series([10, 20, 30])

df_array = df.to_numpy()

series_array = series.to_numpy()

print("DataFrame as NumPy array:")
print(df_array)

print("\nSeries as NumPy array:")
print(series_array)
