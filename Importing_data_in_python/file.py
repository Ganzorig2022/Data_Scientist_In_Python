import requests
import pandas as pd

# Download the file using requests
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
response = requests.get(url)

# Save to file
with open('winequality-red.csv', 'wb') as file:
    file.write(response.content)

print("File downloaded successfully!")

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())