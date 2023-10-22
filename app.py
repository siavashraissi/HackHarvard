from flask import Flask, render_template, url_for
from sentencegen import generate_sentence_with_emotion

app = Flask(__name__)

@app.route('/')
def index():
    # return("TEST")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
