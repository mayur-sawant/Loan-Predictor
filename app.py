import streamlit as st

from src.predictor import predict_loan


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(

    page_title="Loan Predictor",

    page_icon="🏦",

    layout="wide"

)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }

    .hero {

        padding: 35px;

        border-radius: 20px;

        background:
        linear-gradient(
            135deg,
            #1e293b,
            #3730a3
        );

        color: white;

        margin-bottom: 30px;

    }

    .hero h1 {

        font-size: 42px;

        margin-bottom: 8px;

    }

    .hero p {

        font-size: 17px;

        opacity: 0.85;

    }


    .card {

        background: white;

        padding: 25px;

        border-radius: 18px;

        border: 1px solid #e2e8f0;

        box-shadow:
        0px 8px 25px rgba(
            15,
            23,
            42,
            0.06
        );

        margin-bottom: 20px;

    }


    .approved {

        padding: 25px;

        border-radius: 18px;

        background: #ecfdf5;

        border: 2px solid #10b981;

        text-align: center;

    }


    .rejected {

        padding: 25px;

        border-radius: 18px;

        background: #fef2f2;

        border: 2px solid #ef4444;

        text-align: center;

    }


    .result-title {

        font-size: 30px;

        font-weight: 800;

    }


    .result-subtitle {

        font-size: 16px;

        margin-top: 8px;

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HERO
# ==================================================

st.markdown(
    """
    <div class="hero">

        <h1>🏦 Loan Predictor</h1>

        <p>
        Machine Learning powered loan eligibility
        prediction system.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("📊 About")

    st.write(
        """
        This application uses a
        Logistic Regression model to
        predict loan eligibility.
        """
    )

    st.divider()

    st.subheader("Model")

    st.write("Algorithm: Logistic Regression")

    st.write("Preprocessing: Scikit-Learn Pipeline")

    st.write("UI: Streamlit")

    st.divider()

    st.caption(
        "Loan Prediction Project"
    )


# ==================================================
# INPUT CARD
# ==================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


st.subheader("👤 Applicant Information")


col1, col2 = st.columns(2)


# ==================================================
# LEFT COLUMN
# ==================================================

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


# ==================================================
# RIGHT COLUMN
# ==================================================

with col2:

    dependents = st.selectbox(

        "Number of Dependents",

        ["0", "1", "2", "3+"]

    )


    property_area = st.selectbox(

        "Property Area",

        [
            "Urban",
            "Semiurban",
            "Rural"
        ]

    )


    loan_amount_term = st.number_input(

        "Loan Amount Term",

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
            "Good (1)" if x == 1
            else "Bad (0)"

    )


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ==================================================
# VALIDATION
# ==================================================

def validate_inputs():

    errors = []


    if loan_amount_term <= 0:

        errors.append(
            "Loan amount term must be greater than 0."
        )


    if credit_history not in [0, 1]:

        errors.append(
            "Invalid credit history."
        )


    if dependents not in [
        "0",
        "1",
        "2",
        "3+"
    ]:

        errors.append(
            "Invalid dependents value."
        )


    return errors


# ==================================================
# PREDICT BUTTON
# ==================================================

st.markdown("### 🔍 Prediction")


if st.button(
    "Check Loan Eligibility",
    type="primary",
    use_container_width=True
):

    errors = validate_inputs()


    if errors:

        for error in errors:

            st.error(error)


    else:

        with st.spinner(
            "Analyzing applicant information..."
        ):

            result, confidence = predict_loan(

                gender,

                married,

                dependents,

                education,

                self_employed,

                loan_amount_term,

                credit_history,

                property_area

            )


        # ==========================================
        # APPROVED
        # ==========================================

        if result == "Loan Approved":

            st.markdown(
                f"""
                <div class="approved">

                    <div class="result-title">
                        ✅ Loan Approved
                    </div>

                    <div class="result-subtitle">

                        Predicted confidence:
                        <b>{confidence * 100:.2f}%</b>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ==========================================
        # REJECTED
        # ==========================================

        else:

            st.markdown(
                f"""
                <div class="rejected">

                    <div class="result-title">
                        ❌ Loan Rejected
                    </div>

                    <div class="result-subtitle">

                        Predicted confidence:
                        <b>{confidence * 100:.2f}%</b>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Built with Python • Pandas • Scikit-Learn • Streamlit"
)