# Classify Pet Images — Udacity AIPND Project

## Overview
This project uses a pretrained CNN (VGG, ResNet, or AlexNet) to classify pet images and determine:
1. Whether each image is of a dog or not a dog
2. If it is a dog, whether the breed is classified correctly
3. Which of the three CNN architectures performs "best"
4. The runtime trade-off between accuracy and speed across architectures

```All files are modified and all TODOs are completed in the `data` folder.```

## Files
- `check_images.py` — main driver program, ties all functions together and times the run
- `get_input_args.py` — parses command line arguments (`--dir`, `--arch`, `--dogfile`)
- `get_pet_labels.py` — builds pet image labels from filenames
- `classify_images.py` — runs the classifier and compares its label to the pet label
- `adjust_results4_isadog.py` — determines whether each label is/is-not a dog, using `dognames.txt`
- `calculates_results_stats.py` — computes counts and percentages from the results
- `print_results.py` — prints the summary and (optionally) misclassified dogs/breeds
- `classifier.py` — provided CNN classifier function (not modified)
- `resnet_pet-images.txt`, `alexnet_pet-images.txt`, `vgg_pet-images.txt` — output of running `check_images.py` with each architecture on the `pet_images/` folder

## How to Run
```
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
```

## Results

| Metric | VGG | ResNet | AlexNet |
|---|---|---|---|
| N Images | 40 | 40 | 40 |
| N Dog Images | 30 | 30 | 30 |
| N Not-Dog Images | 10 | 10 | 10 |
| % Match | 87.5% | 82.5% | 75.0% |
| % Correct Dogs | 100.0% | 100.0% | 100.0% |
| % Correct Breed | 93.3% | 90.0% | 80.0% |
| % Correct Not-a-Dog | 100.0% | 90.0% | 100.0% |
| Runtime | ~19–20s | ~4–5s | ~2–3s |

## Discussion — Objective 4: Time vs. Accuracy Trade-off

VGG took the longest to run (≈19–20 seconds) but delivered the best results across the board — 100% dog/not-dog accuracy and 93.3% breed accuracy. ResNet was dramatically faster (≈4–5 seconds, roughly 4–5x quicker than VGG) but slightly less accurate: 90% breed accuracy and 90% not-dog accuracy (it misclassified one cat as a dog). AlexNet was the fastest of all (≈2–3 seconds) but also the least accurate, with only 80% breed accuracy.

This confirms the general trade-off in this project: more accurate models take longer to run. For this project, where only 40 images were classified, VGG's extra runtime (about 15 seconds more than AlexNet) is a trivial cost for a meaningful accuracy gain — so **VGG is the "best" model** for this task. However, at much larger scale (thousands or millions of images), that same 6–7x runtime difference would become significant, and a faster model like ResNet — which still achieved 100% dog detection — could be the more practical "good enough" choice when speed matters more than the last few points of breed accuracy.

## Conclusion

Given the results above, **VGG** is the best-performing architecture for this task, achieving 100% accuracy on identifying dogs vs. not-dogs and the highest breed classification accuracy (93.3%) of the three architectures tested.
