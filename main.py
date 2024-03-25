import streamlit as st

def render_page(md=None):
    with open(md, "r") as f:
        reader = f.read()
    st.markdown(reader)

pages = {
    "Asian" : render_page,
    "Bread" : render_page,
    "Mini Waffle Maker" : render_page,
    "Instant Pot" : render_page,
    "Slow Cook" : render_page,
    "Stove Top" : render_page,
    "Sweets" : render_page,
}

md_loader = {
    "Asian" : "assets/texts/eastasian.md",
    "Bread" : "assets/texts/bread.md",
    "Mini Waffle Maker" : "assets/texts/miniwafflemaker.md",
    "Instant Pot" : "assets/texts/instantpot.md",
    "Slow Cook" : "assets/texts/slowcook.md",
    "Stove Top" : "assets/texts/stovetop.md",
    "Sweets" : "assets/texts/sweets.md",
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))
md = md_loader[selected_page]
pages[selected_page](md=md)

st.write("Bon Appetit!!!")