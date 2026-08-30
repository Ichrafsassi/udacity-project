#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check_images.py
#
# PROGRAMMER: Ichraf Sassi
# DATE CREATED: August 31, 2026
# PURPOSE: Classify pet images using a pretrained CNN model, compare these
#          classifications to the true identity of the pets in the images,
#          and summarize how well the CNN performed.
#
# Usage: python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##
# from time import time, sleep

# from get_input_args import get_input_args
# from get_pet_labels import get_pet_labels
# from classify_images import classify_images
# from adjust_results4_isadog import adjust_results4_isadog
# from calculates_results_stats import calculates_results_stats
# from print_results import print_results


# def classify_images(images_dir, results_dic, model):
#     """
#     Creates classifier labels with classifier function, compares pet labels
#     to the classifier labels, and adds the classifier label and the
#     comparison of the labels to the results dictionary using the extend
#     function.
 
#     Parameters:
#         images_dir - path to folder of images to classify (string)
#         results_dic - Results Dictionary, key = filename, value = list
#         model - CNN model architecture: resnet, alexnet, or vgg (string)
 
#     Returns:
#         None - results_dic is mutable so no return needed.
#     """
#     for key in results_dic:
#         # classifier() already returns the FULL label string.
#         # NOTE: do NOT slice with [0] -- that was the bug (it grabbed only
#         # the first character of the string, e.g. "Great Dane" -> "G").
#         classifier_label = classifier(images_dir + key, model)
 
#         # Format the classifier label
#         classifier_label = classifier_label.lower().strip()
 
#         # Pet label is a single term; classifier_label can be several
#         # comma-separated synonyms (e.g. "beagle, walker hound"). Split on
#         # comma and compare the pet label against each individual term so a
#         # match doesn't depend on substring luck (e.g. "pug" inside "pugnacious").
#         classifier_terms = [term.strip() for term in classifier_label.split(",")]
#         pet_label = results_dic[key][0]
 
#         if pet_label in classifier_terms:
#             results_dic[key].extend([classifier_label, 1])
#         else:
#             results_dic[key].extend([classifier_label, 0])


from classifier import classifier
 
 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels
    to the classifier labels, and adds the classifier label and the
    comparison of the labels to the results dictionary using the extend
    function.
 
    Parameters:
        images_dir - path to folder of images to classify (string)
        results_dic - Results Dictionary, key = filename, value = list
        model - CNN model architecture: resnet, alexnet, or vgg (string)
 
    Returns:
        None - results_dic is mutable so no return needed.
    """
    for key in results_dic:
        # classifier() already returns the FULL label string.
        # NOTE: do NOT slice with [0] -- that was the bug (it grabbed only
        # the first character of the string, e.g. "Great Dane" -> "G").
        classifier_label = classifier(images_dir + key, model)
 
        # Format the classifier label
        classifier_label = classifier_label.lower().strip()
 
        # Pet label is a single term; classifier_label can be several
        # comma-separated synonyms (e.g. "beagle, walker hound"). Split on
        # comma and compare the pet label against each individual term so a
        # match doesn't depend on substring luck (e.g. "pug" inside "pugnacious").
        classifier_terms = [term.strip() for term in classifier_label.split(",")]
        pet_label = results_dic[key][0]
 
        if pet_label in classifier_terms:
            results_dic[key].extend([classifier_label, 1])
        else:
            results_dic[key].extend([classifier_label, 0])
 