import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

#Recording the start time
start_time = time.time()

#Header
st.header('French Language Self-Assessment')


#Data Privacy Section
privacy_text = 'This tool allows you to self-assess your language proficiency. Please complete this assessment in <b>one sitting</b>. If you exit the page, your information will not be saved, and you must restart. The results will help us refine the teaching curriculum and enhance our understanding of how best to support student learning. While the data will be <b>anonymized</b> and <b>only shared with the researcher</b>, you can withhold your data if you prefer. Please select one of the following options to indicate your data privacy preference.'
st.markdown(f"<div style='text-align: justify;'>{privacy_text}</div>", unsafe_allow_html=True)
st.radio('',['I consent to sharing my data','I do not consent to sharing my data'])
st.divider()

#Age
Age = 'What is your age?'
st.markdown(f"<div style='text-align: justify;'>{Age}</div>", unsafe_allow_html=True)
st.number_input('', min_value=0, max_value=120, step=1)
st.divider()

#French speaking environment
Speaking_environment = 'Do you live in a French speaking environment?'
st.markdown(f"<div style='text-align: justify;'>{Speaking_environment}</div>", unsafe_allow_html=True)
st.radio('',['Yes','No'])
st.divider()

#Previous experience: Semesters and Quarters
semesters = 'How many semesters have you completed?'
st.markdown(f"<div style='text-align: justify;'>{semesters}</div>", unsafe_allow_html=True)
st.number_input(' ', min_value=0, max_value=120, step=1)
quarters = 'How many quarters have you completed?'
st.markdown(f"<div style='text-align: justify;'>{quarters}</div>", unsafe_allow_html=True)
st.number_input('  ', min_value=0, max_value=120, step=1)
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
frameworks = 'Choose between one of the following language frameworks. Check the boxes that you are confident you can perform <b>95 percent</b> of the time. Be sure to check the box only if you can <b>consistently</b> achieve this level of proficiency in reading, writing, listening, or speaking. Please read each description carefully and select the checkboxes <b>in order</b>. Ensure that you check each box <b>sequentially</b> (i.e., start with 1, then 2, and so on) before moving to the next.'
st.markdown(f"<div style='text-align: justify;'>{frameworks}</div>", unsafe_allow_html=True)
selected_framework = st.radio('',['ACTFL (American Council of the Teaching of Foreign Language)','CEFRL (Common European Framework of Reference for Languages)'])
st.divider()


# Define proficiency levels for common y-axis labels
proficiency_levels_actfl = {
    'Novice Low': 1,
    'Novice Mid': 2,
    'Novice High': 3,
    'Intermediate Low': 4,
    'Intermediate Mid': 5,
    'Intermediate High': 6,
    'Advanced Low': 7,
    'Advanced Mid': 8,
    'Advanced High': 9,
    'Superior': 10
}


#Proficiency levels and their descriptions (Reading)
actfl_levels_reading = {
    'Novice Low': 'I can identify memorized or familiar words when they are supported by gestures or visuals in informational texts.',
    'Novice Mid': 'I can identify some basic facts from memorized words and phrases when they are supported by gestures or visuals in informational texts.',
    'Novice High': 'I can identify some basic facts from memorized words and phrases when they are supported by gestures or visuals in informational texts.',
    'Intermediate Low': 'I can identify the topic and related information from simple sentences in short informational texts.',
    'Intermediate Mid': 'I can understand the main idea and key information in short straightforward informational texts.',
    'Intermediate High': 'I can usually follow the main message in various time frames in straightforward, and sometimes descriptive, paragraph-length informational texts.',
    'Advanced Low': 'I can identify the underlying message and some supporting details across major time frames in descriptive informational texts.',
    'Advanced Mid': 'I can understand the underlying message and most supporting details across major time frames in descriptive informational texts.',
    'Advanced High': 'I can follow the flow of ideas and infer meaning from complex language on unfamiliar, abstract topics within informational texts.',
    'Superior': 'I can read with ease virtually all forms of the written language, including abstract, structurally or linguistically complex texts such as manuals, specialised articles and literary works.'
}

