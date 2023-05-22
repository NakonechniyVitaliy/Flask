from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

user_vitalii = {
    "name": "Vitalii",
    "second_name": "Nakonechniy",
    "age": 20
}

@app.route("/")
def main():
    return render_template("index.html")



@app.route("/profile")
def v():
    return render_template("profile.html", user_vitalii=user_vitalii)



app.run()