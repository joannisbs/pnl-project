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
  bateryLogFile = Logger(dirName + '/batery_tests.tsv');
  learFactorLogFile = Logger(dirName + '/learFactor_tests.tsv');
  # resumeLogFile = Logger(dirName + '/resume_tests.txt');
  
  bateryTestsString = ("Taxa_aprendizado" + "\t" + "Interação" + "\t" + "Acuracia" + "\t" 
        + "Precisão" + "\t" + "Recall" + "\t" + "F1_score");
  bateryLogFile.write(bateryTestsString);
  
  learnTestsString = ("learnFactor" + "\t" + "acuracia_media" + "\t" 
        + "acuracia_dispersion" + "\t" + "acuracia_defaultError" + "\t" + "precision_media" + "\t" 
        + "precision_dispersion" + "\t" + "precision_defaultError" + "\t" + "recall_media" + "\t" 
        + "recall_dispersion" + "\t" + "recall_defaultError" + "\t" + "f1_score_media" + "\t" 
        + "f1_score_dispersion" + "\t" + "f1_score_defaultError");
    
  learFactorLogFile.write(learnTestsString);
      
  learnFactor = 0.1;
  learFactorPass = 0.05;
  learnFactorMax = 0.4;
  
  while learnFactor < learnFactorMax:
    accuracyValues = [];
    precisionValues = [];
    recallValues = [];
    scoresValues = [];
    
    
    for index in range(10):
      print( 'learn :' + str(learnFactor) + ' interation: ' + str(index));
      accuracy, precision, recall, f1_score = newInteration(lines, learnFactor, interationLogFile);
      bateryTestsString = (str(learnFactor) + "\t" + str(index) + "\t" + str(accuracy) + "\t" 
        + str(precision) + "\t" + str(recall) + "\t" + str(f1_score));
      bateryLogFile.write(bateryTestsString);
      
      accuracyValues.append(accuracy);
      precisionValues.append(precision);
      recallValues.append(recall);
      scoresValues.append(f1_score);

    acuracia_media, acuracia_dispersion, acuracia_defaultError = Measures.valueStatistic(accuracyValues);
    
    precision_media, precision_dispersion, precision_defaultError = Measures.valueStatistic(precisionValues);
    
    recall_media, recall_dispersion, recall_defaultError = Measures.valueStatistic(recallValues);
    
    f1_score_media, f1_score_dispersion, f1_score_defaultError = Measures.valueStatistic(scoresValues);
    
    learnTestsString = (str(learnFactor) + "\t" + str(acuracia_media) + "\t" 
        + str(acuracia_dispersion) + "\t" + str(acuracia_defaultError) + "\t" + str(precision_media) + "\t" 
        + str(precision_dispersion) + "\t" + str(precision_defaultError) + "\t" + str(recall_media) + "\t" 
        + str(recall_dispersion) + "\t" + str(recall_defaultError) + "\t" + str(f1_score_media) + "\t" 
        + str(f1_score_dispersion) + "\t" + str(f1_score_defaultError));
    
    learFactorLogFile.write(learnTestsString);
    learnFactor += learFactorPass;
    
    
  interationLogFile.close();
  bateryLogFile.close();
  learFactorLogFile.close();
  
  dateNow2 = datetime.now();
  passTime = dateNow - dateNow2;
  passTimeInSec = passTime.total_seconds();
  passDays    = divmod(passTimeInSec, 86400);    
  passHours   = divmod(days[1], 3600);               
  passMinutes = divmod(hours[1], 60);                
  passSeconds = divmod(minutes[1], 1);   
  print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
  print('Runtime, calculate at %d days, %d hours, %d minutes and %d seconds' % 
    (passDays[0], passHours[0], passMinutes[0], passSeconds[0]))
  # resumeLogFile.close();

  
  

def newInteration(lines, learnFactor, logger):
  execution = Execution(learnFactor, logger);

  linesTraining, linesTeste = execution.separateTrainingTestesLines(lines);


  execution.training(linesTraining);
  results = execution.testing(linesTeste);
  print(results);

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