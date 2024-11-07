import streamlit as st
from streamlit_option_menu import option_menu

@st.dialog('Contact Me') 
def contact_form():
    st.write('Work in Progress!')

# st.set_page_config(page_title = "Sadhiman Das",page_icon="🚀")

c1, c2 = st.columns(2, gap='small', vertical_alignment='center')

with c1:
    st.image('pfp.png', width=250)
with c2:
    st.title('Sadhiman Das')
    st.markdown('##### Student | Data Scientist')
    if st.button("Contact Me"):
        contact_form()
# st.divider()

# st.divider()

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About Me', 'Work', 'Education', 'Certifications'],
        icons=['person', 'briefcase', 'book', 'files'],
        orientation='horizontal'
    )

if selected == 'About Me':
    st.subheader('About Me')
    st.markdown('''
    - 👨‍🎓 As a Business Analytics student at SCMHRD with a B.Tech in Computer Engineering from NMIMS Mumbai, I have 35 months of experience as a Senior Machine Learning Engineer at Quantiphi Analytics. 
    - 🚀 My expertise includes developing advanced solutions using Computer Vision and NLP in the BFSI domain, fine-tuning and deploying Generative AI-based solutions, and managing machine learning projects. 
    - 💡 I am passionate about leveraging AI to drive innovation and solve complex business challenges. 
    ''')
    st.divider()
    st.markdown('![Leetcode Stats](https://leetcard.jacoblin.cool/sadhiman7?theme=nord&ext=activity)', help='hello')

if selected == 'Work':

    st.subheader('Work Experience')

    st.markdown('##### Quantiphi Analytics (2021-2024)')

    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('''
    Senior Machine Learning Engineer
                    
    Jan 2024 - Jul 2024
    ''')
    with col2:
        st.markdown('''
    - Fine-tuned Generative AI models for specific business use cases.
    - Successfully deployed machine learning models using GCP Kubernetes, Flask, and REST API.
    - Implemented scalable AI solutions to handle large data volumes efficiently.
    - Provided technical leadership and guidance to junior engineers.
    - Monitored and optimized model performance to maintain high accuracy.
    ''')
        
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('''
    Machine Learning Engineer
                    
    Nov 2021 - Dec 2023
    ''')
    with col2:
        st.markdown('''
    - Developed innovative information extraction solutions using Computer Vision and NLP.
    - Created machine learning products to optimize processes in the BFSI sector.
    - Conducted Proof of Concepts (PoCs) for applications like object detection and classification.
    - Collaborated with cross-functional teams to integrate AI solutions into existing systems.
    - Engaged in continuous learning to stay updated with the latest AI advancements.
    ''')
        
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('''
    Intern Machine Learning Engineer
                    
    Jul 2021 - Nov 2021
    ''')
    with col2:
        st.markdown('''
    - Gained hands-on experience with traditional machine learning models and deep learning techniques.
    - Worked on practical projects to apply machine learning algorithms to real-world data.
    - Enhanced understanding of end-to-end machine learning workflows through hands-on projects.
    ''')
        
    st.markdown('##### ONGC Ahmedabad (2019)')
        
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('''
    Intern Data Scientist
                    
    Jun 2019 - Jul 2019
    ''')
    with col2:
        st.markdown('''
    - Worked with large-scale data from oil wells using advanced data preprocessing techniques.
    - Explored machine learning applications for improving maintenance data analysis.
    - Streamlined data extraction, transformation, and loading (ETL) processes.
    ''')

if selected=='Education':
    
    st.title('Work in Progress')
    st.write('Please come back at a later time!')

if selected=='Certifications':
    
    st.title('Work in Progress')
    st.write('Please come back at a later time!')