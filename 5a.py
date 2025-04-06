import pandas as pd

data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']
series = pd.Series(data, index=labels)

print("Pandas series:\n", series)

# Accessing the element with label 'a'
print("\nElement with label 'a':", series['a'])

# Adding 5 to each element in the series
print("\nAdding 5 to each element in the series:\n", series + 5)

# Elements greater than 25
print("\nElements greater than 25:\n", series[series > 25])
