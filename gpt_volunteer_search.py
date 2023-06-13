import csv
import os

import pandas as pd


def get_organization_info(path_to_used_organizations) -> str:
    with open(path_to_used_organizations, "r") as f:
        orgs = f.readlines()
    orgs = [org.strip() for org in orgs]
    return "\n".join(orgs)


def parse_organization_data(data):
    organizations = []
    lines = data.strip().split("\n\n")

    for line in lines:
        org_data = line.split("\n")

        organization = {
            "Organization Name": org_data[0].split(": ")[1].strip(),
            "Website": org_data[1].split(": ")[1].strip(),
            "Contact Information": org_data[2].split(": ")[1].strip(),
            "Specialization": org_data[3].split(": ")[1].strip(),
        }

        organizations.append(organization)

    return organizations


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
        writer.writerows(reader)
