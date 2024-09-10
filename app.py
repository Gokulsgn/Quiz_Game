import streamlit as st

# Set page configuration including the favicon
st.set_page_config(
    page_title="Virat Kohli Quiz Game",
    page_icon="https://i.pinimg.com/736x/c0/d2/16/c0d2167e934834850425254fad924d47.jpg",  # Path to your favicon file
    layout="centered",
    initial_sidebar_state="auto"
)

# Updated list of questions and answers for the quiz
questions = [
    {
        "question": "In which year did Virat Kohli make his debut for the Indian national team?",
        "options": ["2009", "2010", "2008", "2011"],
        "answer": "2008"
    },
    {
        "question": "What is Virat Kohli's highest individual score in an ODI match?",
        "options": ["200", "183", "210", "250"],
        "answer": "183"
    },
    {
        "question": "Which IPL team did Virat Kohli lead to the finals in 2016?",
        "options": ["Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Delhi Capitals"],
        "answer": "Royal Challengers Bangalore"
    },
    {
        "question": "How many centuries did Virat Kohli score in the 2018 Test series against Australia?",
        "options": ["5", "6", "4", "3"],
        "answer": "3"
    },
    {
        "question": "Which team did Virat Kohli play for in the 2008 U-19 Cricket World Cup?",
        "options": ["Australia", "India", "Pakistan", "England"],
        "answer": "India"
    },
    {
        "question": "What is Virat Kohli's nickname?",
        "options": ["Rocky", "Teddy", "Chiku", "Sunny"],
        "answer": "Chiku"
    },
    {
        "question": "Which award did Virat Kohli win in 2018 for his exceptional performance in international cricket?",
        "options": ["ICC Emerging Player of the Year", "ICC Cricketer of the Year", "ICC T20 Player of the Year", "ICC Player of the Year"],
        "answer": "ICC Cricketer of the Year"
    }
]

def main():
    st.markdown("<h1 style='text-align: center;'>Virat Kohli Quiz Game</h1>", unsafe_allow_html=True)
    
    # Create a dictionary to store user responses
    responses = {}

    # Collect responses for all questions
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        selected_option = st.radio("Select an option:", q["options"], key=i)
        responses[i] = selected_option

    # Add a submit button for the entire quiz
    if st.button("Submit"):
        score = 0
        for i, q in enumerate(questions):
            if responses[i] == q["answer"]:
                st.success(f"Question {i+1}: Correct!")
                score += 1
            else:
                st.error(f"Question {i+1}: Incorrect! The correct answer was: {q['answer']}")

        st.write(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
