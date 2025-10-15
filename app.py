from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory contacts list
contacts = []

@app.route('/')
def home():
    return "Welcome to the Hacktoberfest CRM!"

@app.route('/contacts', methods=['GET'])
def get_contacts():
    """Get the list of contacts."""
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    """Add a new contact."""
    data = request.get_json()
    contacts.append(data)
    return jsonify({'message': 'Contact added successfully!', 'contact': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
