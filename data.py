import requests

response = requests.get(
    url="https://countriesnow.space/api/v0.1/countries/capital",
    timeout=10
)
response.raise_for_status()

data = response.json()

raw_country_data = data["data"]

clean_country_data = []

for country in raw_country_data:
    country_name = country["name"]
    capital = country["capital"]

    if capital:
        clean_country_data.append({
            "country": country_name,
            "capital": capital
        })
