import requests

url = "https://hba1c-test-504-454776307775.us-central1.run.app"

# Test Abnormal value (≥6.5)
response = requests.post(url, json={"hba1c": 7.2}) 
print(response.status_code)
print(response.json())

# Test Normal value (<6.5)
response = requests.post(url, json={"hba1c": 5.4})
print(response.status_code)
print(response.json())
