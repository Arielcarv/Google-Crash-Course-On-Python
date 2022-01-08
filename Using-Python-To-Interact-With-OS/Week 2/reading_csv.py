#!/usr/bin/env python3
import csv

## Reading CSV
file = open("csv_file.txt")
csv_file = csv.reader(file)
print(csv_file)

for row in csv_file:
    name, surname, address, location, city, PO = row
    print(f"Name: {name}. Surname: {surname}, Address: {address}, City: {city}, PO: {PO}")

file.close()

## Writing CSV
hosts = [['workstation.local', '192.168.25.46'], ['webserver.cloud', '10.2.5.6']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
hosts_csv.close()

## Reading CSV as a DICTIONARY
with open('software.csv') as software_info:
    reader = csv.DictReader(software_info)
    for row in reader:
        print(f'{row["name"]} has {row["users"]} users.')
software_info.close()

## Writing CSV as a DICTIONARY
users = [
    {"name":"Sol Mansi", "username": "solm", "department": "IT Infrastructure"},
    {"name":"Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name":"Charlie Grey", "username": "greyc", "department": "Development"}
]
keys = ["name", "username", "department"]

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

by_department.close()

