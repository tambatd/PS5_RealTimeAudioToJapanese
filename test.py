from flask import Flask
from threading import Thread

app = Flask(__name__)

def my_function():
    while True:
        # Your code here
        print("Running my function...")

# Create a separate thread for running the function
thread = Thread(target=my_function)
thread.start()

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
