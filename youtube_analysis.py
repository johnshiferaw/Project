import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("USvideos.csv")  # Match filename CASE exactly!

# Show top 5 trending videos
print("Top 5 Trending Videos:")
print(data[["title", "channel_title", "views"]].head(5))  # Fixed 'data' and brackets

# Plot views vs. likes
data.plot.scatter(x="views", y="likes", alpha=0.5)  # 'x=' not 'a='
plt.title("YouTube Views vs Likes")
plt.show()