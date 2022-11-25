from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def FUN_404(error):
    return render_template("page_404.html"), 404


@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/about/")
def FUN_public():
    return render_template("about_page.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
