import streamlit as st 
import firebase_admin 

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('ponderingg-d1e72-5ce8969305a7.json')
firebase_admin.initialize_app(cred)
def app():
    st.title('Welcome to :violet[Pondering]')
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''


    def f():
        try:
            user =auth.get_user_by_email(email)
            #print(user.uid)
            st.write('Login Successful')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True

        except:
            st.warning('Login Failed')
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
        
    if not st.session_state['signedout']:
        choice = st.selectbox('Login/signup',['Login','sign Up'])

        if choice=='Login':
            email=st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            st.button('Login', on_click=f)


        else:
            email=st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            username = st.text_input('Enter your unique username')

            if st.button('Create my account'):
               user = auth.create_user(email = email,password =password, uid=username)

               st.success('Account creadted successfully!')
               st.markdown('Please Login using your email and password')
               st.balloons()
    if st.session_state.signout:
         st.text('Name ' +st.session_state.username)
         st.text('Email id: '+st.session_state.useremail)
         st.button('Sign out', on_click=t)
   

          
