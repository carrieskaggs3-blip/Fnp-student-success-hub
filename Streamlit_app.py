import streamlit as st

st.set_page_config(
    page_title="FNP Student Success Hub",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 FNP Student Success Hub")

st.write("""
Welcome to the FNP Student Success Hub.

Use this app for:
- Board review
- OSCE preparation
- SOAP note practice
- Clinical guidelines
- Practice questions
""")

page = st.sidebar.selectbox(
    "Choose a section",
    [
        "Home",
        "Practice Questions",
        "OSCE Practice",
        "SOAP Notes"
    ]
)

if page == "Home":
    st.header("Welcome")
    st.success("Ready to learn!")

elif page == "Practice Questions":
    st.header("Practice Question")

    answer = st.radio(
        "Which medication class is first-line for most patients with hypertension?",
        [
            "Benzodiazepines",
            "Thiazide diuretics",
            "Antibiotics",
            "PPIs"
        ]
    )

    if st.button("Check Answer"):
        if answer == "Thiazide diuretics":
            st.success("Correct!")
        else:
            st.error("Review hypertension guidelines.")

elif page == "OSCE Practice":
    st.header("OSCE Scenario")

    st.write(
        "A 52-year-old patient presents with cough, wheezing, and shortness of breath."
    )

    response = st.text_area(
        "What additional history would you obtain?"
    )

    if st.button("Submit"):
        st.success("Great clinical thinking!")

elif page == "SOAP Notes":
    st.header("SOAP Note Builder")

    subjective = st.text_area("Subjective")
    objective = st.text_area("Objective")
    assessment = st.text_area("Assessment")
    plan = st.text_area("Plan")

    if st.button("Generate SOAP"):
        st.write("## SOAP Note")
        st.write("### Subjective")
        st.write(subjective)

        st.write("### Objective")
        st.write(objective)

        st.write("### Assessment")
        st.write(assessment)

        st.write("### Plan")
        st.write(plan)
