from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p> hello world </p>"

if __name__ == "__main__":
  print("dentro id")
  app.run(host = "0.0.0.0",debug =True )