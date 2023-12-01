# backend.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS

openai.api_key = 'your-api-key'  # Replace with your OpenAI API key

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=data['prompt'],
        max_tokens=150
    )
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)  # Run the Flask app on port 5000
