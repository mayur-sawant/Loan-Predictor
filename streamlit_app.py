import streamlit as st

from input import process_and_predict


# PAGE CONFIG

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 100%
        );
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero */
    .hero {
        background: linear-gradient(
            135deg,
            #1e293b,
            #312e81
        );

        padding: 35px;
        border-radius: 22px;

        color: white;

        margin-bottom: 30px;

        box-shadow:
            0 15px 35px rgba(0,0,0,0.12);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.85;
    }

    /* Cards */
    .card {
        background: white;

        padding: 25px;

        border-radius: 18px;

        margin-bottom: 20px;

        box-shadow:
            0 8px 25px rgba(15,23,42,0.07);

        border: 1px solid #e2e8f0;
    }

    /* Section heading */
    .section-title {
        font-size: 23px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 18px;
    }

    /* Result */
    .approved {
        background: #ecfdf5;
        border: 2px solid #10b981;

        padding: 25px;

        border-radius: 18px;

        text-align: center;

        color: #065f46;
    }

    .rejected {
        background: #fef2f2;
        border: 2px solid #ef4444;

        padding: 25px;

        border-radius: 18px;

        text-align: center;

        color: #991b1b;
    }

    .result-title {
        font-size: 28px;
        font-weight: 800;
    }

    .result-text {
        font-size: 16px;
        margin-top: 8px;
    }

    /* Button */
    div.stButton > button {
        width: 100%;

        border-radius: 12px;

        padding: 13px;

        font-size: 17px;

        font-weight: 700;
    }

    /* Footer */
    .footer {
        text-align: center;

        color: #64748b;

        margin-top: 40px;

        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# HERO


st.markdown(
    """
    <div class="hero">

        <h1>🏦 Loan Prediction System</h1>

        <p>
        Machine Learning powered loan eligibility prediction
        using Logistic Regression.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# SIDEBAR

with st.sidebar:

    st.markdown("## 📊 About the Model")

    st.write(
        """
        This application predicts loan eligibility
        using a Logistic Regression model.
        """
    )

    st.divider()

    st.markdown("### Model Features")

    st.write("• Gender")
    st.write("• Marital Status")
    st.write("• Dependents")
    st.write("• Education")
    st.write("• Self Employment")
    st.write("• Loan Term")
    st.write("• Credit History")
    st.write("• Property Area")

    st.divider()

    st.caption(
        "Loan Prediction ML Project"
    )

# INPUT SECTION


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">👤 Applicant Information</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )


    married = st.radio(
        "Marital Status",
        ["Yes", "No"],
        horizontal=True
    )


    education = st.radio(
        "Education",
        ["Graduate", "Not Graduate"],
        horizontal=True
    )


    self_employed = st.radio(
        "Self Employed",
        ["Yes", "No"],
        horizontal=True
    )


with col2:

    dependents = st.selectbox(
        "Number of Dependents",
        ["0", "1", "2", "3+"]
    )


    property_area = st.selectbox(
        "Property Area",
        ["Urban", "Semiurban", "Rural"]
    )


    loan_amount_term = st.number_input(
        "Loan Amount Term (days)",
        min_value=1,
        max_value=1000,
        value=360,
        step=1
    )


    credit_history = st.radio(
        "Credit History",
        [1, 0],
        horizontal=True,
        format_func=lambda x:
            "Good (1)" if x == 1 else "Bad (0)"
    )


st.markdown("</div>", unsafe_allow_html=True)


# PREDICTION BUTTON

st.markdown("### 🔍 Check Eligibility")

predict_button = st.button(
    "Check Loan Eligibility",
    type="primary",
    use_container_width=True
)


# PREDICTION


if predict_button:

    with st.spinner("Analyzing applicant information..."):

        prediction, errors = process_and_predict(
            gender,
            married,
            dependents,
            education,
            self_employed,
            loan_amount_term,
            credit_history,
            property_area
        )


    # Validation errors

    if errors:

        st.error("Please correct the following:")

        for error in errors:
            st.warning(error)


    # Prediction result

    elif prediction == "Loan Approved":

        st.markdown(
            """
            <div class="approved">

                <div class="result-title">
                    ✅ Loan Approved
                </div>

                <div class="result-text">
                    Based on the provided information,
                    the applicant is predicted to be eligible
                    for the loan.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    elif prediction == "Loan Rejected":

        st.markdown(
            """
            <div class="rejected">

                <div class="result-title">
                    ❌ Loan Rejected
                </div>

                <div class="result-text">
                    Based on the provided information,
                    the applicant is predicted to be not eligible
                    for the loan.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# FOOTER

st.markdown(
    """
    <div class="footer">

        Built with Python • Scikit-Learn • Pandas • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)