from flask import Flask

app = Flask(__name__)

# POST = to receive data
# get = to send data only

@app.route('/')
def home():
    return 'Hello World'

app.run(port=5000)