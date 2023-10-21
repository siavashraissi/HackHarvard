import newspaper

# Step 3: Create a Article object using the newspaper module and pass the website link as a parameter
article = newspaper.Article(url='https://www.cnn.com/2023/10/20/us/las-vegas-police-officer-casino-heists-cec/index.html')

# Step 4: Download the article using the download() method of the Article object
article.download()

# Step 5: Parse the article using the parse() method of the Article object
article.parse()

# Step 6: Extract the main article content using the text attribute of the Article object
article_text = article.text