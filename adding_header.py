import pandas as pd

df = pd.read_csv("file2.csv", header=None)
df.to_csv("colors.csv", header=["general_color_name", "color_name", "hex", "red", "green", "blue"], index=True)