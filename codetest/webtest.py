from flask import Flask, request,  jsonify
import requests

# 发送GET请求
response = requests.get('https://api.github.com')

# 查看响应内容
print(response.status_code)
print(response.json())



app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api', methods=['GET'])
def api():
    data = {'message': 'Hello, API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)