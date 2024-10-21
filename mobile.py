from streamlit_javascript import st_javascript
from user_agents import parse
import streamlit as st

# Get the user agent string from the browser
ua_string = st_javascript("""window.navigator.userAgent;""")
st.text(f"User Agent String: {ua_string}")

try:
    if ua_string:
        user_agent = parse(ua_string)
        st.session_state.is_session_pc = user_agent.is_pc

        # Check for Facebook embedded browser indicators
        is_facebook_embedded = "FBAN" in ua_string or "FBAV" in ua_string

        st.info(f"Is session on a PC? {st.session_state.is_session_pc}")
        st.info(f"Is the browser embedded in Facebook? {is_facebook_embedded}")

        # Check conditions and create a link for Google Chrome download
        if not st.session_state.is_session_pc and is_facebook_embedded:
            st.warning("You are using a Facebook embedded browser on a mobile device. For a better experience, consider using Google Chrome.")
            st.markdown("[Download Google Chrome](https://test-mobile.streamlit.app/)", unsafe_allow_html=True)
    else:
       pass
except Exception as e:
    pass
