from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__, static_url_path="/static")
app.secret_key = "mereallywannadie69420"

def get_username():
    if "username" in session: return session["username"]
    return False

@app.route("/")
def index():
    username = get_username()
    if not username:
        return redirect(url_for("login"))

    session["name"] = "Mr Lum"
    return redirect(url_for("setup"))
    #return render_template("index.html")


@app.route("/setup")
def setup():
    username = get_username()
    if not username:
        return redirect(url_for("login"))

    return render_template("setup.html",myname = session["name"])


@app.route("/login", methods=["GET", "POST"])
def login():
    username = get_username()
    if username:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        
        session["username"] = "Lum Name"
        return redirect(url_for("index"))

        #if db.login(username, hash(password)):
        #    session["username"] = username
        #    return redirect(url_for("index"))
        #return render_template("login.html", error="Invalid Username or Password")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    username = get_username()
    if username:
        return redirect(url_for("index"))

    if request.method == "GET":
        return redirect(url_for("login"))
    else:
        username = request.form["username"]
        password = request.form["password"]
        password = request.form["confirm"]

        return redirect(url_for("login"))

        #password = hash(password)
        #if db.register(username, pnumber, email, password):
        #    return redirect(url_for("login"))
        #return render_template("signup.html", error="Username taken!")

if __name__ == "__main__":
    app.run(debug=True)
