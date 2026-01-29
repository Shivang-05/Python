# with open("weather_data.csv") as dataset:
#     data_list=dataset.readlines()
#     print(data_list)
# import csv
# with open("weather_data.csv") as dataset:
#     data=csv.reader(dataset)
#     tempratures=[]
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             tempratures.append(int(row[1]))
#     print(tempratures)
import pandas
data=pandas.read_csv("weather_data.csv")
data_dict=data.to_dict()
print(data_dict)
data_temp=data["temp"].to_list()
print(data_temp)
