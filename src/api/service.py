import requests

from names_checking.bitrix_data import webhook_url, gender_array_id


def get_gender_value(gender_id):
    contact_list = f"{webhook_url}/crm.contact.userfield.get"
    params = {'ID': gender_array_id}

    response = requests.get(contact_list, params=params)
    if response.status_code.__eq__(200):
        data = response.json().get('result')
        for gender in data["LIST"]:
            if gender["ID"] == gender_id:
                return gender["VALUE"]
    else:
        return None
