import streamlit as st

def main_page(md=None):
    st.markdown("# Welcome to Cookbook")
    st.markdown("### By cyclefenix")

def render_page(md=None):
    with open(md, "r") as f:
        reader = f.read()
    st.markdown(reader)

pages = {
    "Main" : main_page,
    "Asian" : render_page,
    "Bread" : render_page,
    "Instant Pot" : render_page,
    "Mini Waffle" : render_page,
    "Slow Cook" : render_page,
    "Stove Top" : render_page,
    "Sweets" : render_page,
}

md_loader = {
    "Main" : None,
    "Asian" : "assets/texts/asian.md",
    "Bread" : "assets/texts/bread.md",
    "Instant Pot" : "assets/texts/instantpot.md",
    "Mini Waffle" : "assets/texts/miniwaffle.md",
    "Slow Cook" : "assets/texts/slowcook.md",
    "Stove Top" : "assets/texts/stovetop.md",
    "Sweets" : "assets/texts/sweets.md",
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))
md = md_loader[selected_page]
pages[selected_page](md=md)

if md is not None:
    st.write("Bon Appetit!!!")