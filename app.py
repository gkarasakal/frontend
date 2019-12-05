from flask import Flask
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello():
    return "BESTCLOUDFORME!"

@app.route('/hello')
def hello():
    try:
        resp = requests.get("http://hello/")
        if(resp.status_code == 200):
            print(f"Status Code: {resp.status_code} Body: {resp.text}")
            return json.dumps(json.loads(resp.text), indent=4)
        print(f"Status Code: {resp.status_code} Body: Error")
    except:
        print("Hello service is unavailable")
        return "Service is Unavailable"

@app.route('/bcfm')
def bcfm():
    try:
        resp = requests.get("http://bcfm/")
        if(resp.status_code == 200):
            print(f"Status Code: {resp.status_code} Body: {resp.text}")
            return json.dumps(json.loads(resp.text), indent=4)
        print(f"Status Code: {resp.status_code} Body: Error")
    except:
        print("Hello service is unavailable")
        return "Service is Unavailable"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)