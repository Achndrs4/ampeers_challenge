import json 
from utils import get_row_name_from_temperature, write_string_to_file, split_dict_by_key
from consts import EMAIL_INTRO, EMAIL_OUTRO, OUTSIDE_AIR_TEMPERATURES, MONTHS

def format_email_string_from_json(json_location: str) -> dict:
    with open(json_location, 'r') as file:
        data = json.load(file)
    owner_dictionaries = split_dict_by_key(data, "real estate manager")
    emails = {}
    for owner_rows in owner_dictionaries:
        owner = owner_rows[0]["real estate manager"]
        email_str = EMAIL_INTRO.format(owner)
        for row in owner_rows:
                email_str += get_transmission_data(row["street"], row["street number"])
                for outside_air_temperature in OUTSIDE_AIR_TEMPERATURES:
                    email_str += get_house_information("{:.0f}".format(outside_air_temperature), int(row[get_row_name_from_temperature(outside_air_temperature)]) / 1000)
                email_str += "\n\n"
        email_str += EMAIL_OUTRO
        emails[owner] =  email_str
    return emails

def get_house_information(outside_temperature,power) -> str:
    return "\n-Außentemperatur {} °C: {} kW".format(outside_temperature, power)

def get_transmission_data(street, street_number) -> str:
    return "Transmissionsemissionsverluste für {} {}:\n".format(street, street_number)

for month in MONTHS:
    emails = format_email_string_from_json("results/p_values_building-data-{}.json".format(month))
    for owner in emails:
        write_string_to_file(emails[owner], "results/building-email-{}-{}.txt".format(month, owner))