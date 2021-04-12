#!/usr/bin/env python3





from measures import Measures;

from execution import Execution;


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





class Logger:
  def __init__(this, fileName):
    f= open("guru99.txt","w+")
    




main();