#!/usr/bin/env python3

import math

class Measures:
  def getTableResults(results):
    truePositives = 0;
    falsePositives = 0;
    falseNegatives = 0;
    trueNegatives = 0;

    for res in results:
      if res["predict"] >= 0:   # previsao up
        if res["result"] >= 0:  # result up
          truePositives += 1;
        else:                   # result down
          falsePositives +=1;
      else:                     # previsao down
        if res["result"] >= 0:  # result up
          falseNegatives += 1;
        else:                   # result down
          trueNegatives +=1;
          
    return { "truePositives": truePositives, "falsePositives": falsePositives, 
            "trueNegatives":trueNegatives, "falseNegatives":falseNegatives};
    
  def accuracy(tableResults):
    truePositives = tableResults["truePositives"];
    falsePositives = tableResults["falsePositives"];
    falseNegatives = tableResults["falseNegatives"];
    trueNegatives = tableResults["trueNegatives"];
    
    accuracyMeasure = (truePositives + trueNegatives) / (
      truePositives + falsePositives + falseNegatives + trueNegatives);
    
    # print('acuracia :', truePositives, falsePositives, falseNegatives, trueNegatives )
    
    return math.floor(accuracyMeasure * 100);
  
  def precision(tableResults):
    truePositives = tableResults["truePositives"];
    falsePositives = tableResults["falsePositives"];
    falseNegatives = tableResults["falseNegatives"];
    trueNegatives = tableResults["trueNegatives"];
    
    precisionMeasure = (truePositives) / (truePositives + falsePositives);
    
    # print('precisionMeasure :', truePositives, falsePositives, falseNegatives, trueNegatives )
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

  def valueStatistic(listValues):
    sommationOfValues = 0;
    for value in listValues:
      sommationOfValues += value;
      
    media = sommationOfValues/float(len(listValues));
    
    sumMinimunSqrt = 0;
    for value in listValues:
      sommationOfValues += (math.pow((value - media), 2));
      
    dirpersionSqrt = sommationOfValues/float(len(listValues) - 1);
    
    dispersion = math.pow(dirpersionSqrt, 1/2);
    
    lenSquad = math.pow(len(listValues), 1/2);
    defaultError = dispersion/lenSquad;
    
    return math.floor(media), math.floor(dispersion), math.floor(defaultError);
