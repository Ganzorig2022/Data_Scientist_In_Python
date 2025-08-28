import requests
import pandas as pd
import matplotlib.pyplot as plt

# Download the file using requests
csvUrl = (
    "https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
)

excelUrl = "https://assets.datacamp.com/course/importing_data_into_r/latitude.xls"
response1 = requests.get(csvUrl)
response2 = requests.get(excelUrl)

# Save to file locally
# with open('winequality-red.csv', 'wb') as file:
#     file.write(response.content)
latitudeExcel = 'latitude.xls'
with open(latitudeExcel, 'wb') as file:
    file.write(response2.content)

# print("File downloaded successfully!")

# Read file into a DataFrame and print its head
# df = pd.read_csv("winequality-red.csv", sep=";")
# print(df.head())


# Plot first column of df
# df.iloc[:, 0].hist()
# plt.xlabel("fixed acidity (g(tartaric acid)/dm$^3$)")
# plt.ylabel("count")
# plt.show()

file_path = "./latitude.xls"
xls = pd.read_excel(file_path, sheet_name=None)
# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())