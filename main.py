import os
from gpt_search import starter
from gpt_volunteer_search import (
    parse_organization_data,
    write_organizations_to_csv,
    append_csv,
    get_organization_name, find_duplicates, check_relevance, sort_and_filter_organizations,
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USED_ORGANIZATIONS_PATH = os.getenv("USED_ORGANIZATIONS_PATH")
NECESSARY_EQUIP = os.getenv("NECESSARY_EQUIP")
# ORGANIZATION_TO_GENERATE = 40


# RELEVANT_RATE = 50


def main(organizations_to_generate):
    PROMPT = f"""
        Your response is processed by a machine, not human,
        so your response should strictly be in the next format:

        Organization Name:
        Website: 
        Contact Information: (in the next format: 1 (555) 555-5555, jhondoe@gmail.com)
        Specialization: 
        
        DO NOT INCLUDE THESE ORGANIZATIONS ------->
        {get_organization_name(USED_ORGANIZATIONS_PATH)}
    <--------- DO NOT INCLUDE THESE ORGANIZATIONS
    
        Your response should not contain duplicates.
        Your goal is to generate a well-structured list of 
        volunteering organizations that have not been contacted yet
        and are suitable for Eastern Europe. Your response should 
        include at least {organizations_to_generate} organizations
        and should strictly adhere to the specified format. 
        Please only include organizations that actually exist and provide real,
        working website links (base URLs, not specific pages).
    """
    data = starter(PROMPT)
    print("-" * 40)
    print(PROMPT)
    print("-" * 40)
    organizations = parse_organization_data(data)
    organizations = check_relevance(organizations, USED_ORGANIZATIONS_PATH)
    organizations = sort_and_filter_organizations(eval(organizations), 70)
    write_organizations_to_csv("organizations.csv", organizations)
    find_duplicates(USED_ORGANIZATIONS_PATH, "organizations.csv", "duplicates.csv")
    append_csv("organizations.csv", USED_ORGANIZATIONS_PATH)
    return organizations
