from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "change-me-to-a-random-secret-in-prod"

# Demo user store
USERS = {
    "admin": generate_password_hash("Password123")
}

# Demo customer data
CUSTOMERS = [
    {"id": 1, "name": "John", "email": "john@example.com", "phone": "555-0101"},
    {"id": 2, "name": "Hema", "email": "hema@example.com", "phone": "555-0102"},
    {"id": 3, "name": "Carol", "email": "carol@example.com", "phone": "555-0103"}
]

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get("user"):
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapped

# Routes
@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        if username in USERS and check_password_hash(USERS[username], password):
            session["user"] = username
            flash("Logged in successfully.", "info")
            return redirect(url_for("customers"))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("login"))
    return render_template("login.html", title="Login")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

@app.route("/customers")
@login_required
def customers():
    return render_template("customers.html", title="Customers", customers=CUSTOMERS)

@app.route("/api/customers")
@login_required
def api_customers():
    from flask import jsonify
    return jsonify(CUSTOMERS)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)