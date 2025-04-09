import pandas as pd
names=['Alice','bob','charlie','david','eve','frank','grace']
ages =[23,35,45,25,33,36,20]
salaries=[70000,80000,120000,90000,60000,75000,85000]
df= pd.DataFrame({'name':names,'age':ages,'salary':salaries})
print("Pandas df:\n",df )

print("\nDescriptive of df", df.describe())

print("\nfirst 5 rows",df.head())

print("\nlast 5 rows of df",df.tail())
