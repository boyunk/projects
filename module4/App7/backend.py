import requests

API_key="d2fbdd626f00504374736ac44b6fd28f"


def get_data(place, forecast_days, type=None):
    url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Seoul", forecast_days = 3))


# example https://pro.openweathermap.org/data/2.5/forecast/climate?q=Seoul&appid=d2fbdd626f00504374736ac44b6fd28f
# my api key does not work for now
