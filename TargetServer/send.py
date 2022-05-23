import time
import requests

delay = 5 * 60
url = "INSERT URL HERE (Flask port is 6694)"
secretKey = "INSERT KEY HERE"

if __name__ == "__main__":
    while True:
        print("Sending request...")
        loopId = 0
        while loopId >= 0:
            loopId = loopId + 1
            response = requests.post(url=url,headers={
                "SecretKey": secretKey
            })
            if response.status_code == 200:
                print("[OK] Entry completed.")
                loopId = -1
            else:
                print("[CODE " + str(response.status_code) + "] Entry failed.")
                if loopId <= 5:
                    print("Resending request...")
                else:
                    loopId = -1
        print("Sleeping... (" + str(delay) + "s)")
        time.sleep(delay)