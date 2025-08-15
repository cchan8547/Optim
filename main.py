import streamlit as st


page_7251 = st.Page("7251.py", title="7251")
page_8021 = st.Page("8021.py", title="8021")
page_812 = st.Page("812.py", title="812")
# 建立導航
pg = st.navigation([page_7251, page_8021, page_812])

# 執行導航
pg.run()