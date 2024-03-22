from sql import set_database
from functions import add_officer, add_charge
import gradio as gr
import mysql.connector

with gr.Blocks() as demo:
    set_database()
    with gr.Tab("Add Officers"):
        with gr.Row():
            with gr.Column(scale=1):
                uid_text = gr.Textbox(label="UID")
                name_text = gr.Textbox(label="Officer Name")
                rank_text = gr.Textbox(label="Officer Rank")
                unit_text = gr.Textbox(label="Officer Unit")
                add_officer_btn = gr.Button("Add Officer")
            with gr.Column(scale=3):
                btn1 = gr.Button("Refresh")
                gr.Dataframe(
                headers=[ "Name", "Rank"],
                datatype=["str", "str"],
                row_count=5,
                col_count=(2, "fixed"),
                )
                
    with gr.Tab("Add Charge"):
        with gr.Row():
            with gr.Column(scale=1):

                #dynamic logic
                existing_officers=[]
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="your_password",
                        database="ARMY_CAMP"
                    )
                    cursor = connection.cursor()
                    select_query = "SELECT UID FROM OFFICERS"
                    cursor.execute(select_query)
                    existing_officers = [row[0] for row in cursor.fetchall()]      
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                finally:
                    cursor.close()
                    connection.close()
                #The above logic is to handle the problem that charges can only added for the
                #officers which are added.
              
                uid_dropdown = gr.Dropdown(["Select Officer"] + existing_officers, label="Officer UID")  # Placeholder UIDs
                description_text = gr.Textbox(label="Charge Description")
                amount_text = gr.Textbox(label="Charge Amount")
                date_text = gr.Textbox(label="Charge Date")
                charge_type_dropdown = gr.Dropdown(["Fixed Charge", "One-Time"], label="Charge Type")
                add_charge_btn = gr.Button("Add Charge")
            with gr.Column(scale=3):
                btn1 = gr.Button("Refresh")
                gr.Dataframe(
                headers=[ "Name", "Amount"],
                datatype=["str", "str"],
                row_count=5,
                col_count=(2, "fixed"),
                )
                
    # Linking buttons to actions
    add_officer_btn.click(add_officer, inputs=[uid_text, name_text, rank_text, unit_text], outputs=None)
    add_charge_btn.click(add_charge, inputs=[uid_dropdown, description_text, amount_text, date_text, charge_type_dropdown], outputs=None)


if __name__ == "__main__":
    demo.launch()
    