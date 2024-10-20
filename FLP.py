import streamlit as st

#Header
st.header('French Language Self-Assessment')

#Data Privacy Section
privacy_text = 'This tool allows you to self-assess your language proficiency. The results will help us refine the teaching curriculum and enhance our understanding of how best to support student learning. While the data will be anonymized, you have the option to withhold your data if you prefer. Please select one of the following options to indicate your data privacy preference:'
st.markdown(f"<div style='text-align: justify;'>{privacy_text}</div>", unsafe_allow_html=True)
st.radio('',['I consent to sharing my data','I do not consent to sharing my data'])
st.divider()

#French speaking environment
Speaking_environment = 'Do you live in a French speaking environment?'
st.markdown(f"<div style='text-align: justify;'>{Speaking_environment}</div>", unsafe_allow_html=True)
st.radio('',['Yes','No'])
st.divider()

#Previous experience: Semesters and Quarters
semesters = 'How many semesters have you completed?'
st.markdown(f"<div style='text-align: justify;'>{semesters}</div>", unsafe_allow_html=True)
st.text_input('')
quarters = 'How many quarters have you completed?'
st.markdown(f"<div style='text-align: justify;'>{quarters}</div>", unsafe_allow_html=True)
st.text_input(' ')
st.divider()

#Current perception of student on their profeciency level
student_perception = 'Before you begin the questionnaire, please take a moment to reflect on your language skills. Rate your level of proficiency for each of the following skills: reading, writing, speaking, and listening.'
st.markdown(f"<div style='text-align: justify;'>{student_perception}</div>", unsafe_allow_html=True)
st.write('')
st.select_slider('Reading',['Beginner','Intermediate','Advanced','Superior'])
st.write('')
st.select_slider('Listening',['Beginner','Intermediate','Advanced','Superior'])
st.write('')
st.select_slider('Writing',['Beginner','Intermediate','Advanced','Superior'])
st.write('')
st.select_slider('Speaking',['Beginner','Intermediate','Advanced','Superior'])
st.divider()

#Choosing between American/European Frameworks
frameworks = 'Choose between one of the following frameworks.'
st.markdown(f"<div style='text-align: justify;'>{frameworks}</div>", unsafe_allow_html=True)
selected_framework = st.radio('',['ACTFUL (American Council of the Teaching of Foreign Language)','CEFRL (Common European Framework of Reference for Languages)'])
st.divider()


#Proficiency levels and their descriptions (Reading)
actful_levels = {
    'Novice_Low_R': 'I can identify memorized or familiar words when they are supported by gestures or visuals in informational texts.',
    'Novice_Mid_R': 'I can identify some basic facts from memorized words and phrases when they are supported by gestures or visuals in informational texts.',
    'Novice_High_R': 'I can identify some basic facts from memorized words and phrases when they are supported by gestures or visuals in informational texts.',
    'Intermediate_Low_R': 'I can identify the topic and related information from simple sentences in short informational texts.',
    'Intermediate_Mid_R': 'I can understand the main idea and key information in short straightforward informational texts.',
    'Intermediate_High_R': 'I can usually follow the main message in various time frames in straightforward, and sometimes descriptive, paragraph-length informational texts.',
    'Advanced_Low_R': 'I can identify the underlying message and some supporting details across major time frames in descriptive informational texts.',
    'Advanced_Mid_R': 'I can understand the underlying message and most supporting details across major time frames in descriptive informational texts.',
    'Advanced_High_R': 'I can follow the flow of ideas and infer meaning from complex language on unfamiliar, abstract topics within informational texts.',
    'Superior_R': 'I can read with ease virtually all forms of the written language, including abstract, structurally or linguistically complex texts such as manuals, specialised articles and literary works.'
}

#checkboxes with unique keys (Reading)
def actful_questions():
    st.write("ACTFUL Reading Proficiency Questions")
    selected_levels = []
    for level, description in actful_levels.items():
        if st.checkbox(description, key=level):  
            selected_levels.append(level)
    return selected_levels

# Show questions based on the framework selected (Reading)
if selected_framework == 'ACTFUL (American Council of the Teaching of Foreign Language)':
    selected_levels = actful_questions()
st.divider()


#Proficiency levels and their descriptions (Listening)
actful_levels = {
    'Novice_Low_L': 'I can understand memorized or familiar words when they are supported by gestures or visuals in conversations.',
    'Novice_Mid_L': 'I can understand memorized or familiar words when they are supported by gestures or visuals in conversations.',
    'Novice_High_L': 'I can understand familiar questions and statements from simple sentences in conversations.',
    'Intermediate_Low_L': 'I can identify the main idea in short conversations.',
    'Intermediate_Mid_L': 'I can identify the main idea and key information in short straightforward conversations.',
    'Intermediate_High_L': 'I can usually understand the main idea and flow of events expressed in various time frames in conversations and discussions.',
    'Advanced_Low_L': 'I can understand the main message and some supporting details across major time frames in conversations and discussions.',
    'Advanced_Mid_L': 'I can understand the main message and most supporting details across major time frames in conversations and discussions.',
    'Advanced_High_L': 'I can follow the flow of ideas and some nuances from different viewpoints in conversations and discussions.',
    'Superior_L': 'I can follow abstract, complex and unfamiliar topics in extended conversations and discussions involving multiple speakers.'
}

