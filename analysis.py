import os
from openai import OpenAI


api_key = "Add API key"

client = OpenAI(api_key=api_key)

def sentiment_a(review):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",      #You can use gpt-4 here also
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": f"Analyze the sentiment of the following product review:\n\n{review}"}
        ]
    )

    sentiment = response.choices[0].message.content.strip()
    return sentiment

# Read reviews from the input file
with open(r"/content/sample_data/reviews.txt", "r", encoding="utf-8") as file: 
    reviews = file.readlines()

# Analyze sentiment for each review and write the results to the output file
with open("sentiment_analysis.txt", "w", encoding="utf-8") as file:
    for review in reviews:
        sentiment = sentiment_a(review)
        file.write(f"Review: {review.strip()}\nSentiment: {sentiment}\n\n")

print("Sentiment analysis completed. Results written to sentiment_analysis.txt")
