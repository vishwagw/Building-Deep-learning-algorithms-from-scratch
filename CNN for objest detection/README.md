# Convolutional Nerual Network for object detection

This project is to build, train and evaluate a CNN from scratch that can be used for object detection.

1. Convolutional Neural networks (CNN):
Convolutional neural networks are majorly used in object detection and classification processes. t excels at recognizing patterns in images due to its unique architecture that includes convolutional layers, which use filters to extract features from the input image. These algrithms are well suited for analyzing visual input data due to previously mentioned features. 

CNN architecture is inspired by the connectivity patterns of the human brain -- in particular, the visual cortex, which plays an essential role in perceiving and processing visual stimuli.

2. Algorithm structure:
This deep learning algorithm has following algorithmic structure.
* import dataset and library
* preprocessin loaded data
* Re-shaping data for training
* Training the model
* evaluating the model

3. Keras Sequential model:
In this algorithm, we are using a Sequential model for training.
Sequential model is suitable for plainstack of layers where each layer has exactly one input tensor and one output sensor. 

The sequential API allows you to create models layer-by-layer for most problems. It is limited in that it does not allow you to create models that share layers or have multiple inputs or outputs.

The functional API in Keras is an alternate way of creating models that offers a lot more flexibility, including creating more complex models.

he Sequential API is a framework for creating models based on instances of the sequential() class. The model has one input variable, a hidden layer with two neurons, and an output layer with one binary output. Additional layers can be created and added to the model.

4. Conclusion:
The major evaluation is that this Deep learning model as a 99% accuracy. 