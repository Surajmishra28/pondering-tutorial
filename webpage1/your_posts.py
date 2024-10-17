import streamlit as st
from firebase_admin import firestore

def app():
    # Initialize Firestore client
    db = firestore.client()

    # Check if username is set in session state
    if 'username' in st.session_state and st.session_state['username']:
        st.title(f'Posts by: {st.session_state["username"]}')

        try:
            # Fetch the user's posts
            user_posts_ref = db.collection('Posts').document(st.session_state['username'])
            result = user_posts_ref.get()

            # Check if the document exists
            if result.exists:
                r = result.to_dict()
                content = r.get('Content', [])

                # Function to delete a post
                def delete_post(index):
                    post_to_delete = content[index]
                    try:
                        user_posts_ref.update({"Content": firestore.ArrayRemove([post_to_delete])})
                        st.warning('Post deleted')
                       # st.experimental_rerun()  # Rerun to refresh the content
                    except Exception as e:
                        st.error(f'Something went wrong: {e}')

                # Display posts and delete buttons
                for index in range(len(content) - 1, -1, -1):
                    st.text_area(label='', value=content[index], height=100, disabled=True)
                    st.button('Delete Post', on_click=delete_post, args=(index,), key=f'delete_{index}')

            else:
                st.write('No posts found.')

        except Exception as e:
            st.error(f'Error fetching posts: {e}')

    else:
        st.text('Please log in first.')

# Run the app
if __name__ == "__main__":
    app()
