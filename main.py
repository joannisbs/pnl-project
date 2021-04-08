#!/usr/bin/env python3

from predictor import FinancialPoliticalPredictor;

fpp = FinancialPoliticalPredictor();

planilhaDeCorpusTreino = open("./corpus.tsv", "r");
lines = planilhaDeCorpusTreino.readlines();

lines.pop(0);

for line in lines:
  columns = line.split("\t");
  file = open("./texts/" + columns[0]);
  text = file.read();
  result = columns[3];
  resultFormated = float(result.replace(',','.'));
  predict = fpp.training(text, resultFormated);
  print('Discurso: ' + columns[0], 'predict: ' + str(predict), 'result: ' + str(resultFormated));
