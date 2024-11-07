from flask import Flask, jsonify, request
from flask_cors import CORS  # เพิ่มการนำเข้า CORS
import psycopg2
import redis


app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุก request

@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Data from Backend Service'})

def get_db_connection():
    conn = psycopg2.connect(host='postgres-db',  # ชื่อ container ของ PostgreSQL
                            database='microservice_db',
                            user='user',
                            password='password')
    return conn

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'User added successfully'})

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "username": row[1],
            "password": row[2]  # แปลง tuple เป็น dictionary
        })
    cur.close()
    conn.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)