from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def index(): return("heloooo")

if __name__ == "main":
    app.run()


