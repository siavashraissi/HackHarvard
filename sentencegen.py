import openai
import json

openai.api_key = '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'


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
    print(score_message)
    

def generate_sentence_with_emotion(original_sentence, score_message):
    prompt = f'''The following in quotes is a news article: \'{original_sentence}\'. 
    
    {score_message} 

    Rewrite this article with a \'neutral\' score of .6.'
    '''

    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=30
    )

    rewritten_sentence = response.choices[0].text.strip()
    return rewritten_sentence

# Example usage:
# original_sentence = "I love programming"
# rewritten_sentence = generate_sentence_with_emotion(original_sentence, emotion="happy")
# print("Original Sentence:", original_sentence)
# print("Rewritten Sentence:", rewritten_sentence)


features1 = extract_features("C:/Users/raiss/Downloads/example_1.json")
# print(features1)