#Proficiency levels and their descriptions (Listening)
actfl_levels_listening = {
    'Novice Low': 'I can understand memorized or familiar words when they are supported by gestures or visuals in conversations.',
    'Novice Mid': 'I can understand memorized or familiar words when they are supported by gestures or visuals in conversations.',
    'Novice High': 'I can understand familiar questions and statements from simple sentences in conversations.',
    'Intermediate Low': 'I can identify the main idea in short conversations.',
    'Intermediate Mid': 'I can identify the main idea and key information in short straightforward conversations.',
    'Intermediate High': 'I can usually understand the main idea and flow of events expressed in various time frames in conversations and discussions.',
    'Advanced Low': 'I can understand the main message and some supporting details across major time frames in conversations and discussions.',
    'Advanced Mid': 'I can understand the main message and most supporting details across major time frames in conversations and discussions.',
    'Advanced High': 'I can follow the flow of ideas and some nuances from different viewpoints in conversations and discussions.',
    'Superior': 'I can follow abstract, complex and unfamiliar topics in extended conversations and discussions involving multiple speakers.'
}

#Proficiency levels and their descriptions (Writing)
actfl_levels_writing = {
    'Novice Low': 'I can introduce myself using practiced or memorized words and phrases, with the help of gestures or visuals.',
    'Novice Mid': 'I can present information about myself, my interests and my activities using a mixture of practiced or memorized words, phrases and simple sentences.',
    'Novice High': 'I can present personal information about my life and activities, using simple sentences most of the time.',
    'Intermediate Low': 'I can express my preferences on familiar and everyday topics of interest and explain why I feel that way, using simple sentences.',
    'Intermediate Mid': 'I can state my viewpoint about familiar topics and give some reasons to support it, using sentences and series of connected sentences.',
    'Intermediate High': 'I can state my viewpoint on familiar or researched topics and provide reasons to support it, using a few short paragraphs, often across various time frames.',
    'Advanced Low': 'I can deliver presentations on some concrete academic, social and professional topics of interest, using paragraphs across major time frames.',
    'Advanced Mid': 'I can deliver detailed presentations and elaborate on a variety of concrete academic, social and professional topics of interest, using organized paragraphs across major time frames.',
    'Advanced High': 'I can deliver cohesive presentations on a variety of complex concrete topics related to community interests and some specialized fields, and often deal with related issues hypothetically.',
    'Superior': 'I can deliver extended presentations on abstract or hypothetical issues and ideas ranging from broad general interests to my areas of specialized expertise, with precision of expression and to a wide variety of audiences, using spoken, written, or signed language.'
}

#Proficiency levels and their descriptions (Speaking)
actfl_levels_speaking = {
    'Novice Low': 'I can provide information by answering a few simple questions on very familiar topics, using practiced or memorized words and phrases, with the help of gestures or visuals.',
    'Novice Mid': 'I can request and provide information by asking and answering a few simple questions on very familiar and everyday topics, using a mixture of practiced or memorized words, phrases, and simple sentences.',
    'Novice High': 'I can request and provide information by asking and answering practiced and some original questions on familiar and everyday topics, using simple sentences most of the time.',
    'Intermediate Low': 'I can express my preferences on familiar and everyday topics of interest and explain why I feel that way, using simple sentences.',
    'Intermediate Mid': 'I can request and provide information in conversations on familiar topics by creating simple sentences and asking appropriate follow-up questions.',
    'Intermediate High': 'I can exchange information in conversations on familiar topics and some researched topics, creating sentences and series of sentences and asking a variety of follow-up questions.',
    'Advanced Low': 'I can deliver presentations on some concrete academic, social and professional topics of interest, using paragraphs across major time frames.',
    'Advanced Mid': 'I can maintain discussions on a wide variety of familiar and unfamiliar concrete topics of personal and general interest, and sometimes academic, social or professional topics, by using probing questions and providing detailed responses across major time frames.',
    'Advanced High': 'I can discuss and sometimes debate a variety of complex concrete and some abstract academic, social and professional topics and often deal with related issues hypothetically, using precise questions and explanations.',
    'Superior': 'I can discuss and debate a wide variety of complex issues and abstract ideas using precise, sophisticated, and academic language.'
}


# Function to capture highest selected level for a skill
def get_highest_level_actfl(level_descriptions, skill_name):
    selected_level = None
    for level, description in level_descriptions.items():
        if st.checkbox(description, key=f"{skill_name}_{level}"):
            selected_level = level
    return proficiency_levels_actfl.get(selected_level, 0)  # Map to score or return 0 if none selected

