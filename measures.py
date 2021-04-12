#!/usr/bin/env python3

import math

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
