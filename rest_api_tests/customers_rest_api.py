import requests

BASE_URL = "http://127.0.0.1:5001"
LOGIN_URL = f"{BASE_URL}/login"
API_URL = f"{BASE_URL}/api/customers"

# start a session
s = requests.Session()

# login first
login_data = {"username": "admin", "password": "Password123"}
r = s.post(LOGIN_URL, data=login_data)

# now access API
r = s.get(API_URL)
if r.status_code == 200:
    customers = r.json()
    for c in customers:
        print(f"{c['id']} | {c['name']} | {c['email']} | {c['phone']}")
else:
    print("Failed to fetch customers:", r.status_code)