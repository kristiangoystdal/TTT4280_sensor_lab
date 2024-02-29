import csv
from fitparse import FitFile

# Adjust the path to your FIT file
fit_file_path = 'garmin_data/fit_files/reflection.fit'

# Open the FIT file
fitfile = FitFile(fit_file_path)

# Prepare a list to hold all the data rows
data = []

# Collect field names from all records
fieldnames = set()

# Iterate over all data messages that have a record type
for record in fitfile.get_messages('record'):
    # Store data points from this record in a dict
    record_data = {}
    for data_field in record:
        record_data[data_field.name] = data_field.value
        fieldnames.add(data_field.name)
    data.append(record_data)

# Convert fieldnames set to list
fieldnames = list(fieldnames)

# Specify your CSV file name
csv_file_path = 'your_data.csv'

# Write the data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
