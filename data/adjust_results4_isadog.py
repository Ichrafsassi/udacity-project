#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ichraf Sassi
# DATE CREATED: August 30, 2026
# REVISED DATE: August 30, 2026
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file.
#
##

# TODO 4: Define adjust_results4_isadog function below

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog'.
 
    Parameters:
        results_dic - Results Dictionary, key = filename, value = list
          index 0 = pet image label (string)
          index 1 = classifier label (string)
          index 2 = 1/0 (int) 1 = labels match, 0 = no match
        dogfile - text file with all dog names (one breed per line)
 
    Returns:
        None - results_dic is mutable so no return needed.
    """
    dognames_dic = {}
 
    with open(dogfile, "r") as infile:
        for line in infile:
            line = line.rstrip("\n")
            if line not in dognames_dic:
                dognames_dic[line] = 1
            else:
                print("** Warning: duplicate dognames", line)
 
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
 
        # Pet label is-a-dog?
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0
 
        # Classifier label can contain several comma-separated terms --
        # if ANY of them is a known dog name, the classifier said "dog".
        classifier_is_dog = 0
        for term in classifier_label.split(","):
            if term.strip() in dognames_dic:
                classifier_is_dog = 1
                break
 
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
 