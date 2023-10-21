from articletotext import article_text
from transformers import pipeline

classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)

passage = (article)

model_outputs = classifier(passage)

print(model_outputs[0])
