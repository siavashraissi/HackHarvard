from flask import Flask, render_template, jsonify, request

@app.route('/submit', methods=['POST'])
def submit():
    # Assuming you're extracting some data from the submitted form
    url = request.form.get('link')

    # Process the data
    # Example: 
    message = "Received link: " + url

    # Return the result as JSON
    return jsonify({'message': message})
