import numpy as np
import PIL
import pandas as pd
from PIL import ImageFont
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import mysql.connector as sql



config = {
    'user': 'root',
    'password': 'root',
    'host': 'Randy',
    'port': '3307',
    'database' : 'test'
}

def cloudWord():

    query = """ 
    SELECT TEXT FROM TWEETS_TWEET;
    """

    cnn  = sql.connect(**config)
    cursor = cnn.cursor()
    cursor.execute(query)
    data =  cursor.fetchall()
    text = ','.join(map(str,data))
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("wordClound.png")


if __name__ == "__main__":
    cloudWord()
