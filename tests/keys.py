
"""
Don't have an active AerisWeather API client account?
Accessing the API data requires an active AerisWeather API subscription, and registration of your application or
namespace. You can sign up for a free developer account at the https://www.aerisweather.com/signup/ to get your
client ID and secret.
"""

import os

app_id = "com.aerisweather.pythonsdkdemo"

client_id = os.environ["AERIS_CLIENT_ID"]
client_secret = os.environ["AERIS_CLIENT_SECRET"]
