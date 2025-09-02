import requests
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import time

# This might work for some endpoints without API key
# url = "https://api.coingecko.com/api/v3/coins/markets"
# params = {
#     "vs_currency": "usd",
#     "order": "market_cap_desc",
#     "per_page": 10,
#     "page": 1,
#     "sparkline": "false",
# }

# response = requests.get(url, params=params)
# # Fetch data from the API
# data = response.json()

# # Create DataFrame directly from the list of dictionaries
# df = pd.DataFrame(data)

# print("First 5 rows of the DataFrame:")
# print(df.head())  # First 5 records
# print(df.keys())  # Column names

# print("\nDataFrame info:")


class CryptoPriceTracker:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_top_cryptocurrencies(self, limit=10):
        try:
            url = f"{self.base_url}/coins/markets"
            params = {
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 10,
                "page": 1,
                "sparkline": "false",
            }
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()

            print("CryptoPriceTracker", data["data"])
            return data["data"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            return None


# my_script.py
def main():
    # Initialize tracker
    tracker = CryptoPriceTracker()
    # Get top cryptocurrencies
    print("Fetching top cryptocurrencies...")
    top_cryptos = tracker.get_top_cryptocurrencies(limit=5)
    print("top_cryptos", top_cryptos)


if __name__ == "__main__":
    main()  # This only runs when script is executed directly
