import tweepy
from transformers import pipeline

# Configuration de l'API Twitter
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Récupération des tweets en temps réel sur un sujet spécifique
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Extraction du texte du tweet
        tweet_text = status.text
        
        # Utilisation du modèle BERT pour classifier le sentiment du tweet
        classifier = pipeline('sentiment-analysis')
        result = classifier(tweet_text)[0]
        sentiment = result['label']
        score = result['score']
        
        # Affichage du résultat
        print(f'Tweet : {tweet_text}')
        print(f'Sentiment : {sentiment}')
        print(f'Score : {score}')
        print('-------------------------------------')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = auth, listener=myStreamListener)
myStream.filter(track=['your_topic'])
