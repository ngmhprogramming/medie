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


@app.route("/setup", methods=["GET", "POST"])
def setup():
    username = get_username()
    if not username:
        return redirect(url_for("login"))
    
    if request.method == "GET":
        #return render_template("setup.html",myname = session["name"])
        return render_template("details.html")
    else:
        session["date"] = request.form["date"]
        return redirect(url_for("loading",functiontocall = "medicalsummary"))

@app.route("/loading/<functiontocall>", methods=["GET", "POST"])
def loading(functiontocall):
    return render_template("loader.html",nextfunc = functiontocall)


@app.route("/medicalsummary")
def medicalsummary():
    return render_template("medicalsummary.html",myname = session["name"],mydate = session["date"])

@app.route("/budget", methods=["GET", "POST"])
def budget():
    if request.method == "GET":
        return render_template("budget.html")
    else:
        session["budget"] = request.form["budget"]
        return redirect(url_for("singpass_and_dbs"))

@app.route("/pullexternaldata")
def singpass_and_dbs():
    return render_template("externaldata.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    username = get_username()
    if username:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("login.html")
    else:
        session["username"] = username = request.form["username"]
        password = request.form["password"]
        
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

@app.route("/details", methods=["GET", "POST"])
def details():
    if request.method == "GET":
        return render_template("details.html")
    else:
        return redirect(url_for("bills"))

@app.route("/bills", methods=["GET", "POST"])
def bills():
    if request.method == "GET":
        return render_template("bills.html")
    else:
        return redirect(url_for("bills"))

if __name__ == "__main__":
    app.run(debug=True)
