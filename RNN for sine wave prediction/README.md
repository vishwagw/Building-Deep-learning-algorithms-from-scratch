In this file, we are going to create a recurrent neural network from the scratch. 
First of all, what is a Recurrenct neural network(RNN)?
Let's assume that we are reading a book. We do not have to reboot our memory or the undersatnding of the language we are reading to understand the meaning of what we read. We will undestand the context of our reading base on previous learnings of the words we read.

But can we apply this same method to create an artificial learning algorithm. RNN are the algorithms that is being used to recreate this function of a narutal human brain.

RNN are being used in many applications today including:
1. speech recognition.
2. music composition.
3. grammer learning
4. handwriting recognition

core components of a typical RNN:

figure -1 what a typical simple RNN will look like. 

sequence predicting by using RNN:

One of the best use cases of a RNN is sequence prediction. So, we will be creating RNN for sequenc predicting.
we are going to choose a simple sequence, a sine wave prediction.

First we must create the .ipynb file in jupyter notebook or VSCode.
figure - 2 visual presentation of a sine wave.

we have been given the input data for first 50 number of the sequence. we have to predict the 51st number based on input data by designing a Recurrent Neural Network.

step 1 - data preparation or preprocessing
this is the first step for any neural network and ultimately any data science project. 

for this project we will need python's math library.

Figure -3 generated sine wave visualization