#!/usr/bin/env python3



from predictor import FinancialPoliticalPredictor;

import math



def main():


  planilhaDeCorpusTreino = open("./corpus.tsv", "r");
  lines = planilhaDeCorpusTreino.readlines();

  lines.pop(0);
  
  execution = Execution();

  linesTraining, linesTeste = execution.separateTrainingTestesLines(lines);


  execution.training(linesTraining);
  results = execution.testing(linesTeste);
  # print(results);

  tableResults = Measures.getTableResults(results);
  
  accuracy = Measures.accuracy(tableResults)
  precision = Measures.precision(tableResults)
  recall = Measures.recall(tableResults)
  f1_score = Measures.f1_score(precision, recall)
  
  print('\naccuracy: ' + str(accuracy) + '% ' + 'precision: ' + str(precision) 
        + '% ' + 'recall: ' + str(recall) + '% ' + 'f1_score: ' + str(f1_score) + '%')



class Execution:
  def __init__(this):
    this.fpp = FinancialPoliticalPredictor();
  
  def separateTrainingTestesLines(this, lines):
    linesTraining = [];
    linesTeste = [];
    discursesIdsSorted = [];
    
    print('Mount setup training e tests.');
    
    for line in lines:
      if Utils.calcTestLineAleatory():
        linesTeste.append(line);
        columns = line.split("\t");
        identifier = columns[0];
        discursesIdsSorted.append(identifier)
      else:
        linesTraining.append(line);
        
    print('Setup training test mounted!');
    print('Amount training: '+ str(len(linesTraining)));
    print('Amount testing: '+ str(len(linesTeste)));
    
    print('\nSorted from tests: ' + str(" ".join(discursesIdsSorted)) + '\n')
    
    return linesTraining, linesTeste;
  
  def training(this, linesTraining):
    count = 1;
    for line in linesTraining:
      text, result, identifier = Utils.formatLine(line)
      this.fpp.training(text, result);
      numLinesOfTraining = len(linesTraining);
      percetsProgress = math.floor(100 * (count / numLinesOfTraining))
      print('Training: ' + str(count) + '-' + str(numLinesOfTraining) + '  ---  ' + str(percetsProgress) + '%');
      count += 1;
      
  def testing(this, linesTeste):
    count = 1;
    results = [];
    for line in linesTeste:
      text, result, identifier = Utils.formatLine(line);
      predict = this.fpp.testing(text);
      this.fpp.correctLastTest(result);
      numLinesOfTest = len(linesTeste);
      percetsProgress = math.floor(100 * (count / numLinesOfTest));
      
      isCorrectDirection = predict * result > 0;
      
      resultInteration = {
        "id": identifier,
        "result": result,
        "predict": predict,
        "correct": isCorrectDirection,
      }
      
      results.append(resultInteration);
      
      print('Test: ' + str(count) + '-' + str(numLinesOfTest) + '  ---  ' + str(percetsProgress) + '% --- ' 
            + 'predict: ' + str(math.floor(predict)) + ' result: ' + str(result) + ' correct: ' + str(isCorrectDirection));
      count += 1;
    return results;


from random import randint

class Logger:
  def __init__(this, fileName):
    f= open("guru99.txt","w+")
    

  

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
  
class Measures:
  def getTableResults(results):
    truePositives = 0;
    falsePositives = 0;
    falseNegatives = 0;
    trueNegatives = 0;

    for res in results:
      if res["predict"] >= 0:
        if res["result"] >= 0:
          truePositives += 1;
        else:
          falsePositives +=1;
      else:
        if res["result"] >= 0:
          falseNegatives += 1;
        else:
          trueNegatives +=1;
          
    return { "truePositives": truePositives, "falsePositives": falsePositives, 
            "trueNegatives":trueNegatives, "falseNegatives":falseNegatives};
    
  def accuracy(tableResults):
    truePositives = tableResults["truePositives"];
    falsePositives = tableResults["falsePositives"];
    falseNegatives = tableResults["falseNegatives"];
    trueNegatives = tableResults["trueNegatives"];
    
    accuracyMeasure = (truePositives + trueNegatives) / (
      truePositives + trueNegatives + falseNegatives + trueNegatives);
    
    return math.floor(accuracyMeasure * 100);
  
  def precision(tableResults):
    truePositives = tableResults["truePositives"];
    falsePositives = tableResults["falsePositives"];
    falseNegatives = tableResults["falseNegatives"];
    trueNegatives = tableResults["trueNegatives"];
    
    precisionMeasure = (truePositives) / (truePositives + falsePositives);
    
    return math.floor(precisionMeasure * 100);
  
  def recall(tableResults):
    truePositives = tableResults["truePositives"];
    falsePositives = tableResults["falsePositives"];
    falseNegatives = tableResults["falseNegatives"];
    trueNegatives = tableResults["trueNegatives"];
    
    recallMeasure = (truePositives) / (truePositives + falseNegatives);
    
    return math.floor(recallMeasure * 100);
  
  def f1_score(precision, recall):
    f1Measure = (2 * precision * recall) / (precision + recall)
    return math.floor(f1Measure);



main();