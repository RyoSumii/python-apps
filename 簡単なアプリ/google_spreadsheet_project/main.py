import requests
import datetime as dt

# Nutrition & Exercise API
EX_API_ID = "xxxxxxxxx"
EX_API_KEY = "yyyyyyyyy"

EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# change <username> to yours
SHEET_ENDPOINT = "https://api.sheety.co/<username>/workoutTracking/workouts"

# example data
GENDER = "male"  # or "female"
WEIGHT_KG = 65
HEIGHT_CM = 171
AGE = 20

# sheety token
bear_token = "zzzzzzzzzzz"

headers = {
    "x-app-id": EX_API_ID,
    "x-app-key": EX_API_KEY,
    "x-remote-user-id": "0"
}

str_input = str(input("Tell me which exercise you did:"))  
ex_params = {
    "query": str_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXERCISE_END_POINT, json=ex_params, headers=headers)
response.raise_for_status()
exercise_data = response.json()
print(exercise_data)
t = dt.datetime.today()
now_time = t.strftime("%X")
date = t.strftime("%d/%m/%Y")

headers = {
    "Authorization": f"Bearer {bear_token}"
}

# if spreadsheet's name is workout and
body = {
    "workout": {
        "date": date,
        "time": now_time,
        "exercise": exercise_data["exercises"][0]["name"].title(),
        "duration": exercise_data["exercises"][0]["duration_min"],
        "calories": exercise_data["exercises"][0]["nf_calories"],
    }
}

response = requests.post(url=SHEET_ENDPOINT, json=body, headers=headers)
response.raise_for_status()
print(response.text)
