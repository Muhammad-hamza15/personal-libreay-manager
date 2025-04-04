import streamlit as st

# Load or initialize library
if "library" not in st.session_state:
    st.session_state.library = []

# Page title
st.title("📚 Personal Library Manager")

# Book input form
title = st.text_input("Book Title")
author = st.text_input("Author")
status = st.selectbox("Status", ["Unread", "Reading", "Read"])
if st.button("Add Book"):
    if title and author:
        st.session_state.library.append({"Title": title, "Author": author, "Status": status})
        st.success(f'Added "{title}" by {author}')
    else:
        st.warning("Please enter both title and author.")

# Display library
if st.session_state.library:
    for i, book in enumerate(st.session_state.library):
        st.write(f"**{book['Title']}** by {book['Author']} ({book['Status']})")
        if st.button(f"Remove {book['Title']}", key=f"remove_{i}"):
            st.session_state.library.pop(i)
            st.experimental_rerun()
else:
    st.info("Your library is empty. Add some books!")

