import requests

secretKey = "INSERT IDENTICAL KEY HERE"
url = "INSERT URL HERE"

print("Collecting data...")
response = requests.get(url=url,headers={
    "SecretKey": secretKey
})
print("[CODE " + str(response.status_code) + "] Content: " + response.content.decode("utf-8"))