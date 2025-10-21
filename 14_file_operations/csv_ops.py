# Working With CSV files

import csv

# READING

# Read Data Of My CSV File
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # print(csv_reader)
    for row in csv_reader:
        print(row)

print("="*60)

# Assume, We have 10000 customer
# Requirememt : Fetch me customers from Hyderabad
find_by_city = "Pune"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # Get location/Hyderabad Customers
    for row in csv_reader:
        # list works on index basis
        # print(row[3])
        if row[3] == find_by_city:
            print(row)

print("="*60)

# Requirememt : Fetch me customers using gmail
find_by_mail = "@gmail.com"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # Get gmail Customers
    for row in csv_reader:
        # list works on index basis
        # print(row[3])
        if row[1].endswith(find_by_mail):
            print(row)

print("="*60)

# Using DictReader
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)

print("="*60)

# Assume, We have 10000 customer
# Requirememt : Fetch me customers from Hyderabad
find_by_city = "Pune"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    # Get location/Hyderabad Customers
    for row in csv_reader:
        if row["address"] == find_by_city:
            print(row)

print("="*60)

# Requirememt : Fetch me customers using gmail
find_by_mail = "@gmail.com"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    # Get gmail Customers
    for row in csv_reader:
        # list works on index basis
        # print(row[3])
        if row["email"].endswith(find_by_mail):
            print(row)

print("="*60)

# WRITING

with open("14_file_operations/employees.csv","w", newline='') as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Kiranmai', 'kiranmai@gmail.com', '9876543210', 'Hyderabad'])
    csv_writer.writerows([['Abhi', 'abhi@zoho.com', '9123456780', 'Bangalore'],
['Harika', 'harika@yahoo.com', '9988776655', 'Chennai'],
['Ravi', 'ravi@yahoo.com', '9090909090', 'Pune']])
    

# APPENDING

with open("14_file_operations/employees.csv","a", newline='') as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Kiranmai', 'kiranmai@gmail.com', '9876543210', 'Hyderabad'])
    csv_writer.writerows([['Abhi', 'abhi@zoho.com', '9123456780', 'Bangalore'],
['Harika', 'harika@yahoo.com', '9988776655', 'Chennai'],
['Ravi', 'ravi@yahoo.com', '9090909090', 'Pune']])
    csv_writer.writerows([['Abhi', 'abhi@zoho.com', '9123456780', 'Bangalore'],
['Harika', 'harika@yahoo.com', '9988776655', 'Chennai'],
['Ravi', 'ravi@yahoo.com', '9090909090', 'Pune']])
    
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_operations/employees.csv","w", newline = " ") as file_data:
    csv_writer = csv.DictWriter(file_data, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'email': 'manjula@yahoo.com', 'name': 'Manjula', 'mobile': '9801234789', 'address': 'Vemulawada'})