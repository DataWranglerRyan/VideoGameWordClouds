import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


class Review(object):
    def __init__(self):
        self.game = ''
        self.rating = 0
        self.review = ''
        self.author = ''
        self.title = ''
        self.date = ''

    def get_word_count(self):
        wordcloud = WordCloud().generate(self.review)

        # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


