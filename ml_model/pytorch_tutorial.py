import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("colors.csv")
columns = ["general_color_name", "hex", "Unnamed: 0"]
data = data.drop(columns, axis=1)
column_to_move = data.pop("color_name")
data.insert(3, "color", column_to_move)
color_list = data["color"].to_list()
color_list = list(enumerate(color_list))
color_list_dict = {}

test_measured = (246, 247, 238)
like = []
index = 0

for colors in color_list:
    color_list_dict[colors[1]] = colors[0]
    data["color"] = data["color"].replace([colors[1]], [colors[0]])
    print(colors)

while index < len(data.index):
    row = data.loc[[index]]

    like.append(
        round((((min(row.loc[index, "red"], test_measured[0]) / max(row.loc[index, "red"], test_measured[0])) * 100)
        + ((min(row.loc[index, "green"], test_measured[1]) / max(row.loc[index, "green"], test_measured[1])) * 100) 
        + ((min(row.loc[index, "blue"], test_measured[2]) / max(row.loc[index, "blue"], test_measured[2])) * 100)) 
        / 3, 3)
        )
    index += 1

list = list(enumerate(like))
list2 = sorted(list, key=lambda x:-x[1])
print(list2)