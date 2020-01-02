# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/location/cars/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    emptySlots = 1
    response = {}

    # For debugging
    print(f" {emptySlots} free slot(s)")

    response["MESSAGE"] = f"{emptySlots} free slot(s)"

    # Return the response in json format
    return jsonify(response)

@app.route('/location/cars/', methods=['POST'])
def post_something():
    param = request.form.get('image')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Image sent for processing",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no image found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1> Welcome to Gorrilla !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)