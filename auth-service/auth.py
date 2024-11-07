from flask import Flask, request, jsonify
from flask_cors import CORS  # เพิ่มการนำเข้า CORS

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุก request

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'password':
        return jsonify({'token': 'fake-jwt-token'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)