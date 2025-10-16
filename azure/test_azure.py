import requests

azure_function_url = "https://504-test-g7cgcpgjddfhh7cc.eastus-01.azurewebsites.net/api/http_trigger1?code=R7s29NkG8PfVRqDpub0h-sjPkaUv_S_hOT5-Io59AEheAzFu11WFbg=="
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