import pandas as pd
import matplotlib.pyplot as plt

dict = {
    "Movie": ["Shawshank Redemption", "Catch Me If You Can", "Inception", "Interstellar", "The Dark Knight"],
    "IMDb_Rating": [9.3, 8.1, 8.8, 8.6, 9.0],
    "Box_Office": [28, 3, 8, 6, 10]
}
df=pd.DataFrame(dict)
# Bar Plot
plt.bar(df['Movie'], df['IMDb_Rating'])
plt.show()

# Histogram
plt.hist(df['IMDb_Rating'])
plt.show()

# Line Plot
plt.plot(df['Movie'], df['IMDb_Rating'])
plt.show()

# Scatter Plot
plt.scatter(df['IMDb_Rating'], df['Box_Office'])
plt.show()
