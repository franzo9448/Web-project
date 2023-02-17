from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/nozarik")
def nozarik():
  return render_template("nozarik.html") 

@app.route("/politica")
def politica():
  return render_template("politics.html") 

@app.route("/floreal")
def floreal():
  return render_template("floreal.html") 

@app.route("/nalowand")
def nalowand():
  return render_template("nalowand.html")

@app.route("/pentola")
def pentola():
  return render_template("pentola.html") 

@app.route("/callisto")
def callisto():
  return render_template("callisto.html") 

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/characters")
def characters():
  return render_template("characters.html")

@app.route("/notes")
def notes():
  return render_template("notes.html")


if __name__ == "__main__":
  print("dentro id")
  app.run(host = "0.0.0.0",debug =True )