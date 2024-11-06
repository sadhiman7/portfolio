import streamlit as st
import os

about_page = st.Page(
    page = 'views/about_me.py',
    title = 'About Me',
    default=True
)

projects = [ st.Page(
    page = f'views/projects/{i}',
    title = ' '.join([x.capitalize() for x in i[:-3].split('_')])
) for i in os.listdir('views/projects')
]

pg = st.navigation(
    pages={
        'Info': [about_page],
        'Projects': projects
        }
    )

pg.run()