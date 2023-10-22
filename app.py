from flask import Flask, render_template, jsonify, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    link = request.form.get['link']
    # Do something with the link value
    return ('message: Link submitted successfully')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Assuming you're extracting some data from the submitted form
#     url = request.form['link']

#     # Process the data
#     # Example: 
#     message = "Received link: " + url

#     # Return the result as JSON
#     return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)