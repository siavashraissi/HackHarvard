from transformers import pipeline
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

# Load the sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis")

# Function to modify a sentence to make it more neutral
def make_sentence_neutral(sentence, sentiment_threshold=0.7):
    # Get the sentiment score for the input sentence
    sentiment_result = sentiment_analysis(sentence)

    # Extract the sentiment label and score
    sentiment_label = sentiment_result[0]['label']
    sentiment_score = sentiment_result[0]['score']

    # If the sentiment score is below the threshold, consider it neutral
    if sentiment_score < sentiment_threshold:
        return sentence
    else:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)

        # Replace non-neutral words with synonyms
        neutral_words = []
        for word in words:
            synsets = wordnet.synsets(word)
            if synsets:
                neutral_words.append(synsets[0].lemmas()[0].name())
            else:
                neutral_words.append(word)

        neutral_sentence = ' '.join(neutral_words)
        return neutral_sentence

# Example sentence
input_sentence = "The Gaza war is devastating, and there is a lot of misinformation spreading."

# Make the sentence more neutral
neutralized_sentence = make_sentence_neutral(input_sentence)

print("Original Sentence:", input_sentence)
print("Neutralized Sentence:", neutralized_sentence)
