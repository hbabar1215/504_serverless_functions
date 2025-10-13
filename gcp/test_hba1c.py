import requests
url = "https://hba1c-test-504-454776307775.us-central1.run.app"

# Test a normal value
## if post
response = requests.post(url, json={"hba1c": 5.4})
## if get
response = requests.get(url, params={"hba1c": 5.4})
print(response.status_code)
print(response.json())
