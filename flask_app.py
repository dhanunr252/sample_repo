from flask import Flask
app = Flask(__name__)
@app.route("/")
def defaultPage():
    return "Hello Guest"

@app.route("/app1")
def app1Page():
    return "Hello Guest - From App1  cimmit changes"
@app.route("/home/<string:name>")
def GuestName(name):
    return {"Hello": name}
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
