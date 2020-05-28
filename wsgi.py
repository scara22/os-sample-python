from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World from Openshift Online by Gianni Scarafile!"

if __name__ == "__main__":
    application.run()
