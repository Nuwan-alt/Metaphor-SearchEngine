import pandas as pd
import json
import chardet

# Determine the encoding of the Excel file
with open('190394R - CS4642.xlsx', 'rb') as excel_file:
    result = chardet.detect(excel_file.read())

encoding = result['encoding']

df = pd.read_excel('190394R - CS4642.xlsx', engine='openpyxl', dtype=str)

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

data_list = df.to_dict(orient='records')

with open('dataset/data1.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("Data has been successfully written to data.json")