#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Ichraf Sassi
# DATE CREATED: August 30, 2026
# REVISED DATE: August 30, 2026
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages.
##

# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's
    model architecture to classifying pet images.
 
    Parameters:
        results_dic - Results Dictionary, key = filename, value = list
          index 0 = pet image label (string)
          index 1 = classifier label (string)
          index 2 = 1/0 match
          index 3 = 1/0 pet label is-a-dog
          index 4 = 1/0 classifier label is-a-dog
 
    Returns:
        results_stats_dic - Dictionary of statistics (counts & percentages)
    """
    results_stats_dic = dict()
 
    results_stats_dic["n_images"] = len(results_dic)
 
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
 
    for key in results_dic:
        if results_dic[key][3] == 1:
            n_dogs_img += 1
        else:
            n_notdogs_img += 1
 
        if results_dic[key][2] == 1:
            n_match += 1
 
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            n_correct_dogs += 1
 
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            n_correct_notdogs += 1
 
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            n_correct_breed += 1
 
    results_stats_dic["n_dogs_img"] = n_dogs_img
    results_stats_dic["n_notdogs_img"] = n_notdogs_img
    results_stats_dic["n_match"] = n_match
    results_stats_dic["n_correct_dogs"] = n_correct_dogs
    results_stats_dic["n_correct_notdogs"] = n_correct_notdogs
    results_stats_dic["n_correct_breed"] = n_correct_breed
 
    results_stats_dic["pct_match"] = (n_match / results_stats_dic["n_images"]) * 100
 
    if n_dogs_img > 0:
        results_stats_dic["pct_correct_dogs"] = (n_correct_dogs / n_dogs_img) * 100
        results_stats_dic["pct_correct_breed"] = (n_correct_breed / n_dogs_img) * 100
    else:
        results_stats_dic["pct_correct_dogs"] = 0.0
        results_stats_dic["pct_correct_breed"] = 0.0
 
    if n_notdogs_img > 0:
        results_stats_dic["pct_correct_notdogs"] = (n_correct_notdogs / n_notdogs_img) * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0
 
    return results_stats_dic
 