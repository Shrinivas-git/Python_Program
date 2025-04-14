import pandas as pd
import numpy as np
data = {
    "Name": ["Raju", "sanu", np.nan, "annu", "durgav"],
    "Age": [2, np.nan, 30, 28, 22],
    "Score": [85, 90, np.nan, 75, 88]
}
df = pd.DataFrame(data)
print("Missing data:")
print(df.isnull())
df.fillna(value=10,inplace=True)
print(df)
print("\nDataFrame after replacing missing values:")
print(df)
