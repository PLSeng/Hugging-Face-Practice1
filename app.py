from transformers import pipeline
import gradio as gr

# Load the model
summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text)[0]['summary_text']

with gr.Blocks() as io:
    testbox = gr.Textbox(lines=4, label="Input Text", placeholder="Paste a long text here to summarize")
    gr.Interface(fn=summarize_text, inputs=testbox, outputs="text")
    
    
io.launch()