#!/usr/bin/env python3

class Memory:
  def __init__(this):
    this._weights = {};
    this._defaultSistemicCorrection = 0;
    
  def setWeightToken(this, token, value):
    this._weights[token] = value;
    
  def getWeightToken(this, token):
    if token in this._weights:
      return this._weights[token];
    this._weights[token] = 0;
    return 0;
  
  def setDefaultSistemicCorrection(this, value):
    this._defaultSistemicCorrection = value;
    
  def getDefaultSistemicCorrection(this):
    return this._defaultSistemicCorrection;
  
  def printWeghts(this):
    print(this._weights);
    