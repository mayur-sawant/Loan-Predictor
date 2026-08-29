import streamlit as st

from ui.ui import process_and_predict

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🏦 Loan Prediction System")
st.caption("Machine Learning powered loan eligibility prediction using Logistic Regression.")

with st.sidebar:
    st.header("📊 About the Model")
    st.write("This application predicts loan eligibility using a Logistic Regression model.")
    st.divider()
    st.subheader("Model Features")
    for item in [
        "Gender",
        "Marital Status",
        "Dependents",
        "Education",
        "Self Employment",
        "Loan Term",
        "Credit History",
        "Property Area",
    ]:
        st.write(f"• {item}")

    st.caption("Loan Prediction ML Project")

with st.form("loan_form"):
    st.subheader("👤 Applicant Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        married = st.radio("Marital Status", ["Yes", "No"], horizontal=True)
        education = st.radio("Education", ["Graduate", "Not Graduate"], horizontal=True)
        self_employed = st.radio("Self Employed", ["Yes", "No"], horizontal=True)

    with col2:
        dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
        loan_amount_term = st.number_input(
            "Loan Amount Term (days)",
            min_value=1,
            max_value=1000,
            value=360,
            step=1,
        )
        credit_history = st.radio(
            "Credit History",
            [1, 0],
            horizontal=True,
            format_func=lambda x: "Good (1)" if x == 1 else "Bad (0)",
        )

    submitted = st.form_submit_button("Check Loan Eligibility", use_container_width=True)

if submitted:
    with st.spinner("Analyzing applicant information..."):
        prediction, errors = process_and_predict(
            gender,
            married,
            dependents,
            education,
            self_employed,
            loan_amount_term,
            credit_history,
            property_area,
        )

    if errors:
        st.error("Please correct the following:")
        for error in errors:
            st.warning(error)
    elif prediction == "Loan Approved":
        st.success("✅ Loan Approved\n\nBased on the provided information, the applicant is predicted to be eligible for the loan.")
    elif prediction == "Loan Rejected":
        st.error("❌ Loan Rejected\n\nBased on the provided information, the applicant is predicted to be not eligible for the loan.")

st.markdown("---")
st.caption("Built with Python • Scikit-Learn • Pandas • Streamlit")