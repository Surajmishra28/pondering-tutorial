import streamlit as st
from firebase_admin import firestore

def app():
    # Initialize Firestore database if not already done
    if 'db' not in st.session_state:
        st.session_state.db = firestore.client()  # Initialize Firestore client

    # Initialize username in session state
    if 'username' not in st.session_state:
        st.session_state.username = ''  # Default value for username

    # Placeholder message based on login status
    ph = 'Login to be able to post!!' if st.session_state.username == '' else 'Post your thought'
    
    # Text area for new posts
    post = st.text_area(label=':orange[+ New post]', placeholder=ph, height=None, max_chars=500)

    # Button to post the new content
    if st.button('Post', use_container_width=True):
        if post:
            # Fetch existing post information
            info = st.session_state.db.collection('Posts').document(st.session_state.username).get()

            # Prepare post data
            data = {"Content": [post], 'Username': st.session_state.username}
            if info.exists:
                # Update existing document
                st.session_state.db.collection('Posts').document(st.session_state.username).update({
                    u'Content': firestore.ArrayUnion([post])
                })
            else:
                # Create new document
                st.session_state.db.collection('Posts').document(st.session_state.username).set(data)

            st.success('Post uploaded!!')

    # Display latest posts
    st.header(':violet[Latest Posts]')
    # Fetch all documents from 'Posts'
    posts_ref = st.session_state.db.collection('Posts').stream()
    for doc in posts_ref:
        d = doc.to_dict()
        try:
            st.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']), 
                         value=d['Content'][-1], height=20, disabled=True)
        except Exception as e:
            st.error(f"Error displaying post: {e}")

# Run the app
if __name__ == "__main__":
    app()
