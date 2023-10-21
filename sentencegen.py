import openai
import json

openai.api_key = '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'


def extract_features(emotions_file):
    with open(emotions_file, 'r') as f:
        emotions = json.load(f)
    features = []
    for emotion in emotions.values():
        features.append(emotion)
    print(emotions)
    return features
    

# def generate_sentence_with_emotion(original_sentence, emotion="happy"):
#     prompt = f"Turn this sentence {original_sentence} into a {emotion} sentence:\n\nOriginal Sentence: {original_sentence}\nEmotion: {emotion}\nRewritten Sentence:"

#     response = openai.Completion.create(
#         engine="text-davinci-002",  # Choose the appropriate engine
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=10
#     )

#     rewritten_sentence = response.choices[0].text.strip()
#     return rewritten_sentence

# Example usage:
# original_sentence = "I love programming"
# rewritten_sentence = generate_sentence_with_emotion(original_sentence, emotion="happy")
# print("Original Sentence:", original_sentence)
# print("Rewritten Sentence:", rewritten_sentence)


features1 = extract_features("C:/Users/raiss/Downloads/example_1.json")
print(features1)