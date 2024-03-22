import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        bike_type = gr.Plot()
        station = gr.Plot()

    demo.load(get_count_ride_type, inputs=None, outputs=bike_type)
    demo.load(get_most_popular_stations, inputs=None, outputs=station)

demo.launch()
