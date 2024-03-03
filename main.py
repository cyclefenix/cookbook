import streamlit as st

def render_page(md=None):
    with open(md, "r") as f:
        reader = f.read()
    st.markdown(reader)

pages = {
    "Bread" : render_page,
    "Breakfast": render_page,
    "Instant Pot" : render_page,
    "Pasta": render_page,
    "Slow Cook" : render_page,
    "Sweets" : render_page,
}

md_loader = {
    "Bread" : "assets/texts/bread.md",
    "Breakfast": "assets/texts/breakfast.md",
    "Instant Pot" : "assets/texts/instantpot.md",
    "Pasta" : "assets/texts/pasta.md",
    "Slow Cook" : "assets/texts/slowcook.md",
    "Sweets" : "assets/texts/sweets.md",
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))
md = md_loader[selected_page]
pages[selected_page](md=md)

st.write("Bon Appetit!!")