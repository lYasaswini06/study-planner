import streamlit as st

# Function to generate the study plan
def generate_study_plan(goal, subject, study_time, study_days, current_grade, learning_style, difficulty_level, strengths, weaknesses, learning_methods):
    study_plan = []

    for i in range(study_days):
        if i % 2 == 0:
            study_plan.append(f"Day {i+1}: Review notes and textbook for {subject} ({study_time} hours)")
        else:
            study_plan.append(f"Day {i+1}: Practice problems and exercises for {subject} ({study_time} hours)")

    # Add strategies based on learning style
    if learning_style == "Visual":
        study_plan.append("📊 Use diagrams and charts to visualize concepts.")
    elif learning_style == "Auditory":
        study_plan.append("🎧 Listen to audio lectures or podcasts on the subject.")
    elif learning_style == "Kinesthetic":
        study_plan.append("🧪 Use hands-on activities and experiments to learn concepts.")

    # Add tips based on difficulty
    if difficulty_level == "Easy":
        study_plan.append("🔁 Focus on reviewing and practicing previously learned material.")
    elif difficulty_level == "Medium":
        study_plan.append("🆕 Focus on learning new concepts and practicing problems.")
    elif difficulty_level == "Hard":
        study_plan.append("🚀 Focus on mastering complex concepts and practicing challenging problems.")

    # Use strengths and weaknesses
    study_plan.append(f"💪 Your strength in {subject}: {strengths}")
    study_plan.append(f"⚠️ Your weakness in {subject}: {weaknesses}")

    # Learning methods
    study_plan.append(f"📚 Preferred learning methods: {', '.join(learning_methods)}")

    return study_plan

# Streamlit UI
st.title("📘 Personalized Study Planner")
st.write("Please fill out the form to generate a personalized study plan")

with st.form("study_plan_form"):
    goal = st.text_input("What is your study goal (e.g. pass an exam, finish a project)?")
    subject = st.selectbox("What subject do you want to study?", ["Math", "Science", "English", "History", "Other"])
    strengths = st.text_input("What are your strengths in the subject?")
    weaknesses = st.text_input("What are your weaknesses in the subject?")
    study_time = st.slider("How many hours can you dedicate to studying per day?", 1, 8)
    study_days = st.slider("How many days a week can you study?", 1, 7)
    current_grade = st.selectbox("What is your current grade level?", ["Freshman", "Sophomore", "Junior", "Senior"])
    learning_style = st.selectbox("What is your learning style?", ["Visual", "Auditory", "Kinesthetic"])
    learning_methods = st.multiselect("Which learning methods do you prefer?", ["Reading", "Watching videos", "Doing hands-on activities"])
    difficulty_level = st.selectbox("How difficult do you find the subject?", ["Easy", "Medium", "Hard"])
    submit = st.form_submit_button("Generate Study Plan")

if submit:
    plan = generate_study_plan(goal, subject, study_time, study_days, current_grade, learning_style, difficulty_level, strengths, weaknesses, learning_methods)
    st.subheader("📅 Your Personalized Study Plan")
    for line in plan:
        st.write("✅ " + line)
