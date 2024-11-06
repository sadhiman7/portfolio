import streamlit as st

about_page = st.Page(
    page = 'views/about_me.py',
    title = 'About Me',
    default=True
)

project_page = st.Page(
    page = 'views/projects.py',
    title = 'Projects'
)

pg = st.navigation(
    pages={
        'Info': [about_page],
        'Projects': [project_page]
        }
    )

pg.run()