import streamlit as st
from interview_engine import generate_question
from sentiment_analysis import analyze_response

st.set_page_config(page_title="AI Interview Coach")

st.title("AI Interview Coach")
st.write("Practice technical interviews with AI-generated questions and get instant feedback.")

domain = st.selectbox(
    "Select Interview Domain",
    ["Data Science", "Cloud Computing", "Software Engineering", "Machine Learning"]
)

if st.button("Generate Interview Question"):
    question = generate_question(domain)
    st.session_state["question"] = question

if "question" in st.session_state:
    st.subheader("Interview Question")
    st.write(st.session_state["question"])

response = st.text_area("Your Answer")

if st.button("Evaluate Answer") and response:
    score, sentiment = analyze_response(response)

    st.subheader("Evaluation Result")
    st.write(f"Confidence Score: {score}")
    st.write(f"Sentiment: {sentiment}")
