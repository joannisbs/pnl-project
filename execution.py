#!/usr/bin/env python3

from predictor import FinancialPoliticalPredictor;
from utils import Utils;

import math



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
