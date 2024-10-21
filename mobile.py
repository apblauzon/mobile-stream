from streamlit_javascript import st_javascript
from user_agents import parse
import streamlit as st

# Get the user agent string from the browser
ua_string = st_javascript("""window.navigator.userAgent;""")


try:
    if ua_string:
        user_agent = parse(ua_string)
        st.session_state.is_session_pc = user_agent.is_pc

        is_facebook_embedded = "FBAN" in ua_string or "FBAV" in ua_string

        if not st.session_state.is_session_pc and is_facebook_embedded:
            st.markdown(
                """
                <div style='text-align: center; background-color: #fff; border: 2px solid #ffcc80; padding: 10px; border-radius: 5px;'>
                    <div style='text-align: center;'>
                        <h5 style='margin: 0; color:#5381a3;'>For Optimal Experience:</h5>
                    </div>
                    <p style='margin: 0; color: black;'>copy the app link and paste it as your web address of your browser.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.write("You are in broswer")
    else:
        pass
except Exception as e:
    pass
