from flask import Flask
from flask import request
app = Flask(__name__)

with open("key.secret") as keyFile:
    key = keyFile.read()

@app.route("/",methods = ["POST","GET"])
def action():
    if request.method == "POST":
        if request.headers.get("SecretKey") == key:
            print("[OK - POST] " + request.remote_addr + " has been written to file!")
            with open("ip.address","w") as ipFile:
                ipFile.write(request.remote_addr)
            return "OK",200
        else:
            print("[FAIL - POST] " + request.remote_addr + " sent the wrong key!")
            return "FAIL",401
    else:
        if request.headers.get("SecretKey") == key:
            print("[OK - GET] " + request.remote_addr + " returning file contents!")
            with open("ip.address","r") as ipFile:
                return ipFile.read(),200
        else:
            print("[FAIL - GET] " + request.remote_addr + " sent the wrong key!")
            return "FAIL",401

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=6694)
