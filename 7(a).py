import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Movie": ["Shawshank Redemption", "Catch Me If You Can", "Inception", "Interstellar", "The Dark Knight"],
    "IMDb_Rating": [9.3, 8.1, 8.8, 8.6, 9.0],
    "Box_Office": [28, 3, 8, 6, 10]
})

plt.subplot(2, 2, 1)
plt.bar(df['Movie'], df['IMDb_Rating'], color='skyblue')
plt.subplot(2, 2, 2)
plt.hist(df['IMDb_Rating'], bins=5, alpha=0.5, color='blue')
plt.subplot(2, 2, 3)
plt.plot(df['Movie'], df['IMDb_Rating'], marker='o', color='green')
plt.subplot(2, 2, 4)
plt.scatter(df['IMDb_Rating'], df['Box_Office'], color='red')

plt.tight_layout()
plt.show()
