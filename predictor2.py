#!/usr/bin/env python3
import re
import nltk
import math
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords as NltkStopWords
from string import punctuation

from memory import Memory;

class FinancialPoliticalPredictor:

  def __init__(this, learnFactor):
    this.learnFactor = learnFactor;
    this.memory = Memory();
  
  def training(this, discurso, result):
    tokens = this.__getTokens(discurso);
    sentences = this.__getSentences(discurso);
    types = set(tokens);
    TFIDFMatrix = this.__computeTF_IDF(types, sentences);
    predict = this.__computePredict(TFIDFMatrix, sentences);
    this.__computeCorrection(predict, result, TFIDFMatrix, types);
    return predict;
  
  def testing(this, discurso):
    tokens = this.__getTokens(discurso);
    sentences = this.__getSentences(discurso);
    types = set(tokens);
    TFIDFMatrix = this.__computeTF_IDF(types, sentences);
    predict = this.__computePredict(TFIDFMatrix, sentences);
    
    this.lastPredict = predict;
    this.lastTFIDFMatrix = TFIDFMatrix;
    this.lastTypes = types;
    
    return predict;
  
  def correctLastTest(this, result):
    this.__computeCorrection(this.lastPredict, result, this.lastTFIDFMatrix, this.lastTypes);

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
    if len(tokens) == 0:
      return 0;
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
  
  def __computePredict(this, tfdifs, sentences):
    weights = 0;
    for count, sent in enumerate(sentences):
      tokens = this.__getTokens(sent);
      words = set(tokens);
      weightOfSentence = 0;
      for word in words:
        peso = this.memory.getWeightToken(word);
        weightOfWord = tfdifs[word][count] * peso;
        weightOfSentence = weightOfSentence + weightOfWord;
      weights = weights + weightOfSentence;
      
    return weights + this.memory.getDefaultSistemicCorrection();
        
  def __computeCorrection(this, predict, result, tfdifs, types):
    err = result - predict;
    sistemicFactor = this.learnFactor * err;
    oldSistemicErr = this.memory.getDefaultSistemicCorrection();
    newSistemicErr = oldSistemicErr + sistemicFactor;
    this.memory.setDefaultSistemicCorrection(newSistemicErr);
    for word in types:
      peso = this.memory.getWeightToken(word);
      factor = this.learnFactor * err;
      newPeso = peso + factor;
      this.memory.setWeightToken(word, newPeso);
  
