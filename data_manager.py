import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

SHEETY_API_ENDPOINT = "https://api.sheety.co/45e9136f2c27586e7b04f8df9b2fbc77/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = []

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_API_ENDPOINT, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city["id"]}",
                auth=self.authorization,
                json=new_data
            )
            print(response.text)