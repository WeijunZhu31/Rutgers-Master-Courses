"""

"""

import numpy as np
import pandas as pd
import os
import re
import copy


label = input("What categorical of data do you want to handle (entertainment, politics, us, world)? ")

### Handle the content of the data ###
content_list = []
# Be careful: the index sorted by the firs number of the number, like: 0,1,10,100,101,102...
index_list = []
for root, dirs, files in os.walk("./content/{}/".format(label)):
    for name in files:
        name = os.path.join(root, name)
        # print(name)
        index_list.append(int(re.search(r"\d+", name).group()))
        with open(name, "r", encoding="utf-8") as f:
            f = f.read()
            content_list.append(f)
# print(index_list)
# print(content_list)
print("The length of the content_list : {}".format(len(content_list)))

### Handle the Titles of the data ###
with open(r"news_link/{}.txt".format(label), "r", encoding="utf-8") as f:
    # Read the txt flies, and ignore the line-feed.
    raw_content = f.read().splitlines()
for line in raw_content:
    # Delete the \ in the dict
    storage01 = line.strip('\\')
# Extract the Title from dict, and save into a list
title_list_raw = list(eval(storage01).keys())
# let each title matches to the order of index_list
title_list = []
for i in index_list:
    title_list.append(title_list_raw[i])

print(title_list)
print("The length of the titles_list : {}".format(len(title_list)))


### Handle the Date of the data ###
date_list = []
index_list = []
for root, dirs, files in os.walk("./news_date/{}/".format(label)):
    for name in files:
        name = os.path.join(root, name)
        # print(name)
        index_list.append(int(re.search(r"\d+", name).group()))
        with open(name, "r", encoding="utf-8") as f:
            f = f.read()
            date_list.append(f)
# print(index_list)
# print(date_list)

# strip the blank spaces of the elements
date_temp = []
for i in date_list:
    i = i.replace(" ", "")
    date_temp.append(i)
date_list = copy.deepcopy(date_temp)
print(date_list)
print("The length of the content_list : {}".format(len(date_list)))

# Add the specific year
date_temp = []
for i in date_list:
    if "January" in i:
        i = "2020," + i
    if "February" in i:
        i = "2020," + i
    if "March" in i:
        i = "2020," + i
    if "April" in i:
        i = "2020," + i
    if "May" in i:
        i = "2019," + i
    if "June" in i:
        i = "2019," + i
    if "July" in i:
        i = "2019," + i
    if "August" in i:
        i = "2019," + i
    if "September" in i:
        i = "2019," + i
    if "October" in i:
        i = "2019," + i
    if "November" in i:
        i = "2019," + i
    if "December" in i:
        i = "2019," + i
    date_temp.append(i)
date_list = copy.deepcopy(date_temp)
print(date_list)

# Replace the months with the number, like: February --> 2
date_temp = []
for i in date_list:
    i = i.replace("January", "1,")
    i = i.replace("February", "2,")
    i = i.replace("March", "3,")
    i = i.replace("April", "4,")
    i = i.replace("May", "5,")
    i = i.replace("June", "6,")
    i = i.replace("July", "7,")
    i = i.replace("August", "8,")
    i = i.replace("September", "9,")
    i = i.replace("October", "10,")
    i = i.replace("November", "11,")
    i = i.replace("December", "12,")
    date_temp.append(i)
date_list = copy.deepcopy(date_temp)
print(date_list)


Title = pd.DataFrame({"Title": title_list})
Content = pd.DataFrame({"Content": content_list})
Date = pd.DataFrame({"Date": date_list})

# Save the data into a dataFrame
temp = pd.concat([Title, Content, Date], axis=1)
temp["Category"] = "{}".format(label)
print(temp)

# Save the data to the csv file
# temp.to_csv(r"./data/{}.csv".format(label), encoding="utf-8")
temp.to_json(r"./data/{}.txt".format(label))


data = pd.read_json(r"./data/{}.txt".format(label))
print(len(data["Title"]))
print(len(data["Content"]))
print(len(data["Date"]))
