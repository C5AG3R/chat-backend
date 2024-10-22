from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    # Replace this with your assistant's response logic
    response = f"You said: {message}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0')