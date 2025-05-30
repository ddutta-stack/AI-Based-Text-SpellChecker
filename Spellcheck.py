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
    response = requests.post(ollama_url, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No response from model")    
    else:
        return f"Error: {response.status_code} - {response.text}"   
    # Test the function with some sample data
    
# if __name__ == "__main__":
#     sample_text = "He does likes the apples and oranges. She go to the store yesterday."
#     print(f"OriginalText: \n\n{sample_text}")
#     print("Corrected text:\n")
#     print(correctgrammar(sample_text))
    


# Gradio interface for the spell checker
interface = gr.Interface(
    fn=correctgrammar,
    inputs=gr.Textbox(label="Enter text to correct grammar", lines=5),
    outputs=gr.Textbox(label="Corrected text"), 
    title="AI-Based Text Spell Checker",
    description="This application uses Deepseek AI model via Ollama API to correct grammar in the provided text.",
    theme="default",
)
# Launch the Gradio interface the web application
if __name__ == "__main__":
    interface.launch()