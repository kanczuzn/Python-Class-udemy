travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visits,cities):
    travel_log.append({"country":country,"visits":visits,"cities":cities})
    # Find the entry that's Russia.
    country_loc = next((i for i, item in enumerate(travel_log) if item["country"] == "Russia"), None)
    # Change Russia's visits to 4.
    travel_log[country_loc]["visits"] = 4



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
