#!/usr/bin/env python3

from random import randint

class Utils:
  def calcTestLineAleatory():
    numberAleatory = randint(0,99);
    if (numberAleatory % 12) % 4 == 1: 
      return True;
    return False;
  
  def formatLine(line):
    columns = line.split("\t");
    identifier = columns[0];
    file = open("./texts/" + identifier);
    text = file.read();
    result = columns[3];
    resultFormated = float(result.replace(',','.'));
    return text, resultFormated, identifier;
  