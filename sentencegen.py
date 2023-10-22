import openai
import json
from transformers import pipeline
import newspaper

openai.api_key = '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'


def convertArticleText(link):
    article = newspaper.Article(url=link)

    article.download()

    article.parse()

    article_text = article.text

    return(article_text)


def extract_features(emotions_dict):
    with open(emotions_dict) as f:
        data = json.load(f)
    score_message = 'The scores for the intensity of each emotion\'s level, separated by \';\' are: '
    for i, emotion in enumerate(data):
        score_message += f'{emotion}: {data[emotion]}'
        if i == len(data) - 1:
            score_message += '.'
        else:
            score_message += '; '
    return(score_message)
    

def generate_sentence_with_emotion(original_sentence, score_message):
    prompt = f'''The following in quotes is a news article: \'{original_sentence}\'. 
    
    {score_message} 

    Rewrite this article with a \'neutral\' score of .6. Only include the rewritten article in your response, with no other comments or information. '
    '''

    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=30
    )

    rewritten_sentence = response.choices[0].text.strip()
    return rewritten_sentence


# HuggingFace Roberta Classifier
classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)

# temporary link
passage = convertArticleText(link="https://www.cnn.com/2023/10/20/opinions/israel-gaza-biden-ukraine-russia-mark/index.html")

model_outputs = classifier(passage, truncation=True, padding=True, max_length=512)

article = convertArticleText("https://www.cnn.com/2023/10/20/opinions/israel-gaza-biden-ukraine-russia-mark/index.html")
score_message = extract_features("emotions_dict.json")
new_article = generate_sentence_with_emotion(article, score_message)
