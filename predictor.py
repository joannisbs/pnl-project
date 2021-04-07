import re
import nltk
import math
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords as NltkStopWords
from string import punctuation



class FinancialPoliticalPredictor:
  _globalListOfTypesAndWeights = {};
  _defaultPrimaryAdjust = 0;
  
  def __init__(this):
    this.memory = Memory();
  
  
  def training(this, discurso, result):
    tokens = this.__getTokens(discurso);
    sentences = this.__getSentences(discurso);
    types = set(tokens);
    TFIDFMatrix = this.__computeTF_IDF(types, sentences);
    predict = this.__predict(TFIDFMatrix, sentences);
    print(predict)
    # print(len(set(tokens)))
    # print(len(set(tokens)) / len(tokens))
    
    
  def __getTokens(this, text):
    # Obtendo os tokens do discurso
    tokens = word_tokenize(text);
    # Retirando as StopWords e a pontuação
    stopwords = set(NltkStopWords.words('portuguese') + list(punctuation));
    tokens = [word for word in tokens if not word in stopwords];
    # Deixando em "lower" e selecionando apenas "alpha" caracteres
    tokens = [tokens.lower() for tokens in tokens if tokens.isalpha()];
    return tokens;
  
  def __getSentences(this, text):
    sentences = sent_tokenize(text);
    sentencesFormated = [];
    for sent in sentences:
      tokens = word_tokenize(sent);
      stopwords = set(NltkStopWords.words('portuguese') + list(punctuation));
      tokens = [word for word in tokens if not word in stopwords];
      tokens = [tokens.lower() for tokens in tokens if tokens.isalpha()];
      sentencesFormated.append(" ".join(tokens));
    return sentencesFormated;
  
  def __computeTF_IDF(this, types, sentences):
    TfIdfObjectMatrix = {};
    for word in types:
      TfIdfList = {}
      idfValue = this.__computeIDF(word, sentences)
      for count, sent in enumerate(sentences):
        tfValue = this.__computeTf(word, sent);
        TfIdfList[count] = idfValue * tfValue;
      TfIdfObjectMatrix[word]=TfIdfList;
    return TfIdfObjectMatrix;
  
  def __computeTf(this, word, sentence):
    count = len(re.findall(word, sentence))
    tokens = this.__getTokens(sentence);
    tfValue = float(count)/float(len(tokens));
    return tfValue;
  
  def __computeIDF(this, word, sentences):
    count = 0;
    for sent in sentences:
      isOccurred = len(re.findall(word, sent)) > 0;
      if isOccurred: 
        count = count + 1;
      
    numSentences = len(sentences);
    idf = math.log10(float(numSentences)/ float(count));
    return idf;
  
  def __predict(this, tfdif, sentences):
    global _defaultPrimaryAdjust;
    
    weights = 0;
    for count, sent in enumerate(sentences):
      tokens = this.__getTokens(sent);
      words = set(tokens);
      weightOfSentence = 0;
      for word in words:
        peso = this.memory.getWeightToken(word);
        weightOfWord = tfdif[word][count] * peso;
        weightOfSentence = weightOfSentence + weightOfWord;
      weights = weights + weightOfSentence;
      
    return weights + this.memory.getDefaultSistemicCorrection();
        
        
       
    
    
    
  
  
# word: peso, -


class Memory:
  def __init__(this):
    this._weights = {};
    this._defaultSistemicCorrection = 0;
    
  def setWeightToken(this, token, value):
    this._weights[token] = value;
    
  def getWeightToken(this, token):
    if token in this._weights:
      return this._weights[token];
    this._weights[token] = 1;
    return 1;
  
  def setDefaultSistemicCorrection(this, value):
    this._defaultSistemicCorrection = value;
    
  def getDefaultSistemicCorrection(this):
    return this._defaultSistemicCorrection;
    
    