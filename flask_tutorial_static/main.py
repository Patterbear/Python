from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
