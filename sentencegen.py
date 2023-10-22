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
    score_message = 'The scores for the intensity of each emotion\'s level, separated by \';\' are: '
    for i, emotion in enumerate(emotions_dict):
        score_message += f'{emotion}: {emotions_dict[emotion]}'
        if i == len(emotions_dict) - 1:
            score_message += '.'
        else:
            score_message += '; '
    return(score_message)
    

def generate_sentence_with_emotion(original_sentence, score_message):
    prompt = f'''The following in quotes is a news article: \'{original_sentence}\'. 
    
    {score_message} 

    Rewrite this article with the same scores for each emotion, but with a \'neutral\' score of .6. Only include the rewritten article in your response, with no other comments or information.'
    '''

    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=500
    )

    rewritten_sentence = response.choices[0].text.strip()
    return rewritten_sentence


def robertaClassifier(passage):
    # HuggingFace Roberta Classifier
    classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)

    # generate emotion scores
    model_outputs = classifier(passage, truncation=True, padding=True, max_length=512)

    new_dict = {}
    for item in model_outputs[0]:
        new_dict[item['label']] = item['score']
    # new_dict['neutral'] = 0.6

    return new_dict


# temporary link
passage = convertArticleText("https://www.cnn.com/2023/10/20/opinions/israel-gaza-biden-ukraine-russia-mark/index.html")

# extract emotion scores and generate score message
score_message = extract_features(robertaClassifier(passage))
print(score_message)
# new_article = generate_sentence_with_emotion(passage, score_message)

# print(new_article)