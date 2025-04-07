import pandas as pd
data_dict={'a':100,'b':200,'c':300,'d':400}
series = pd.Series(data_dict)

print("Pandas series:\n", series)

print("\nElement with label 'a':", series['a'])

print("\nValue associatedwith key 'b'\n", series['b'])

print("\nSubstracting 50 from each element\n", series-50)
print("\nElements greater than 250 ",series[series>250])