from streamlit_javascript import st_javascript
from user_agents import parse
import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

st.set_page_config(page_title="DatViz Ai", page_icon="logo.svg", layout="wide")
ua_string = st_javascript("""window.navigator.userAgent;""")
link='https://test-mobile.streamlit.app/'


try:
    if ua_string:
        user_agent = parse(ua_string)
        st.session_state.is_session_pc = user_agent.is_pc

        is_facebook_embedded = "FBAN" in ua_string or "FBAV" in ua_string

        if not st.session_state.is_session_pc and is_facebook_embedded:
            st.image("head_logo.svg", use_column_width=True)
            st.markdown(
                """
                <div style='text-align: center; background-color: #fff; padding: 10px; border-radius: 5px;'>
                    <p style='margin: 0; color: black;'>Copy the app link and paste it as your web address of your browser.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            st.write("")
            col1,col2,col3,col4,col5 = st.columns(3)
            with col3:
                st_copy_to_clipboard("https://test-mobile.streamlit.app/")
    else:
        pass
except Exception as e:
    pass
