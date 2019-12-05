from flask import Flask
import requests
import json
app = Flask(__name__)


@app.route('/')
def home():
    return "BESTCLOUDFORME!"

@app.route('/hello')
def hello():
    try:
        resp = requests.get("http://hello/")
        if(resp.status_code == 200):
            print("Status Code: {status} Body: {text}".format(
                status = resp.status_code,
                text = resp.text
            ))
            return json.dumps(json.loads(resp.text), indent=4)
        print("Status Code: {status} Body: Error".format(
            status = resp.status_code
        ))
    except:
        print("Hello service is unavailable")
        return "Service is Unavailable"

@app.route('/bcfm')
def bcfm():
    try:
        resp = requests.get("http://bcfm/")
        if(resp.status_code == 200):
            print("Status Code: {status} Body: {text}".format(
                status = resp.status_code,
                text = resp.text
            ))
            return json.dumps(json.loads(resp.text), indent=4)
        print("Status Code: {status} Body: Error".format(
            status = resp.status_code
        ))
    except:
        print("Hello service is unavailable")
        return "Service is Unavailable"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)