import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, trending, your_posts


st.set_page_config(
    page_title="Pondering",
)

class MultiApp:

    def __init__(self):
        self.apps =[]
    def add_app(self, title, function):
        self.apps.append({"title":title,
        "function": function
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title= 'Pondering',
                options=['about','account','home','trending','your_posts'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","backround-color": 'black'},
            "icon": {"color": "white", "font-size": "23ps"},
            "nav-link":{"color": "white","font-size": "20px", "text-align": "left", "margin":"0px"},
            "nav-ling-selected":{"background-color":"#2ab21"},}
            ) 
        if app== 'home':
                home.app()
        if app== 'account':
                account.app()
        if app== 'about':
                about.app()
        if app== 'trending':
                trending.app()
        if app== 'your_posts':
                your_posts.app()
    run()
            