import pandas as pd

# Read the CSV file
data = pd.read_csv('1.csv')

# Convert the data into a list of dictionaries
records = data.to_dict(orient='records')

# Create the final JSON structure
json_data = {"records": [{"fields": record} for record in records]}

# Print the generated JSON data
print(json_data)