import logging
import threading

import tensorflow as tf
import torch
from flask import Flask, jsonify, redirect, render_template, request, url_for
from transformers import (AutoTokenizer, T5ForConditionalGeneration,
                          T5Tokenizer, TFAutoModelForSeq2SeqLM)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load pre-trained model and tokenizer
llm_tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
llm_model = TFAutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# nlp_tokenizer = T5Tokenizer.from_pretrained("google/t5-base")
# nlp_model = T5ForConditionalGeneration.from_pretrained("google/t5-base")

# Function for summarization
def summarize_text(text):
    try:
        inputs = llm_tokenizer("summarize: " + text, return_tensors="tf", max_length=5000, truncation=True)
        summary_ids = llm_model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = llm_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        logger.error(f"Error during summarization: {e}")
        return "Error in summarization."

# Create Flask app
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login logic (e.g., verify user credentials)
        return redirect(url_for('landing_page'))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle registration logic (e.g., create a new user)
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/summaryizetext", methods=["POST"])
def summary():
    input_text = request.form.get("text", "")
    result = {}

    if not input_text:
        return jsonify({"error": "Missing input text"}), 400

    def summarization_task():
        summary = summarize_text(input_text)
        result["summary"] = summary

    thread = threading.Thread(target=summarization_task)
    thread.start()
    thread.join()  # Wait for the thread to complete

    return jsonify(result)

@app.route("/summarize")
def summarize():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    pass


# @app.route("/analyse", methods=["POST"])
# def analyse():
#     input_text = request.form.get("text", "")
#     target_language = request.form.get("target_language", "")

#     if not input_text or not target_language:
#         return jsonify({"error": "Missing text or target language"}), 400

#     # Assuming source_language is known or determined somehow
#     source_language = "en"  # Example source language (Romanian)

#     # Format input for T5
#     formatted_input = f"translate {source_language} to {target_language}: {input_text}"
#     inputs = nlp_tokenizer(formatted_input, return_tensors="pt")

#     try:
#         with torch.no_grad():
#             outputs = nlp_model.generate(**inputs)

#         # Decode the output
#         translated_text = nlp_tokenizer.decode(outputs[0], skip_special_tokens=True)
#         logger.info(f"Translated text: {translated_text}")
#         return jsonify({"translation": translated_text})
#     except Exception as e:
#         logger.error(f"Error during translation: {e}")
#         return jsonify({"error": "Translation error."}), 500

@app.route("/translate")
def translate():
    return render_template("translate.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0')
