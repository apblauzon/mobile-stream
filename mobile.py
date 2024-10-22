from streamlit_javascript import st_javascript
from user_agents import parse
import streamlit as st
import pyperclip

# Get the user agent string from the browser
ua_string = st_javascript("""window.navigator.userAgent;""")
a='https://test-mobile.streamlit.app/'
st.set_page_config(page_title="DatViz Ai", page_icon="logo.svg", layout="wide")

try:
    if ua_string:
        user_agent = parse(ua_string)
        st.session_state.is_session_pc = user_agent.is_pc

        is_facebook_embedded = "FBAN" in ua_string or "FBAV" in ua_string

        if not st.session_state.is_session_pc and is_facebook_embedded:
            st.markdown(
                """
                <div style='text-align: center; background-color: #fff; padding: 10px; border-radius: 5px;'>
                    <p style='margin: 0; color: black;'>copy the app link and paste it as your web address of your browser.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            st.write("")
            if st.button('Copy Link', type='primary',use_container_width=True):
                pyperclip.copy(a)
                st.success('Link Copied Successfully!')
        else:
            st.write("You are in broswer")
    else:
        pass
except Exception as e:
    pass
