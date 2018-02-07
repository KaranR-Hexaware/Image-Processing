# This program will compare two json files and will give the output as TRUE if they are same, else FALSE

#import the json package to handle json files
import json

# open the json datafile. Put your data file in the same working directory. Give your filename
var_1 = open("json_data5.txt","r")
var_2 = open("json_data6.txt","r")


# store the data in a variable 
data_1 = json.load(var_1)
data_2 = json.load(var_2)


# Function to compare the json data
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


# Function call and print the output
print(ordered(data_1) == ordered(data_2))

#Close the file which was opened before
var_1.close()
var_2.close()
