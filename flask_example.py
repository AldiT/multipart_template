"""
Simple example for multipart processing © Aldi Topalli
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    username = request.args.get('username')
    if request.method == 'POST':#
        f = request.files['file']
        #do some arbitrary processing

    ## Maybe get some other parameters using requests
    
    #### Question
    ## How to reproduce this simple multipart processing in an OpenFaaS function?
    return "File processed successfully"


if __name__ == '__main__':
    app.run(debug=True)
