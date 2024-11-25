from dotenv import load_dotenv
load_dotenv() # Load all the environment variables

import streamlit as st 
import os
import sqlite3 

import google.generativeai as genai

## Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Google gemini model and provide sql query
def get_gemini_response(question, prompt):
    # Load the gemini model
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content([question, prompt])
    return response.text

#Function to retrieve data from database
def read_sql_query(sql_query,db):
    # Create a connection to the database
    conn = sqlite3.connect(db)
    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute(sql_query)
    # Fetch the results
    results = cursor.fetchall()
    # Close the cursor and connection
    cursor.close()
    conn.close()
    for result in results:
        print(result)
    return results

#Define your prompt
prompt = [
    """
    You are an expert in converting English into SQL query!.
    The SQL database has the name student and has the following columns - Name, Class, Section, Marks.
    \n\n For Example, \n Example 1 - How may records are present in the student table?, 
    \n Answer - SELECT COUNT(*) FROM student; \n\n Example 2 - Tell me all the students in Data Science class?,
    \n Answer - SELECT * FROM student WHERE Class = 'Data Science';
    also the sql code should not have ''' in the beginning or end and sql word should be in the beginning of the query.

"""
]  


#Streamlit App
st.set_page_config(
    page_title="SQL Query Generator",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="expanded"
)   

st.title("SQL Query Generator")

# Get user input
question = st.text_input("Enter your question:", key="input")

submit = st.button("Ask the Question", key="submit")

#Submit clicked
if submit:
    response = get_gemini_response(question, prompt[0])
    st.write(response)

    if response:
        db = "student.db"
        sql_query = response
        results = read_sql_query(sql_query,db)
        st.subheader("The Results: ")
        for row in results:
            st.write(row)

    else:
        st.write("No results found.")
          

