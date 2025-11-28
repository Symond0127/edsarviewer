import pandas as pd
import os

# #Target CSV file
# csv_path = 'edsarviewer/data.csv'
# excel_path = 'edsarviewer/converted.xlsx'

# #Get only selected columns in CSV file
# desired_columns = ['DeviceName', 'LotNo', 'TestNG No1', 'TestNG No2', 'TestNG No3', 'Analysis Comment', 'Instructions']

# #csv_path = os.path.join('\\172.27.19.3\\web\\edsarviewer\\data.csv') #CSV file path location 
# #excel_path = os.path.join('\\172.27.19.3\\web\\edsarviewer\\converted.xlsx') #Excel file path location

# #Read the CSV file into a Dataframe, selecting only the desired columns
# df = pd.read_csv(csv_path, usecols=desired_columns)
# df.to_excel(excel_path, index=False, sheet_name='Sheet1')

print("SUCCESSFULLY CONVERTED!")