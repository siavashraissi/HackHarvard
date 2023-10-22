from flask import Flask, render_template
from sentencegen import generate_sentence_with_emotion

app = Flask(__name__)

@app.route('/')
def home():
    # add function later to generate new article
    return render_template('index.html', new_article=new_article, emotion=emotion)

if __name__ == '__main__':
    app.run(debug=True)
