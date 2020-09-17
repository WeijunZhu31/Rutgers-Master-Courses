# Topic 1: A Tour d'Horizon of the course


You must have a working Python implementation. Python version 3.7 or later is a must. You should also implement Tensorflow and Keras (see below)

- Read DL chapters Chpater 1, Introduction
- Read the accompanying lecture notes on neural networks
- Read Ch 1 & 2 of DLP, also Appendix A on installing Python, Tensorflow and Keras
- The following notes are a broad overview of neural networks and deep learning field:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [An overview of Neural networks](https://sakai.rutgers.edu/access/lessonbuilder/item/12558157/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Topic10NeuralNets.pdf)

- - The following python scripts serve as initial warm-ups on Tensorflow. The first one is a very simple code, the first baby steps:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [tfPractice.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12558159/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/tfPractice.py)

- - The next one is slightly more sophisticated Tensorflow code implementing linear regression on the California "housing" data. Both matirx formula for the regression weights, and the gradient decent methods are implemented. Please study these scripts carefully to get a handle on Tensorflow:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [tfRegressionGDCAHousing.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12558162/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/tfRegressionGDCAHousing.py)

- - Finally, the following is from the text DLP. A Keras implementation of a one-layer neural network on the "digit handwriting" data:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnist1.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12558167/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnist1.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [testDigitShow.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12558592/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/testDigitShow.py)

- - The same problem and the same method but using "functional" approach to build the network:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistFunctional.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12559090/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistFunctional.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [testDigitShowFunctional.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12559636/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/testDigitShowFunctional.py)

- # Topic 2: Review of Learning Theory Basics:

   #### Maximum Likelihood, Linear and Logistic Regression

   - Read Chapter 4 of DLP
   - Review Chapters 2 & 3 (skip section 3.14 for now), and Chapter 5 up to section 5.9 of DL
   - Also I am leaving four relevant lecture notes I prepared for an introductory machine learning class covering maximum likelihood, linear regression, logistic regression, and nonlinear models. The last one also covers basic rules of feature selection, model complexity, and regularization.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [Maximum Likelihood](https://sakai.rutgers.edu/access/lessonbuilder/item/12558357/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Topic2MaxLikelihood-1.pdf)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [Linear Regression](https://sakai.rutgers.edu/access/lessonbuilder/item/12558358/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Topic3LinearRegressionClassification.pdf)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [Logisitic Regression](https://sakai.rutgers.edu/access/lessonbuilder/item/12558359/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Topic4LogisticRegression-4.pdf)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [Nonlinear models, model selection, Regularization](https://sakai.rutgers.edu/access/lessonbuilder/item/12558360/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Topic5ModelSelection.pdf)

- - The following web site is a good reference for Keras:

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [keras.io/](https://sakai.rutgers.edu/access/lessonbuilder/item/12559028/)

- - If you have an R installation, you may want to run the following script to visualize both likelihood and log likelihood function arising from logistic regression (it requires installing the rgl library)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [logiticGraph.r](https://sakai.rutgers.edu/access/lessonbuilder/item/12559652/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/logiticGraph.r)

- # Topic 3: Review of Multi-variate Calculus and Optimization Techniques

   - Read chapter 6 of DL (you can skip 6.2.2.4)
   - Pay special attention to DL 6.5 on details of the back-propagation algorithm
   - Also continue reviewing DLP ch. 4.
   - The following Python scripts show how differentiation is accomplished.
   - After the script we have a note from the book "*Handson Machine Learning with Scikit-Learn, Keras and Tensorflow"* by A. Geron. This note gives you the exact process involved for both back-propagation and feed-forward methods for differentiation.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [tfDerivPractice.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12565291/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/tfDerivPractice.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [Hands on Machine Learning with Scikit Learn and TensorflowAppendixD Autodiff.pdf](https://sakai.rutgers.edu/access/lessonbuilder/item/12566342/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/Hands on Machine Learning with Scikit Learn and TensorflowAppendixD Autodiff-1.pdf)

- # Topic 4: Regularization

   - Real DL chapter 7 (skip 7.14 for now)
   - Read DLP ch. 4
   - **A note on tensorflow2:** If you have tensorflow2 installed, some of the scripts in DLP and what I post may not work properly and need to be modified slightly. A great book that covers not only Tensorflow and Keras, but also Scikit-learn is "*Hands-On Machine-Learning with scikit-learn keras and tensorflow*" by A. Ge'ron. I highly recommend this book.
   - The following two scripts work on the IMDB data (comes with keras) and tries to build a binary classification model for it

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [imdbBinaryClassification.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12566303/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/imdbBinaryClassification-1.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [imdbBinaryClassificationDropout.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12566304/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/imdbBinaryClassificationDropout-1.py)

- # Topic 5: Optimization Techniques

   - Review Chapter 4 and read chapter 8 of DL
   - Read DLP Chapter 7 section 7.1 (for a formal introduction to the functional form of Keras and more complex forms of graphs,) and 7.2 for callbacks and especially using them for early stopping strategy, and for Tesnorboard visualization.
   - This is a good time to set visit [https://colab.research.google.com ](https://colab.research.google.com/)and learn how to use their GPU enabled notebooks. Could be useful for your projects. I have provided a short Howto in HW2 text. Also notice I have observed some issues running the first script below on Colab. Colab has some bugs, but when it works, it is really fast.
   - The following are a series of scripts on a data set of consisted of 50,000 color, low-resolution pictures belonging to ten categories. The first script is a straightforward without any regularization or initialization. We use it as a benchmark. Try using Google Colab.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistCiafarFunctional.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12569121/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistCiafarFunctional-1.py)

- - The next two scripts implement L1 and L2 regularization and early stopping to this data.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistCiafarFunctionalRegularized.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12570032/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistCiafarFunctionalRegularized.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistCiafarFunctionalValidation.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12570033/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistCiafarFunctionalValidation.py)

- - 3/11/20 lecture for those who could make the class. Follow the following [link ](https://drive.google.com/drive/u/1/folders/1mID8Trqb_i42a4RMx59woQcRYcewq8Ka)in Google Drive

- # Topic 6: Convolutional Neural Networks and Image Recognition

   - Read DL chapter 9, and DLP Ch. 5.
   - The following scripts implement convolutional neural nets on the Fashion mnist data and the cifar10 data
   - Here are two different implementations of convolutional neural nets for the FashioMnist data. The second one has more layers and adds dropout layers

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistFashionConv.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573626/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistFashionConv.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistFashionConv2.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573662/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistFashionConv2.py)

- - For the cifar10 data here is an attempt. It improves the error rate to over 50%. I will try to dabble with it and improve accuracy.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [mnistCiafarConv.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573627/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/mnistCiafarConv.py)

- - The famous cats and dogs data set is a set of 8000 pictures, 4000 for cats and 4000 for dogs. Below a sequence of convolutional neural net models are given to try to achieve a a high accuracy prediction.
     1. The first file is a small convnet. It achieves a relatively low accuracy in recognizing cats from dogs.
     2. The second and the third ones use a predefined GGV16 predefined convnet that comes with keras. In the second file, the images are fed to GGV16, and then the output is fed to our own dense layers.
     3. In the third file the GGV16 is the start of our layers and we add our own layers on top of it. In this version "data augmentation" is used and each time an image is accessed, a transformation such as rotation/shearing/zooming/flipping etc. is applied.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [catsDogsSetupFiles.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12576034/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/catsDogsSetupFiles.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [catsDogsSetupPretrainedVGG16featureExtractred.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12579863/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/catsDogsSetupPretrainedVGG16featureExtractred.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [catsDogsSetupPretrainedVGG16.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12579864/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/catsDogsSetupPretrainedVGG16.py)

- - Here are some concrete scripts showing how specific filters effects are on the image data.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [filter.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573667/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/filter.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [testFilter.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573668/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/testFilter.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [simpleFilterTesnorflow.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12573669/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/simpleFilterTesnorflow.py)

- - Running one dimensional CNN on text data: IMDB

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [imdbEmbedBinaryClassification.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12576032/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/imdbEmbedBinaryClassification.py)

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [imdbEmbedBinaryClassificationConv1D.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12576033/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/imdbEmbedBinaryClassificationConv1D.py)

- # Topic 7: Recurrent Neural Networks

   - Read DL chapter 10 and DLP chapter 6.
   - The following file is a simple simulated data run through a number of RNN's.

- ![img](https://sakai.rutgers.edu/lessonbuilder-tool/images/not-required.png)

    [timeSeriesGeneration.py](https://sakai.rutgers.edu/access/lessonbuilder/item/12579867/group/8a41c8ea-9bdf-4502-a2fe-28db4c4b7f33/Lecture Notes/timeSeriesGeneration.py)