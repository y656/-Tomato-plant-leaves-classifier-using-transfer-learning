# Tomato plant leaves classifier using Transfer learning 

This repository contains code for implementation of Mobilenet v2 architecture in agriculture domain to identify different diseases occuring in tomato plants.
I have used MobilenetV2 for the purpose of Transfer Learning because it is less computationally expensive and perfect fit for deloying in Mobile devices and Computers without GPU.

## Introduction:

Farmers growing Tomato crop are facing losses every year because of various diseases which can occur to a tomato plant. There are 9 common diseases which are:'Tomato_Bacterial_spot','Tomato_Early_blight','Tomato_Late_blight','Tomato_Leaf_Mold','Tomato_Septoria_leaf_spot','Tomato_Spider_mites_Two_spotted_spider_mite','Tomato__Target_Spot','Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus'.If a farmer can identify these diseases early and apply apropriate pesticides, then it can prevent ecconomic loss.

Our task is to create a Deep Learning model which can be deployed to mobile devices whereby a farmer takes a picture of Tomato leaf and our model should be able to predict it is a healthy plant or diseased plant and identify the type of disease. 

### Dataset:
The data for this repository is downloaded from https://www.kaggle.com/datasets/emmarex/plantdisease. 

### Overview:

I have built a tensorflow input pipeline and applied data preprocessing techniques to improving diversity of dataset by adding random flipped images.
Optimized tensorflow pipeline using prefetch and cache. I have then created a base model from pre trained mobilenet and used it as feature extractor  and added classifier layers on top of base model. Freezed the base layers and got an initial accuracy of 88%.

One way to increase performance even further is to train (or "fine-tune") the weights of the top layers of the pre-trained model alongside the training of the classifier you added. The training process will force the weights to be tuned from generic feature maps to features associated specifically with the dataset.Hence I fine tuned the entire model from 100 layer to adapt these specialized features to work with the new dataset.


### Results:

After optimizing the model performance using Adam optimizer,it  achieved a validation accuracy of 99.06% and validation loss of 0.0315 over 11 epochs which indicates our model is performing good on new data.




