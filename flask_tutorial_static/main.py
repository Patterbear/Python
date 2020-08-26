from flask import Flask, render_template, url_for
from admin.second import second

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(second, url_prefix="/admin")


@app.route("/")
def test():
    return "<h1>Test</h1?>"


if __name__ == "__main__":
    app.run(debug=True)
