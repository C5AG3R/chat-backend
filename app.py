from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hardcoded API Key and Assistant ID
API_KEY = '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'
ASSISTANT_ID = 'asst_Hju9RyyxzaWjGxRihoc9GDta'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    # Make a request to the assistant API using the assistant ID and API Key
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "assistant_id": ASSISTANT_ID,
        "message": message
    }
    
    response = requests.post('https://api.your-assistant.com/chat', headers=headers, json=payload)

    if response.status_code == 200:
        assistant_response = response.json().get('response')
    else:
        assistant_response = "There was an issue with your request."

    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
