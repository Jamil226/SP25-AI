import streamlit as st

# App Title
st.title("My First App")

# Header
st.header("Main Header")

# Sub-Header
st.subheader("Sub Header")

# Markdown
st.markdown("Installing Streamlit **Text**")
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")

# Caption
st.caption("This is a caption")

# Code Block
st.code("for(i = 0; i<=10; i++)")

# Preformatted Text

st.text("Lorem ipsum dummy text")

# Latex

st.latex("x = x^2")

# Divider
st.divider()

st.text("Lorem ipsum dummy text")
st.divider()
st.text("Lorem ipsum dummy text")


# st.write

st.write("Lorem ipsum dummy text")
