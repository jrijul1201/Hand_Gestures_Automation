# Hand Gestures Recognition and Automation (Perceptron and CNN)

Goal is to recognize hand gestures. We've trained the model on our own dataset using *Perceptron* (and *CNN* thereafter). We've included our dataset in the repository itself. In it's present state the model is trained to recognize 7 gestures but can easily be trained for many hand gestures. We have also uploaded the code that we used for capturing the hand and processing it for training the model.

Model gives a high train accuracy: *99.95%* and validation accuracy: *98.81%*

Images in the dataset are of dimension *200 by 200*. But for performance reasons they have been resized to *50 by 50*.

## What's in the Repository

* `captureHand.py` - This program can capture new hand gestures and write them in the specified directory
* `recognizer.py` - This is the main program that uses pretrained model (in the repo) for recognizing hand gestures
* `trainer.py` - This program uses the given dataset to train the Perceptron model
* `modelWeights.h5` - Weights for the Perceptron model
* `trainedModel.json` - JSON format of the model
* `CNN Model` - A directory that contains CNN model implementation for the same recognition purpose (with 4 gestures)

### Sample of Images from the Dataset
* C

![C.jpeg](Sample_Images/C.jpeg)

* Fist

![fist.jpeg](Sample_Images/fist.jpeg)

* Index

![index.jpeg](Sample_Images/index.jpeg)

* L

![L.jpeg](Sample_Images/L.jpeg)

* OK

![ok.jpeg](Sample_Images/ok.jpeg)

* Palm

![palm.jpeg](Sample_Images/palm.jpeg)

* Thumb

![thumb.jpeg](Sample_Images/thumb.jpeg)

## Model Outputs

* Model Summary

![CNNoutput.jpg](Model_Images/summary.JPG)

* Training Output

![PERCEPTRONoutput.jpg](Model_Images/output.JPG)
