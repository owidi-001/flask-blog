# app.py
from flask import Flask ,render_template

app = Flask(__name__) # name for the Flask app (refer to output)

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return render_template('index.html')

# running the server
app.run(debug = True) # to allow for debugging and auto-reload