# Capture the highest selected levels if ACTFL framework is selected
skill_scores = {}
if selected_framework == 'ACTFL (American Council of the Teaching of Foreign Language)':
    with st.expander('ACTFL Reading Proficiency Questions'):
        skill_scores['Reading'] = get_highest_level_actfl(actfl_levels_reading, 'Reading')

    with st.expander('ACTFL Listening Proficiency Questions'):
        skill_scores['Listening'] = get_highest_level_actfl(actfl_levels_listening, 'Listening')

    with st.expander('ACTFL Writing Proficiency Questions'):
        skill_scores['Writing'] = get_highest_level_actfl(actfl_levels_writing, 'Writing')

    with st.expander('ACTFL Speaking Proficiency Questions'):
        skill_scores['Speaking'] = get_highest_level_actfl(actfl_levels_speaking, 'Speaking')



# Generate bar chart if any skill level was selected
if any(skill_scores.values()):
    st.write("Proficiency Levels Across Skills")
    plt.figure(figsize=(8, 6))
    plt.bar(skill_scores.keys(), skill_scores.values(), color='skyblue')
    plt.title("Proficiency Levels Across Skills")
    plt.xlabel("Skills")
    plt.ylabel("Proficiency Level")
    plt.yticks(list(proficiency_levels_actfl.values()), list(proficiency_levels_actfl.keys()))
    st.pyplot(plt)



# Define proficiency levels for common y-axis labels
proficiency_levels_cefrl = {
    'A1': 1,
    'A2': 2,
    'B1.2': 3,
    'B2.2': 4,
    'C1': 5,
    'C2': 6,
}

#Proficiency levels and their descriptions (Reading)
cefrl_levels_reading = {
    'A1': 'I can understand familiar names, words and very simple sentences, for examples on notices and posters or in catalogues.',
    'A2': 'I can read very short, simple texts. I can find specific, predictable information in simple everyday material such as advertisements, prospectuses, menus and timetables and I can understand short simple personal letters.',
    'B1.2': 'I can understand texts that consist mainly of high frequency everyday or job-related language. I can understand the description of events, feelings and wishes in personal letters.',
    'B2.2': 'I can read articles and reports concerned with contemporary problems in which the writers adopt particular attitudes or viewpoints. I can understand contemporary literary prose.',
    'C1': 'I can understand long and complex factual and literary texts, appreciating distinctions of style. I can understand specialised articles and longer technical instructions, even when they do not relate to my field.',
    'C2': 'I can read with ease virtually all forms of the written language, including abstract, structurally or linguistically complex texts such as manuals, specialised articles and literary works.',
}


#Proficiency levels and their descriptions (listening)
cefrl_levels_listening = {
    'A1': 'I can recognize familiar words and very basic phrases concerning myself, my family and immediate concrete surroundings when people speak slowly and clearly.',
    'A2': 'I can understand phrases and the highest frequency vocabulary related to areas of most immediate personal relevance (e.g. very basic personal and family information, shopping, local area, employment). I can catch the main point in short, clear, simple messages and announcements.',
    'B1.2': 'I can understand the main points of clear standard speech on familiar matters regularly encountered in work, school, leisure, etc. I can understand the main point of many radio or TV programmes on current affairs or topics of personal or professional interest when the delivery is relatively slow and clear.',
    'B2.2': 'I can understand extended speech and lectures and follow even complex lines of argument provided the topic is reasonably familiar. I can understand most TV news and current affairs programmes. I can understand the majority of films in standard direct.',
    'C1': 'I can understand extended speech even when it is not clearly structured and when relationships are only implied and not signalled explicitly. I can understand television programmes and films without too much effort.',
    'C2': 'I have no difficulty in understanding any kind of spoken language, whether live or broadcast, even when delivered at fast native speed, provided I have some time to get familiar with the accent.',
}

#Proficiency levels and their descriptions (Writing)
cefrl_levels_writing = {
    'A1': 'I can write a short, simple postcard, for example sending holiday greetings. I can fill in forms with personal details, for example entering my name, nationality and address on a hotel registration form.',
    'A2': 'I can write short, simple notes and messages relating to matters in areas of immediate need. I can write a very simple personal letter, for example thanking someone for something.',
    'B1.2': 'I can write simple connected text on topics which are familiar or of personal interest. I can write personal letters describing experiences and impressions.',
    'B2.2': 'I can write clear, detailed text on a wide range of subjects related to my interests. I can write an essay or report, passing on information or giving reasons in support of or against a particular point of view. I can write letters highlighting the personal significance of events and experiences.',
    'C1': 'I can express myself in clear, well- structured text, expressing points of view at some length. I can write about complex subjects in a letter, an essay or a report, underlining what I consider to be the salient issues. I can select style appropriate to the reader in mind.',
    'C2': 'I can write clear, smoothly flowing text in an appropriate style. I can write complex letters, reports or articles which preset a case with an effective logical structure which helps the recipient to notice and remember significant points. I can write summaries and reviews of professional or literary works.',
}

