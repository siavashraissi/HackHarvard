from transformers import pipeline
import newspaper

def convertArticleText(link):
    article = newspaper.Article(url=link)

    article.download()

    article.parse()

    article_text = article.text

    return(article_text)

classifier = pipeline(task="sentiment-analysis", model="SamLowe/roberta-base-go_emotions", top_k=None)

passage = convertArticleText(link="https://www.cnn.com/2023/10/20/opinions/israel-gaza-biden-ukraine-russia-mark/index.html")

model_outputs = classifier(passage, truncation=True, padding=True, max_length=512)

print(model_outputs[0][0])
