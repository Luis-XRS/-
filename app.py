from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "计算机网络大作业"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    
