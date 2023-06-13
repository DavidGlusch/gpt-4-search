import csv
import os

from gpt_search import starter
from gpt_volunteer_search import (
    parse_organization_data,
    write_organizations_to_csv,
    append_csv,
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USED_ORGANIZATIONS_PATH = os.getenv("USED_ORGANIZATIONS_PATH")
NECESSARY_EQUIP = os.getenv("NECESSARY_EQUIP")
ORGANIZATION_TO_GENERATE = 1
RELEVANT_RATE = 50
PROMPT = f"""
     The desired format for each organization is as follows:

    Organization Name:
    Website: 
    Contact information: ( for the organization in the next format: 1 (555) 555-5555, jhondoe@gmail.com)
    Specialization: (A brief description of the organization's mission and services)
    DO NOT INCLUDE THESE ORGANIZATIONS ------->
Disaster Philanthropy: Ukraine Humanitarian Crisis Recovery Fund
European Civil Protection and Humanitarian Aid Operations
Funds for NGOs: Humanitarian Solidarity Grant Program in Ukraine
Disasters Emergency Committee (DEC)
Scottish Catholic International Aid Fund (SCIAF)
Mercy Corps
People in Need
CARE International
Greenpeace International
UNICEF Europe and Central Asia
Concern Worldwide
Welthungerhilfe
World Vision International
Action Against Hunger
International Rescue Committee (IRC)
International Committee of the Red Cross (ICRC)
International Federation of Red Cross and Red Crescent Societies (IFRC)
Oxfam International
Direct Relief
Americares
Good360
Samaritan's Purse
Food First
Feed a Billion
Operation USA (OpUSA)
World Relief
Blumont
ALIGHT
Mercy Corps
German Federal Foreign Office: Humanitarian Assistance
Canadian Foodgrains Bank
International Relief Teams
All Hands and Hearts
Red Cross
Team Rubicon USA
Convoy of Hope
The Salvation Army USA
REACT International
Southern Baptist Disaster Relief (SBDR)
National Organization for Victim Assistance (NOVA)
NECHAMA
Volunteers of America (VOA)
Doctors Without Borders (MSF)
ShelterBox
Mennonite Central Committee (MCC)
World Health Organization (WHO)
Catholic Relief Services (CRS)
International Medical Corps
Caritas Europe
CONCORD Europe
ACTED
VOICE
World Evangelical Alliance (WEA)
ReliefWeb
International Council of Voluntary Agencies (ICVA)<--------- DO NOT INCLUDE THESE ORGANIZATIONS

    Your goal is to generate a well-structured list of volunteering organizations that have not been contacted yet
    and are suitable for Eastern Europe. Your response should include at least {ORGANIZATION_TO_GENERATE} organizations
    and should strictly adhere to the specified format. Please only include organizations that actually exist and provide real,
    working website links (base URLs, not specific pages).
"""


def main():
    result = starter(PROMPT)
    organizations = parse_organization_data(result)

    write_organizations_to_csv("organizations.csv", organizations)
    append_csv("organizations.csv", USED_ORGANIZATIONS_PATH)

    return organizations
