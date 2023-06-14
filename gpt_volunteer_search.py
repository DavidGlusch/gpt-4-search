import csv
import os
import re

import pandas as pd


def get_organization_info(path_to_used_organizations) -> str:
    with open(path_to_used_organizations, "r") as f:
        orgs = f.readlines()
    orgs = [org.strip() for org in orgs]
    return "\n".join(orgs)


def parse_organization_data(data_string):
    organizations = []

    # Split the text into blocks separated by the word 'Organization Name:'
    blocks = re.split(r'Organization Name:', data_string)[1:]

    for block in blocks:
        # Initialize an empty dictionary to hold the organization info
        org_dict = {}

        # Search for the name, website, contact info, and specialization using regex
        name = re.search(r'^(.*)\n', block)
        website = re.search(r'Website: (.*?)\n', block)
        contact = re.search(r'Contact Information: (.*?)\n', block)
        spec = re.search(r'Specialization: (.*?)(?:\n|$)', block)

        # If any of the search results are not None, add them to the dictionary
        if name is not None:
            org_dict['Organization Name'] = name.group(1).strip()
        if website is not None:
            org_dict['Website'] = website.group(1).strip()
        if contact is not None:
            org_dict['Contact Information'] = contact.group(1).strip()
        if spec is not None:
            org_dict['Specialization'] = spec.group(1).strip()

        # Add the organization info dictionary to the list
        organizations.append(org_dict)

    return organizations


# def parse_organization_data(data):
#     organizations = []
#     lines = data.strip().split("\n\n")
#
#     for line in lines:
#         org_data = line.split("\n")
#
#         organization = {
#             "Organization Name": org_data[0].split(": ")[1].strip(),
#             "Website": org_data[1].split(": ")[1].strip(),
#             "Contact Information": org_data[2].split(": ")[1].strip(),
#             "Specialization": org_data[3].split(": ")[1].strip(),
#         }
#
#         organizations.append(organization)
#
#     return organizations


def write_organizations_to_csv(filename, organizations):
    fieldnames = [
        "Organization Name",
        "Website",
        "Contact Information",
        "Specialization",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(organizations)


def extract_fields_from_csv(csv_filename):
    fields = []
    with open(csv_filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            field = {
                "Organization Name": row["Organization Name"],
                "Website": row["Website"],
                "Contact Information": row["Contact Information"],
                "Specialization": row["Specialization"]
            }
            fields.append(field)
    return fields


def write_fields_to_file(filename, fields):
    with open(filename, "a") as f:
        for field in fields:
            f.write("Organization Name: {}\n".format(field["Organization Name"]))
            f.write("Website: {}\n".format(field["Website"]))
            f.write("Contact Information: {}\n".format(field["Contact Information"]))
            f.write("Specialization: {}\n".format(field["Specialization"]))
            f.write("\n")


def append_csv(input_file, output_file):
    with open(input_file, 'r') as file_in, open(output_file, 'a', newline='') as file_out:
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)
        header = next(reader)  # do not delete, needed for correct csv appending
        writer.writerows(reader)


def get_organization_name(orgs_file):
    organization_name = []

    with open(orgs_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                organization_name.append(row[0])

    return " \n".join(organization_name)


def find_duplicates(blacklist_file, data_file, output_file):
    blacklist = pd.read_csv(blacklist_file)  # Завантаження блеклісту
    data = pd.read_csv(data_file)  # Завантаження нових даних

    duplicates = data[data['Organization Name'].isin(blacklist['Organization Name'])]  # Знаходження дублікатів організацій

    duplicates.to_csv(output_file, index=False, mode='a', header=not os.path.exists(output_file))  # Додавання дублікатів до вихідного файлу