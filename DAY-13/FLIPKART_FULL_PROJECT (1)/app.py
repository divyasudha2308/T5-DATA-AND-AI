from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------- CONFIG ----------
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

DB = "ecommerce.db"

# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect(DB)

def init_db():
    con = get_db()
    c = con.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        image TEXT
    )
    """)

    con.commit()
    con.close()

def seed_users():
    con = get_db()
    c = con.cursor()
    try:
        c.execute("INSERT INTO users VALUES (NULL,'admin','admin123','admin')")
        c.execute("INSERT INTO users VALUES (NULL,'user','user123','user')")
    except:
        pass
    con.commit()
    con.close()

init_db()
seed_users()

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("home.html")

# ---------- LOGIN ----------
@app.route("/login/<role>", methods=["GET", "POST"])
def login(role):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        con = get_db()
        c = con.cursor()
        c.execute(
            "SELECT * FROM users WHERE username=? AND password=? AND role=?",
            (username, password, role)
        )
        user = c.fetchone()
        con.close()

        if user:
            session["user"] = username
            session["role"] = role

            if role == "admin":
                return redirect("/admin")
            else:
                return redirect("/products")
        else:
            flash("Invalid login")

    return render_template("login.html", role=role)

# ---------- ADMIN DASHBOARD ----------
@app.route("/admin")
def admin():
    if session.get("role") != "admin":
        return redirect("/")

    con = get_db()
    c = con.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    con.close()

    return render_template("admin_dashboard.html", products=products)

# ---------- ADD PRODUCT ----------
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if session.get("role") != "admin":
        return redirect("/")

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        image = request.files.get("image")

        filename = ""
        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        con = get_db()
        c = con.cursor()
        c.execute(
            "INSERT INTO products (name, price, image) VALUES (?,?,?)",
            (name, price, filename)
        )
        con.commit()
        con.close()

        flash("Product added successfully")
        return redirect("/admin")

    return render_template("add_product.html")

# ---------- DELETE PRODUCT ----------
@app.route("/delete_product/<int:id>")
def delete_product(id):
    if session.get("role") != "admin":
        return redirect("/")

    con = get_db()
    c = con.cursor()
    c.execute("DELETE FROM products WHERE id=?", (id,))
    con.commit()
    con.close()

    flash("Product deleted")
    return redirect("/admin")

# ---------- PRODUCTS ----------
@app.route("/products")
def products():
    con = get_db()
    c = con.cursor()
    c.execute("SELECT * FROM products")
    items = c.fetchall()
    con.close()
    return render_template("products.html", items=items)

# ---------- CART ----------
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True
    flash("Product added to cart")
    return redirect("/products")


@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = []

    ids = session["cart"]
    products = []

    if len(ids) > 0:
        placeholders = ",".join("?" * len(ids))
        con = get_db()
        c = con.cursor()
        c.execute(f"SELECT * FROM products WHERE id IN ({placeholders})", ids)
        products = c.fetchall()
        con.close()

    return render_template("cart.html", products=products)


@app.route("/remove_from_cart/<int:id>")
def remove_from_cart(id):
    session["cart"].remove(id)
    session.modified = True
    return redirect("/cart")

# ---------- CHECKOUT ----------
@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("checkout.html")


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
