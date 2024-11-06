import streamlit as st
from streamlit_ace import st_ace
from io import StringIO
from contextlib import redirect_stdout

st.set_page_config(page_title='Python Compiler', layout='wide')

st.title('Python Compiler')

col = st.columns(2)

with col[1]:
    st.subheader('Code Output')

with col[0]:
    st.subheader('Code Input')
    cc = "print('Enjoy Python')"
    cc = st_ace(cc, language='python', min_lines=8)

    if st.button('Run Code', type='primary'):
        with col[1]:
            try:
                exec(cc)
                f = StringIO()
                with redirect_stdout(f):
                    exec(cc)
                s = f.getvalue()
            # print('s', s)
                st.code(s)
            except Exception as e:
                st.error(e)