import streamlit as st 
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
import altair as alt
import plotly.express as px

def read_json(json_path):
    """
        input (str) : path of json file
        output (json): return a json file
    """
    # Opening JSON file
    f = open(json_path,"r")

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    return data

data = read_json('test.json')

st.set_page_config(page_title = 'Auto Recruitment Dashboard', 
    layout='wide',
    page_icon='💹')


st.markdown(f"<h1 style='text-align: center; color: red;'>Auto Recruitment</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: black;'>This application is a Recruitment dashboard</p>", unsafe_allow_html=True)


st.sidebar.title("Auto Recruitment")
st.sidebar.markdown("This application is a Recruitment dashboard:")
st.markdown("<hr/>", unsafe_allow_html=True)

def get_profile_names(data):
    p_names = []
    for p in data.keys():
        p_names.append(data[p]['Name'])
    return p_names

st.sidebar.title("Profiles")
select = st.sidebar.selectbox('User', get_profile_names(data), key='1')


    
def working_domains(data):
    name = data['Name']
    domain = data['Working_Domain']
    scores = domain['Scores']
    skills = domain['Skills']
    return scores, skills



def search_profile_by_name(name,data):
    for key in data.keys():
        profile = data[key]
        if profile['Name'].lower() == name.lower():
            return profile
    
def JD_matched_skills(profile_data):
    skills = profile_data['JD matched skills']
    return skills
 
def resume_linkedin_matched_skills(profile_data):
    skills = profile_data['Resume linkedin matched skills']
    return skills

def experience_details(profile_data):
    experience = profile_data['Experience Details']
    total_exp = experience[-1]
    company_exp = experience[0]
    return total_exp, company_exp

def skills_from_experience(profile_data):
    skills = profile_data['Skills from Experience']
    return skills

if select:    
    profile_data = search_profile_by_name(select,data)
    
    scores, skills = working_domains(profile_data)
    jd_matched_skills = JD_matched_skills(profile_data)
    resume_linkedin_matched_skills = resume_linkedin_matched_skills(profile_data)
    total_exp, company_exp = experience_details(profile_data)
    skills_from_experience = skills_from_experience(profile_data)
    
    st.markdown("## Working Domain & Score")
    if scores:
        score_df = pd.DataFrame(scores.items(),columns = ['domain','score']) 
        fig = px.pie(score_df, values='score', names='domain', title='Working Domain Score')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    else:
        st.markdown("Working Domains not Found!")
    st.markdown("<hr/>", unsafe_allow_html=True)
          
        
    
    st.markdown("## Skills Matched with Job Description") 
    if jd_matched_skills:
        score_df = pd.DataFrame(jd_matched_skills.items(),columns = ['skill','score']) 
        fig = px.pie(score_df, values='score', names='skill', title='JD skills & Score')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    else:
        st.markdown("No skill matched with Job Description!")
    st.markdown("<hr/>", unsafe_allow_html=True)
      
        
    
    st.markdown("## Resume Linkedin Matched Skills & Score")
    if resume_linkedin_matched_skills:
        score_df = pd.DataFrame(resume_linkedin_matched_skills.items(),columns = ['skills','score']) 
        fig = px.pie(score_df, values='score', names='skills', title='Resume Linkedin Matched Skills & Score')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    else:
        st.markdown("Skills mentioned in linkedin not matched with resume's skills!")
    st.markdown("<hr/>", unsafe_allow_html=True)
        
        
    st.markdown("## Experience Details")
    if company_exp:
        st.markdown(f"<h1 style='text-align: center; color: blue;'>Total Experience : {total_exp} years</h1>", unsafe_allow_html=True)
        score_df = pd.DataFrame(company_exp.items(),columns = ['Company','Experience']) 
        fig = px.bar(score_df,x='Company',y='Experience',color="Experience", title="Experience Details",height=600)
        
        st.plotly_chart(fig)
    else:
        st.markdown("Experience not Found!")
    st.markdown("<hr/>", unsafe_allow_html=True)
        
    
    
    st.markdown("## Skills & Scores From Experience")
    if skills_from_experience:
        score_df = pd.DataFrame(skills_from_experience.items(),columns = ['skills','score']) 
        fig = px.pie(score_df, values='score', names='skills', title='Skills & Scores From Experience')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    else:
        st.markdown("Skills not matched with Experience")
    st.markdown("<hr/>", unsafe_allow_html=True)
        
