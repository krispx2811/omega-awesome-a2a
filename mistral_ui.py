import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time
from datetime import datetime

# Initialize the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "mistralai/Mistral-7B-Instruct-v0.3"
    st.info("Loading Mistral-7B model... This may take a minute.")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        torch_dtype=torch.float16, 
        device_map="auto"
    )
    return tokenizer, model

tokenizer, model = load_model()

# Function to generate a response
def generate_response(prompt, max_length, temperature, top_p, repetition_penalty):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    start_time = time.time()
    output = model.generate(
        **inputs,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        pad_token_id=tokenizer.eos_token_id
    )
    elapsed_time = time.time() - start_time
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response, elapsed_time

# Streamlit UI layout
st.title("🚀 Mistral-7B Text Generator")
st.write("Interact with the Mistral-7B-Instruct-v0.3 model for text generation.")

# Input prompt
prompt = st.text_area("📝 Enter your prompt here:", "Explain quantum computing in simple terms.")

# Parameter sliders
st.sidebar.header("🔧 Adjust Generation Parameters")
max_length = st.sidebar.slider("Max Length", 50, 500, 200, step=10)
temperature = st.sidebar.slider("Temperature", 0.1, 1.5, 0.7, step=0.1)
top_p = st.sidebar.slider("Top-p (nucleus sampling)", 0.1, 1.0, 0.9, step=0.05)
repetition_penalty = st.sidebar.slider("Repetition Penalty", 0.5, 2.0, 1.0, step=0.1)

# Generate button
if st.button("✨ Generate Response"):
    if prompt:
        st.info("Generating response... Please wait.")
        response, elapsed_time = generate_response(prompt, max_length, temperature, top_p, repetition_penalty)
        
        # Display response
        st.subheader("🗣 Model Response:")
        st.write(response)
        
        # Display generation time
        st.success(f"⏱ Response generated in {elapsed_time:.2f} seconds.")
        
        # Save to log
        with open("mistral_ui_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()}\nPrompt: {prompt}\nResponse: {response}\n{'='*60}\n")
        st.info("💾 Response saved to log.")
    else:
        st.warning("Please enter a prompt before generating.")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Hugging Face Transformers.")
