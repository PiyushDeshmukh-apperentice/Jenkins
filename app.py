import streamlit as st

st.set_page_config(page_title="E-Commerce", page_icon="🛍️", layout="wide")

st.title("🛒 Simple E-Commerce Store")
st.subheader("Welcome to StreamShop — a e-commerce app built with Streamlit")

# Product Catalog
products = {
    "Smartphone": 29999,
    "Laptop": 69999,
    "Headphones": 1999,
    "Smartwatch": 4999,
    "Bluetooth Speaker": 2499
}

st.write("### Available Products")
cols = st.columns(3)
for idx, (product, price) in enumerate(products.items()):
    with cols[idx % 3]:
        st.image("https://via.placeholder.com/150", caption=product)
        st.write(f"💰 Price: ₹{price}")
        if st.button(f"Add {product}", key=product):
            st.session_state["cart"] = st.session_state.get("cart", [])
            st.session_state["cart"].append((product, price))
            st.success(f"{product} added to cart!")

# Shopping Cart
st.write("---")
st.write("### 🧾 Your Cart")
cart = st.session_state.get("cart", [])
if cart:
    total = sum(price for _, price in cart)
    for product, price in cart:
        st.write(f"- {product}: ₹{price}")
    st.write(f"**Total: ₹{total}**")
    if st.button("Checkout"):
        st.success("✅ Order placed successfully!")
        st.session_state["cart"] = []
else:
    st.info("Your cart is empty.")
