import pandas as pd
import numpy as np

import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Add Officers"):
        with gr.Row():
            with gr.Column(scale=1):
                text1 = gr.Textbox(label="UID")
                text2 = gr.Textbox(label="Officer Name")
                text2 = gr.Textbox(label="Officer Rank")
                text2 = gr.Textbox(label="Officer Unit")
                btn1 = gr.Button("Add Officer")
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
                gr.Dropdown(
                ["A", "B", "C"], label="Officer", info="Choose Officer"
                ),
                text2 = gr.Textbox(label="Charge Description")
                text2 = gr.Textbox(label="Charge Amount")
                text2 = gr.Textbox(label="Charge Date")
                gr.CheckboxGroup(["Fixed Charge", "One-Time"], label="Charge Type"),
                btn1 = gr.Button("Add Charge")
            with gr.Column(scale=3):
                btn1 = gr.Button("Refresh")
                gr.Dataframe(
                headers=[ "Name", "Amount"],
                datatype=["str", "str"],
                row_count=5,
                col_count=(2, "fixed"),
                )
                        
        
if __name__ == "__main__":
    demo.launch()
