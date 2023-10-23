import pandas as pd
import json
import chardet

# Determine the encoding of the Excel file
with open('190394R - CS4642.xlsx', 'rb') as excel_file:
    result = chardet.detect(excel_file.read())

# Convert the detected encoding to a codec
encoding = result['encoding']

# Read the Excel file using openpyxl with the detected encoding
df = pd.read_excel('190394R - CS4642.xlsx', engine='openpyxl', dtype=str)

# Convert the DataFrame to a list of dictionaries
data_list = df.to_dict(orient='records')

# Write the data to a JSON file
with open('dataset/data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("Data has been successfully written to data.json")
