from flask import Flask, render_template
from sentencegen import generate_sentence_with_emotion

app = Flask(__name__)

@app.route('/')
def index():
    new_article = generate_sentence_with_emotion()
    return render_template('index.html', new_article=new_article)

if __name__ == '__main__':
    app.run(debug=True)
