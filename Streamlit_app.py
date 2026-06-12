import streamlit as st

st.set_page_config(
    page_title="FNP Student Success Hub",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 FNP Student Success Hub")

page = st.sidebar.selectbox(
    "Choose a Section",
    [
        "Home",
        "Board Review",
        "OSCE Practice",
        "SOAP Note Builder",
        "Guidelines"
    ]
)

if page == "Home":

    st.header("Welcome")

    st.success("Ready to learn!")

    st.write("""
    This app helps you prepare for:
    - Exams
    - OSCEs
    - Clinical practice
    - Board certification
    """)

elif page == "Board Review":

    st.header("Board Review Questions")

    question = st.radio(
        "Which medication class is considered first-line for most patients with uncomplicated hypertension?",
        [
            "Benzodiazepines",
            "Thiazide Diuretics",
            "Antibiotics",
            "Proton Pump Inhibitors"
        ]
    )

    if st.button("Check Answer"):

        if question == "Thiazide Diuretics":

            st.success("Correct!")

            st.info("""
            Rationale:

            Thiazide diuretics are considered one of the recommended
            first-line treatments for uncomplicated hypertension.
            """)

        else:

            st.error("Incorrect.")

elif page == "OSCE Practice":

    st.header("OSCE Case")

    st.write("""
    A 52-year-old patient presents with cough,
    wheezing, and shortness of breath.
    """)

    history = st.text_area(
        "What additional history would you obtain?"
    )

    if st.button("Submit OSCE Response"):

        st.success("Response recorded.")

        st.write("""
        Consider:
        - Smoking history
        - Asthma history
        - COPD history
        - Allergies
        - Trigger exposures
        - Fever
        - Medication use
        """)

elif page == "SOAP Note Builder":

    st.header("SOAP Note Builder")

    subjective = st.text_area("Subjective")

    objective = st.text_area("Objective")

    assessment = st.text_area("Assessment")

    plan = st.text_area("Plan")

    if st.button("Generate SOAP Note"):

        st.subheader("SOAP Note")

        st.write("### Subjective")
        st.write(subjective)

        st.write("### Objective")
        st.write(objective)

        st.write("### Assessment")
        st.write(assessment)

        st.write("### Plan")
        st.write(plan)

elif page == "Guidelines":

    st.header("Clinical Guidelines")

    st.write("ADA - Diabetes")

    st.write("GINA - Asthma")

    st.write("GOLD - COPD")

    st.write("ACC/AHA - Cardiovascular")

    st.write("IDSA - Infectious Disease")