#checkboxes with unique keys (Listening)
def actful_questions():
    st.write("ACTFUL Listening Proficiency Questions")
    selected_levels = []
    for level, description in actful_levels.items():
        if st.checkbox(description, key=level):  
            selected_levels.append(level)
    return selected_levels

# Show questions based on the framework selected (Listening)
if selected_framework == 'ACTFUL (American Council of the Teaching of Foreign Language)':
    selected_levels = actful_questions()
st.divider()


#Proficiency levels and their descriptions (Writing)
actful_levels = {
    'Novice_Low_W': 'I can introduce myself using practiced or memorized words and phrases, with the help of gestures or visuals.',
    'Novice_Mid_W': 'I can present information about myself, my interests and my activities using a mixture of practiced or memorized words, phrases and simple sentences.',
    'Novice_High_W': 'I can present personal information about my life and activities, using simple sentences most of the time.',
    'Intermediate_Low_W': 'I can express my preferences on familiar and everyday topics of interest and explain why I feel that way, using simple sentences.',
    'Intermediate_Mid_W': 'I can state my viewpoint about familiar topics and give some reasons to support it, using sentences and series of connected sentences.',
    'Intermediate_High_W': 'I can state my viewpoint on familiar or researched topics and provide reasons to support it, using a few short paragraphs, often across various time frames.',
    'Advanced_Low_W': 'I can deliver presentations on some concrete academic, social and professional topics of interest, using paragraphs across major time frames.',
    'Advanced_Mid_W': 'I can deliver detailed presentations and elaborate on a variety of concrete academic, social and professional topics of interest, using organized paragraphs across major time frames.',
    'Advanced_High_W': 'I can deliver cohesive presentations on a variety of complex concrete topics related to community interests and some specialized fields, and often deal with related issues hypothetically.',
    'Superior_W': 'I can deliver extended presentations on abstract or hypothetical issues and ideas ranging from broad general interests to my areas of specialized expertise, with precision of expression and to a wide variety of audiences, using spoken, written, or signed language.'
}

#checkboxes with unique keys (Writing)
def actful_questions():
    st.write("ACTFUL Writing Proficiency Questions")
    selected_levels = []
    for level, description in actful_levels.items():
        if st.checkbox(description, key=level):  
            selected_levels.append(level)
    return selected_levels

# Show questions based on the framework selected (Writing)
if selected_framework == 'ACTFUL (American Council of the Teaching of Foreign Language)':
    selected_levels = actful_questions()
st.divider()


#Proficiency levels and their descriptions (Speaking)
actful_levels = {
    'Novice_Low_S': 'I can provide information by answering a few simple questions on very familiar topics, using practiced or memorized words and phrases, with the help of gestures or visuals.',
    'Novice_Mid_S': 'I can request and provide information by asking and answering a few simple questions on very familiar and everyday topics, using a mixture of practiced or memorized words, phrases, and simple sentences.',
    'Novice_High_S': 'I can request and provide information by asking and answering practiced and some original questions on familiar and everyday topics, using simple sentences most of the time.',
    'Intermediate_Low_S': 'I can express my preferences on familiar and everyday topics of interest and explain why I feel that way, using simple sentences.',
    'Intermediate_Mid_S': 'I can request and provide information in conversations on familiar topics by creating simple sentences and asking appropriate follow-up questions.',
    'Intermediate_High_S': 'I can exchange information in conversations on familiar topics and some researched topics, creating sentences and series of sentences and asking a variety of follow-up questions.',
    'Advanced_Low_S': 'I can deliver presentations on some concrete academic, social and professional topics of interest, using paragraphs across major time frames.',
    'Advanced_Mid_S': 'I can maintain discussions on a wide variety of familiar and unfamiliar concrete topics of personal and general interest, and sometimes academic, social or professional topics, by using probing questions and providing detailed responses across major time frames.',
    'Advanced_High_S': 'I can discuss and sometimes debate a variety of complex concrete and some abstract academic, social and professional topics and often deal with related issues hypothetically, using precise questions and explanations.',
    'Superior_S': 'I can discuss and debate a wide variety of complex issues and abstract ideas using precise, sophisticated, and academic language.'
}

#checkboxes with unique keys (Speaking)
def actful_questions():
    st.write("ACTFUL Speaking Proficiency Questions")
    selected_levels = []
    for level, description in actful_levels.items():
        if st.checkbox(description, key=level):  
            selected_levels.append(level)
    return selected_levels

# Show questions based on the framework selected (Speaking)
if selected_framework == 'ACTFUL (American Council of the Teaching of Foreign Language)':
    selected_levels = actful_questions()
st.divider()


