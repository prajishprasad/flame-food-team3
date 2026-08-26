from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions (to store cart data)

# Dummy data: cafes and menus
cafes = {
    "Cafe One": {"Coffee": 20, "Sandwich": 50, "Muffin": 30},
    "Cafe Two": {"Tea": 15, "Burger": 70, "Fries": 40},
    "Cafe Three": {"Pizza": 100, "Pasta": 80, "Salad": 50},
    "Cafe Four": {"Idli":20, "Dosa":50, "Filter Coffee":20}
}

@app.route("/")
def home():
    """Show list of cafes"""
    return render_template("index.html", cafes=cafes)

@app.route("/cafe/<name>")
def show_cafe(name):
    """Show menu of a cafe"""
    menu = cafes.get(name, [])
    return render_template("cafe.html", cafe=name, menu=menu)

@app.route("/add_to_cart/<cafe>/<item>")
def add_to_cart(cafe, item):
    """Add an item to the cart (stored in session)"""
    cart = session.get("cart", [])
    cart.append({"cafe": cafe, "item": item})
    session["cart"] = cart
    return redirect(url_for("view_cart"))

@app.route("/cart")
def view_cart():
    """View items in cart"""
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)

@app.route("/checkout")
def checkout():
    """Clear the cart (no real payment)"""
    session["cart"] = []
    return "Thanks for ordering! Your cart is now empty."
    
if __name__ == "__main__":
    app.run(debug=True)