#Proficiency levels and their descriptions (Speaking)
cefrl_levels_speaking = {
    'A1': 'I can understand familiar names, words and very simple sentences, for examples on notices and posters or in catalogues.',
    'A2': 'I can read very short, simple texts. I can find specific, predictable information in simple everyday material such as advertisements, prospectuses, menus and timetables and I can understand short simple personal letters.',
    'B1.2': 'I can understand texts that consist mainly of high frequency everyday or job-related language. I can understand the description of events, feelings and wishes in personal letters.',
    'B2.2': 'I can read articles and reports concerned with contemporary problems in which the writers adopt particular attitudes or viewpoints. I can understand contemporary literary prose.',
    'C1': 'I can understand long and complex factual and literary texts, appreciating distinctions of style. I can understand specialised articles and longer technical instructions, even when they do not relate to my field.',
    'C2': 'I can read with ease virtually all forms of the written language, including abstract, structurally or linguistically complex texts such as manuals, specialised articles and literary works.',
}


# Function to capture highest selected level for a skill
def get_highest_level_cefrl(level_descriptions, skill_name):
    selected_level = None
    for level, description in level_descriptions.items():
        if st.checkbox(description, key=f"{skill_name}_{level}"):
            selected_level = level
    return proficiency_levels_cefrl.get(selected_level, 0)  # Map to score or return 0 if none selected


# Capture the highest selected levels if ACTFL framework is selected
skill_scores = {}
if selected_framework == ('CEFRL (Common European Framework of Reference for Languages)'):
    with st.expander('CEFRL Reading Proficiency Questions'):
        skill_scores['Reading'] = get_highest_level_cefrl(cefrl_levels_reading, 'Reading')

    with st.expander('CEFRL Listening Proficiency Questions'):
        skill_scores['Listening'] = get_highest_level_cefrl(cefrl_levels_listening, 'Listening')

    with st.expander('CEFRL Writing Proficiency Questions'):
        skill_scores['Writing'] = get_highest_level_cefrl(cefrl_levels_writing, 'Writing')

    with st.expander('CEFRL Speaking Proficiency Questions'):
        skill_scores['Speaking'] = get_highest_level_cefrl(cefrl_levels_speaking, 'Speaking')


# Generate bar chart if any skill level was selected
if any(skill_scores.values()):
    st.write("Proficiency Levels Across Skills")
    plt.figure(figsize=(8, 6))
    plt.bar(skill_scores.keys(), skill_scores.values(), color='skyblue')
    plt.title("Proficiency Levels Across Skills")
    plt.xlabel("Skills")
    plt.ylabel("Proficiency Level")
    plt.yticks(list(proficiency_levels_cefrl.values()), list(proficiency_levels_cefrl.keys()))
    st.pyplot(plt)

st.divider()


#Thank you message
Thanks = 'Thank you for taking the time to complete this assessment. This tool is designed to help students gain a clearer understanding of their language proficiency. To continuously improve student experience, we welcome any feedback on the interface and usability of this site. Please feel free to share any suggestions, comments, or ideas below.'
st.markdown(f"<div style='text-align: justify;'>{Thanks}</div>", unsafe_allow_html=True)
st.text_area('', height=150)
st.divider()


#Submit button and Time
if st.button('Submit'):
    end_time = time.time()
    total_time = end_time - start_time
    minutes, seconds = divmod(total_time, 60)
    st.write(f"Time taken to complete: {int(minutes)} minutes and {int(seconds)} seconds.")
st.divider()

#Credits
# Credits text
Thanks = 'Developed by Professor Stéphanie Gaillard in collaboration with Diana Nazari, Data Science Fellow (DATA 1150).'
st.markdown(
    f"<div style='text-align: center;'>{Thanks}</div>",
    unsafe_allow_html=True
)