import gradio as gr
from src.predictor import predict_loan


def check_loan(
    gender,
    married,
    dependents,
    education,
    self_employed,
    loan_amount_term,
    credit_history,
    property_area,
):

    return predict_loan(
        gender,
        married,
        dependents,
        education,
        self_employed,
        loan_amount_term,
        credit_history,
        property_area
    )


with gr.Blocks(title="Loan Prediction System") as app:

    gr.Markdown(
        """
        # 🏦 Loan Prediction System

        Enter applicant details to predict loan eligibility.
        """
    )

    with gr.Row():

        gender = gr.Dropdown(
            ["Male", "Female"],
            label="Gender"
        )

        married = gr.Dropdown(
            ["Yes", "No"],
            label="Married"
        )

        dependents = gr.Dropdown(
            ["0", "1", "2", "3+"],
            label="Dependents"
        )

    with gr.Row():

        education = gr.Dropdown(
            ["Graduate", "Not Graduate"],
            label="Education"
        )

        self_employed = gr.Dropdown(
            ["Yes", "No"],
            label="Self Employed"
        )

        property_area = gr.Dropdown(
            ["Urban", "Semiurban", "Rural"],
            label="Property Area"
        )

    with gr.Row():

        loan_amount_term = gr.Number(
            label="Loan Amount Term",
            value=360
        )

        credit_history = gr.Dropdown(
            ["1", "0"],
            label="Credit History"
        )


    predict_button = gr.Button(
        "Check Loan Eligibility"
    )

    result = gr.Textbox(
        label="Prediction"
    )


    predict_button.click(
        fn=check_loan,
        inputs=[
            gender,
            married,
            dependents,
            education,
            self_employed,
            loan_amount_term,
            credit_history,
            property_area
        ],
        outputs=result
    )


app.launch()