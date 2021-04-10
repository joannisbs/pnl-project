#!/usr/bin/env python3



from predictor import FinancialPoliticalPredictor;





def main():

  # fpp = FinancialPoliticalPredictor();

  planilhaDeCorpusTreino = open("./corpus.tsv", "r");
  lines = planilhaDeCorpusTreino.readlines();

  lines.pop(0);
  
  execution = Execution();

  linesTraining, linesTeste = execution.separateTrainingTestesLines(lines);


  execution.training(linesTraining);






class Execution:
  def __init__(this):
    this.fpp = FinancialPoliticalPredictor();
  
  def separateTrainingTestesLines(this, lines):
    linesTraining = [];
    linesTeste = [];
    
    for line in lines:
      if Utils.calcTestLineAleatory():
        linesTeste.append(line);
      else:
        linesTraining.append(line)
        
    return linesTraining, linesTeste;
  
  def training(this, linesTraining):
    for line in linesTraining:
      text, result, identifier = Utils.formatLine(line)
      predict = this.fpp.training(text, result);
      print('Discurso: ' + identifier, 'predict: ' + str(predict), 'result: ' + str(result));


from random import randint

class Utils:
  def calcTestLineAleatory():
    numberAleatory = randint(0,99);
    if numberAleatory % 4 == 1: 
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
  
class Measures:
  pass




main();