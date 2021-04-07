import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords as NltkStopWords
from string import punctuation



class FinancialPoliticalPredictor:
  _globalListOfTypes = [];
  
  
  def training(self, discurso, result):
    # Obtendo os tokens do discurso
    tokens = word_tokenize(discurso)
    # Retirando as StopWords e a pontuação
    stopwords = set(NltkStopWords.words('portuguese') + list(punctuation))
    tokens = [word for word in tokens if not word in stopwords]
    # Deixando em "lower" e selecionando apenas "alpha" caracteres
    tokens = [tokens.lower() for tokens in tokens if tokens.isalpha()]
    print(len(tokens))
    print(len(set(tokens)))
    print(len(set(tokens)) / len(tokens))