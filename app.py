from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/nozarik")
def nozarik():
  return render_template("nozarik.html") 

if __name__ == "__main__":
  print("dentro id")
  app.run(host = "0.0.0.0",debug =True )