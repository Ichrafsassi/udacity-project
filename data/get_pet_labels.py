#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Ichraf Sassi
# DATE CREATED: August 30, 2026
# REVISED DATE: August 30, 2026
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##

# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files.
 
    Parameters:
        image_dir - The (full) path to the folder of images (string)
 
    Returns:
        results_dic - Dictionary with 'key' = image filename and 'value' as a
        List. The list contains the following item:
            index 0 = pet image label (string)
    """
    results_dic = {}
 
    filenames = listdir(image_dir)
 
    for filename in filenames:
        # Skip hidden files (e.g. .DS_Store)
        if filename[0] != ".":
            pet_label = filename.lower()
            pet_label = pet_label.split("_")
            # drop the trailing numeric/extension token (e.g. '01141.jpg')
            pet_label = " ".join(pet_label[:-1])
            pet_label = pet_label.strip()
 
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Key=", filename,
                      "already exists in results_dic with value =",
                      results_dic[filename])
 
    return results_dic