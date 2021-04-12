#!/usr/bin/env python3

import os

from datetime import datetime

from measures import Measures;

from execution import Execution;


def main():
  dateNow = datetime.now();
  dateNowFormated = dateNow.strftime('%Y-%m-%d %H:%M:%S')
  print('Start at: ' + dateNowFormated);
  
  dirResutsName = dateNow.strftime('%Y-%m-%d_%H:%M');
  dirName = './results/' + dirResutsName;
  
  try:
    os.mkdir(dirName);
    print("Directory " , dirName ,  " Created ") ;
  except:
    print("Directory " , dirName ,  " create error");
    
  planilhaDeCorpusTreino = open("./corpus.tsv", "r");
  lines = planilhaDeCorpusTreino.readlines();

  lines.pop(0);
  interationLogFile = Logger(dirName + '/interation_L01_I01.txt');
  bateryLogFile = Logger(dirName + '/batery_tests.txt');
  # learFactorLogFile = Logger(dirName + '/learFactor_tests.txt');
  # resumeLogFile = Logger(dirName + '/resume_tests.txt');
  
  learnFactor = 0.001;
  learFactorPass = 0.02;
  learnFactorMax = 0.3;
  while learnFactor < learnFactorMax:
    for index in range(10):
      accuracy, precision, recall, f1_score = newInteration(lines, learnFactor, interationLogFile);
      bateryTestsString = (str(learnFactor) + "\t" + str(index) + "\t" + str(accuracy) + "\t" 
        + str(precision) + "\t" + str(recall) + "\t" + str(f1_score));
      bateryLogFile.write(bateryTestsString);
    learnFactor += learFactorPass;
  
  interationLogFile.close();
  bateryLogFile.close();
  # learFactorLogFile.close();
  # resumeLogFile.close();

  
  

def newInteration(lines, learnFactor, logger):
  execution = Execution(learnFactor, logger);

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
        + '% ' + 'recall: ' + str(recall) + '% ' + 'f1_score: ' + str(f1_score) + '%');
  
  return accuracy, precision, recall, f1_score;




class Logger:
  def __init__(this, fileName):
    this.file = open(fileName,"w+");
  def write(this, line):
    this.file.write(line + '\n');
  def close(this):
    this.file.close();
  




main();