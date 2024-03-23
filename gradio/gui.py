import pandas as pd
from create_db import set_database
from functions import add_officer, add_charge, existing_officers_name, existing_officers_uid, get_name_rank,get_total_charges,get_name_from_uid,get_name_uid
import gradio as gr

def refresh_officers(dataframe):
    officers_data = get_name_rank()  # Fetch officers' details from the database
    print(type(officers_data))
    officers_df = pd.DataFrame(officers_data)
    print(officers_df)
    dataframe.update(data=officers_df)

def refresh_charges(dataframe):
    charges_data = get_name_rank()  # Fetch charges' details from the database
    dataframe.update(data=charges_data)


with gr.Blocks() as demo:
    set_database()
    print(get_name_rank)
    with gr.Tab("Add Officers"):
        with gr.Row():
            with gr.Column(scale=1):
                uid_text = gr.Textbox(label="UID")
                name_text = gr.Textbox(label="Officer Name")
                rank_text = gr.Textbox(label="Officer Rank")
                unit_text = gr.Textbox(label="Officer Unit")
                add_officer_btn = gr.Button("Add Officer")
            with gr.Column(scale=3):
                officers_dataframe = gr.Dataframe(
                    headers=["Name", "Rank"],
                    datatype=["str", "str"],
                    row_count=20,
                    col_count=(2, "fixed"),
                )
                refresh_officers_btn = gr.Button("Refresh Officers")
                
    with gr.Tab("Add Charge"):
        with gr.Row():
            with gr.Column(scale=1):
                uid_dropdown = gr.Dropdown(["Select Officer"] + get_name_uid(), label="Officer UID")
                description_text = gr.Textbox(label="Charge Description")
                amount_text = gr.Textbox(label="Charge Amount")
                date_text = gr.Textbox(label="Charge Date")
                charge_type_dropdown = gr.Dropdown(["Fixed Charge", "One-Time"], label="Charge Type")
                add_charge_btn = gr.Button("Add Charge")
            with gr.Column(scale=3):
                charges_dataframe = gr.Dataframe(
                    headers=["Name", "Amount"],
                    datatype=["str", "str"],
                    row_count=20,
                    col_count=(2, "fixed"),
                )
                refresh_charges_btn = gr.Button("Refresh Charges")

    message_output = gr.Textbox(label="Status", interactive=False, lines=2)
    
    # print (get_total_charges(12))
    # print (get_name_from_uid(12))

    # Linking buttons to actions
    add_officer_btn.click(add_officer, inputs=[uid_text, name_text, rank_text, unit_text], outputs=message_output)
    add_charge_btn.click(add_charge, inputs=[uid_dropdown, description_text, amount_text, date_text, charge_type_dropdown], outputs=message_output)
    refresh_officers_btn.click(refresh_officers, inputs=[], outputs=officers_dataframe)
    refresh_charges_btn.click(refresh_charges, inputs=[], outputs=charges_dataframe)


if __name__ == "__main__":
    demo.launch()
