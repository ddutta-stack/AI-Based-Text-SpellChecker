import requests
import gradio as gr
ollama_url = "http://localhost:11434/api/generate"
def correctgrammar(text):
    ''' Function to correct grammar in a given text using the Llama 3.1 model via Ollama API.'''
    prompt = f"Correct the grammar in the following text: {text}"
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt":prompt,
        "stream": False,
        "temperature": 0.4,      
    }
    