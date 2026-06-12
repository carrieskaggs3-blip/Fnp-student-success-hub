import streamlit as st
import random

st.set_page_config(
    page_title="FNP Student Success Hub",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 FNP Student Success Hub")

st.sidebar.title("Student Menu")

page = st.sidebar.selectbox(
    "Choose a Section",
    [
        "Home",
        "Announcements",
        "Board Review",
        "OSCE Cases",
        "SOAP Note Builder",
        "Guideline Center",
        "Student Reflection"
    ]
)

questions = [
    {
        "topic": "Hypertension",
        "question": "Which medication class is commonly used first-line for uncomplicated hypertension?",
        "options": ["Benzodiazepines", "Thiazide diuretics", "Antibiotics", "PPIs"],
        "answer": "Thiazide diuretics",
        "rationale": "Thiazide diuretics are one recommended first-line option for uncomplicated hypertension."
    },
    {
        "topic": "Diabetes",
        "question": "Which lab best reflects average glucose control over about 3 months?",
        "options": ["CBC", "A1C", "TSH", "BNP"],
        "answer": "A1C",
        "rationale": "A1C reflects average blood glucose over about 3 months."
    },
    {
        "topic": "Hyperlipidemia",
        "question": "Which medication class lowers LDL and reduces ASCVD risk?",
        "options": ["Statins", "Beta blockers", "Loop diuretics", "Antihistamines"],
        "answer": "Statins",
        "rationale": "Statins lower LDL and reduce cardiovascular risk."
    },
    {
        "topic": "Asthma",
        "question": "Which test helps confirm obstructive lung disease?",
        "options": ["Spirometry", "Urinalysis", "CBC", "TSH"],
        "answer": "Spirometry",
        "rationale": "Spirometry helps assess airflow obstruction."
    },
    {
        "topic": "Thyroid",
        "question": "Which lab is usually checked first when evaluating thyroid function?",
        "options": ["A1C", "TSH", "BNP", "Troponin"],
        "answer": "TSH",
        "rationale": "TSH is usually the initial screening test for thyroid dysfunction."
    }
]

osce_cases = {
    "Asthma Exacerbation": {
        "stem": "A 24-year-old presents with wheezing, cough, and shortness of breath after exposure to a dog.",
        "history": ["Trigger exposure", "Nighttime symptoms", "Rescue inhaler use", "Prior hospitalizations", "Allergies"],
        "plan": ["Assess severity", "Short-acting bronchodilator", "Consider steroid if moderate/severe", "Trigger education", "Follow-up plan"]
    },
    "Hypertension Follow-Up": {
        "stem": "A 56-year-old returns for BP follow-up. Office BP today is 152/92.",
        "history": ["Home BP readings", "Medication adherence", "Dietary sodium", "NSAID use", "Chest pain or neurologic symptoms"],
        "plan": ["Confirm BP pattern", "Lifestyle counseling", "Medication adjustment", "Assess target organ risk", "Follow-up"]
    },
    "Diabetes Follow-Up": {
        "stem": "A 60-year-old with type 2 diabetes has an A1C of 8.2%.",
        "history": ["Medication adherence", "Hypoglycemia", "Diet", "Exercise", "Complication screening"],
        "plan": ["Review medications", "Lifestyle counseling", "Foot exam", "Eye exam referral if due", "Follow-up A1C"]
    }
}

if page == "Home":
    st.header("Welcome")
    st.success("Use this hub to study, practice, and build clinical reasoning.")

    st.write("""
    This app supports:
    - Board review
    - OSCE preparation
    - SOAP note practice
    - Guideline review
    - Student reflection
    """)

    st.info("Focus on diagnosis, first-line treatment, patient education, safety, and follow-up.")

elif page == "Announcements":
    st.header("Course Announcements")

    st.warning("""
    Exam reminder:
    Review first-line treatments, diagnostic criteria, guideline updates, and red flags.
    """)

    st.info("""
    OSCE reminder:
    Verbalize your assessment, explain your plan clearly, and remember that this is similar to what you do in clinical.
    """)

elif page == "Board Review":
    st.header("Board Review")

    topic_list = ["All Topics"] + sorted(list(set(q["topic"] for q in questions)))
    selected_topic = st.selectbox("Choose a topic", topic_list)

    if selected_topic == "All Topics":
        filtered_questions = questions
    else:
        filtered_questions = [q for q in questions if q["topic"] == selected_topic]

    q = st.selectbox(
        "Choose a question",
        filtered_questions,
        format_func=lambda x: x["question"]
    )

    st.subheader(q["topic"])
    answer = st.radio(q["question"], q["options"])

    if st.button("Check Answer"):
        if answer == q["answer"]:
            st.success("Correct.")
        else:
            st.error(f"Not quite. Correct answer: {q['answer']}")

        st.info(q["rationale"])

elif page == "OSCE Cases":
    st.header("OSCE Practice Cases")

    case_name = st.selectbox("Choose a case", list(osce_cases.keys()))
    case = osce_cases[case_name]

    st.subheader(case_name)
    st.write(case["stem"])

    student_history = st.text_area("What additional history would you obtain?")
    student_plan = st.text_area("What is your assessment and plan?")

    if st.button("Review OSCE Response"):
        st.success("Response submitted for this session.")

        st.write("Important history to consider:")
        for item in case["history"]:
            st.write(f"- {item}")

        st.write("Plan items to consider:")
        for item in case["plan"]:
            st.write(f"- {item}")

elif page == "SOAP Note Builder":
    st.header("SOAP Note Builder")

    subjective = st.text_area("Subjective")
    objective = st.text_area("Objective")
    assessment = st.text_area("Assessment")
    plan = st.text_area("Plan")

    if st.button("Generate SOAP Note"):
        st.subheader("Generated SOAP Note")

        st.write("### Subjective")
        st.write(subjective if subjective else "Not entered.")

        st.write("### Objective")
        st.write(objective if objective else "Not entered.")

        st.write("### Assessment")
        st.write(assessment if assessment else "Not entered.")

        st.write("### Plan")
        st.write(plan if plan else "Not entered.")

elif page == "Guideline Center":
    st.header("Guideline Center")

    st.write("Use these as quick reminders for major guideline groups.")

    st.subheader("Common Guideline Areas")
    st.write("- ADA: Diabetes")
    st.write("- GINA: Asthma")
    st.write("- GOLD: COPD")
    st.write("- ACC/AHA: Cardiovascular disease and hyperlipidemia")
    st.write("- IDSA: Infectious disease")
    st.write("- USPSTF: Screening and prevention")

    st.warning("Always verify current recommendations through official guideline sources.")

elif page == "Student Reflection":
    st.header("Student Reflection")

    topic = st.text_input("What topic do you need to review?")
    confidence = st.slider("How confident do you feel today?", 1, 10, 5)
    plan = st.text_area("What is your study plan?")

    if st.button("Submit Reflection"):
        st.success("Reflection submitted for this session.")
        st.write("Topic:", topic)
        st.write("Confidence:", confidence)
        st.write("Study plan:", plan)
