from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deploying"

PRODUCTS = [
    {
        "id": 1, "name": "Personalised Gift Box", "category": "Gift Box",
        "price": 799, "old_price": 999,
        "image": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 2, "name": "Elegant Jewellery Gift", "category": "Accessories",
        "price": 599, "old_price": 749,
        "image": "https://images.unsplash.com/photo-1617038220319-276d3cfab638?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 3, "name": "Birthday Surprise Box", "category": "Birthday",
        "price": 899, "old_price": 1099,
        "image": "https://images.unsplash.com/photo-1512909006721-3d6018887383?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 4, "name": "Soft Teddy Bear", "category": "Soft Toys",
        "price": 499, "old_price": 649,
        "image": "https://images.unsplash.com/photo-1559454403-b8fb88521f11?auto=format&fit=crop&w=900&q=85"
    },
]

@app.context_processor
def inject_cart_count():
    cart = session.get("cart", {})
    return {"cart_count": sum(cart.values())}

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/add-to-cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if not any(p["id"] == product_id for p in PRODUCTS):
        flash("That product could not be found.", "error")
        return redirect(url_for("home"))
    cart = session.get("cart", {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    flash("Product added to your demo cart.", "success")
    return redirect(url_for("home") + "#products")

@app.route("/cart")
def cart():
    cart_data = session.get("cart", {})
    items = []
    total = 0
    for product in PRODUCTS:
        quantity = cart_data.get(str(product["id"]), 0)
        if quantity:
            line_total = product["price"] * quantity
            total += line_total
            items.append({**product, "quantity": quantity, "line_total": line_total})
    return render_template("cart.html", items=items, total=total)

@app.route("/remove-from-cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart_data = session.get("cart", {})
    if not cart_data:
        flash("Your cart is empty. Add a product first.", "error")
        return redirect(url_for("home"))
    items = []
    total = 0
    for product in PRODUCTS:
        quantity = cart_data.get(str(product["id"]), 0)
        if quantity:
            total += product["price"] * quantity
            items.append({**product, "quantity": quantity})
    if request.method == "POST":
        customer_name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        payment_method = request.form.get("payment_method", "Manual UPI")
        if not customer_name or not phone or not address:
            flash("Please fill in all delivery details.", "error")
        else:
            # Demo only: orders are not saved to a database yet.
            session["last_order"] = {
                "name": customer_name, "phone": phone, "address": address,
                "payment_method": payment_method, "total": total
            }
            session["cart"] = {}
            return redirect(url_for("order_success"))
    return render_template("checkout.html", items=items, total=total)

@app.route("/order-success")
def order_success():
    order = session.get("last_order")
    if not order:
        return redirect(url_for("home"))
    return render_template("success.html", order=order)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)