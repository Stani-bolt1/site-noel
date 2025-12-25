from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Code d'accès (à personnaliser)
liste_code = ["Joëlle", "Joelle", "joëlle", "joelle"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form.get("code")
        if code in liste_code:
            return redirect(url_for("noel"))
        else:
            return render_template("index.html", erreur=True)
    return render_template("index.html", erreur=False)

@app.route("/noel")
def noel():
    return render_template("noel.html")

if __name__ == "__main__":
    app.run(debug=True)