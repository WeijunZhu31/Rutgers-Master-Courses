import copy
import os
import re
# from datetime import datetime
# import pandas

### Handle the Date of the data ###
label = input("What categorical of data do you want to handle (entertainment, politics, us, world)? ")
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






