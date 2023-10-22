from flask import Flask, render_template, jsonify, request, url_for
from sentencegen import convertArticleText, extract_features, generate_sentence_with_emotion, robertaClassifier

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        linkurl = request.form['link']
        # if request.form['submitbutton'] == 'Submit':
            # link = request.form.get('link')
            # Do something with the link value
        passage = convertArticleText(linkurl)
        new_article = generate_sentence_with_emotion(passage, robertaClassifier(passage))
        return(new_article)

    else:
        return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     link = request.form['submitlink']
#     # Do something with the link value
#     return jsonify({'message': 'Link submitted successfully'})

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