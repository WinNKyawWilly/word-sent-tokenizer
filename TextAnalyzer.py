import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk.data
import time 


class TextAnalyzer:
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt_tab')
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """Clean by remove speical character and  normalizing"""
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = ' '.join(text.split())
        return text
    
    def tokenize_sentence(self, text):
        """Tokenize text into sentence"""
        PunktSentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sent_tokenize = PunktSentenceTokenizer.tokenize
        text = sent_tokenize(text)
        return text
    
    def tokenize_word(self, text):
        """Tokenize text into words"""
        text = word_tokenize(text)
        text = [word for word in text if word not in self.stop_words]
        return text

    def word_frequency(self, text, n=10):
        """Count word frequency"""
        counter = Counter(text)
        return counter.most_common(n)
    
    def get_analysis(self, text):
        sent_text = ' '.join(re.sub(r'\d+', '', text.lower()).split())
        
        text = self.clean_text(text)
        with open('nltk/clean_text.txt', 'w') as file:
            file.write(text)
        
        sentences = self.tokenize_sentence(sent_text)
        with open('nltk/sentences.txt', 'w') as file:
            for sentence in sentences:
                sentence = re.sub(r'[^\w\s]', '', sentence)
                file.write(sentence + '\n')

        words = self.tokenize_word(text)
        with open('nltk/words.txt', 'w') as file:
            for word in words:
                file.write(word + '\n')

        word_freq = self.word_frequency(words)
        with open('nltk/word_freq.txt', 'w') as file:
            for word, freq in word_freq:
                file.write(f'{word}: {freq}\n')
        return sentences, words, word_freq

### Main ###

if __name__ == "__main__":
    #import text file
    with open('alice29.txt', 'r') as file:
        text = file.read()
    
    startTime = time.time()

    text_analyzer = TextAnalyzer()
    sentences, words, word_freq = text_analyzer.get_analysis(text)

    endTime = time.time()

    ## Calculate time taken
    with open('nltk/time.txt', 'w') as file:
        file.write(f"Time taken: {endTime - startTime} seconds")
    print(f"Time taken: {endTime - startTime} seconds")
    
