import requests

azure_function_url = "https://504-test-g7cgcpgjddfhh7cc.eastus-01.azurewebsites.net/api/http_trigger1?code=<YOUR_FUNCTION_KEY>"
# Test Abnormal value (≥6.5)
response = requests.post(azure_function_url, json={"hba1c": 7.2}) 
print(response.status_code)
print(response.json())

# Test Prediabetic value (5.7-6.4)
response = requests.post(azure_function_url, json={"hba1c": 6.1})
print(response.status_code)
print(response.json())

# Test Normal value (<5.7)
response = requests.post(azure_function_url, json={"hba1c": 5.2})
print(response.status_code)
print(response.json())