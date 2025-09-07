from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify(message="Hello from Flask backend (deployed by Ansible)!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port={{ flask_port }})
