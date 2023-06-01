# NLPToolkit
Natural Language Processing Tutorial and Examples for Python

# Welcome to my NLP Training Toolkit
This short tutorial will get you on your way to making custom natural language systems in Python in no time whatsoever. Just follow these steps and you will have a working system in no time.

## What is Natural Language Processing and why should you use it?
Natural Language Processing is a type of system intended to create a text or voice based interface for functions of your application. This type of system can frequently be found in chatbots, search engines, video games, and more. 

Natural language processing enables commands like "Set the temperature of my house to 75 degrees in 30 minutes", which allow users to accomplish goals faster without the need for digging through menus to find the right settings.

Although this sort of system may seem daunting at first, I am here to show you how you can easily integrate it into your own python projects.

## Basic Principles
There are two basic components in a natural language query, an **intent** and the **entities**.

- **Intent** - What action the user wants to take by writing out the command, like turn on appliance, change variable, create new XYZ, etc
- **Entities** - What components are in the command that correspond to inputs in your application, like time, name, location, etc

A natural language processing system needs to be able to identify the overall intent of a command, and then pick apart the relevant entities to fill out and execute the users wishes in python. 

This can be accomplished using a combination of various methods:

- **Machine learning for intents** - You can train a intent classification system using a recurrent neural network (RNN) architecture with an LSTM (Long Short-Term Memory) layer to identify the intent as a whole.
- **RegEx for entities** - A rule based approach can be taken for entities you know will be consistent, like time, dates, links, etc you can use a RegEx expression to extract these entities.
- **FuzzyWuzzy for entities** - For entities which are explicitly named, like the names of devices, variables, etc which are prone to being misspelled by users
- **Machine learning for entities** - You can train a Named Entity Recognition (NER) to identify entities which are explicitly named. NER helps in extracting structured information from unstructured text when tools like FuzzyWuzzy won't cut it. 
-- **Machine learning for free form entities** - You can train a custom Conditional Random Field (CRF) or Recurrent Neural Network (RNN) to pick out parts of your user input which might be more complex, like a description which the user desires to set for a variable, a situation where multiple variables are updated in one command (not recommended but possible), etc


## Using this Toolkit
*Work In Progress*
To start creating your own natural language processing tools, I have created a convenient set of pre-set training tools, data-creation aids, and model testing systems designed to aid in full end to end deployment.


### Getting set up
This system is designed to work with Python 3.10 out of the box. Install Python 3.10 and install all the project requirements from the included requirements.txt

### Intent System Creation
To start, we will define intents. Navigate to your categories.csv file and fill each line with an intent variable you want, like add_data, retrieve_data, create_post, etc. Whatever you want your application to be able to do with natural language processing. Just make sure they're are no spaces or special characters besides _

Once you are done configuring your categories for detection, you will run the local flask server *datamaker.py.* This will open up a site on your local network with a simple data formatter for creating your intent training data, which will be used to train your own intent module.

#### Making Intent Classifier data
**Think of every way your user might wright out a command you want them to be able to access and write them out while the correct category is selected.** When I say every way, I really mean get creative with it. Assume your users will try the most absurd backwards wordings of what they want to do, and type it out. Include examples with and without intents, with things in backwards, etc. You want to get at least 15-25 examples for every intent you want, and more so if you have overlapping similarities in two or more intents.
#### Training the intent classifier model
Once you are done, you can check your new file data.csv for all your fully formatted data. Take the contents of this file, and copy it all into the training_data = [ ] section of *train_intent_model.py*

Now, run the train intent model file. Keep an eye on the terminal for the training accuracy while it goes on, and especially keep an eye on what epoch is it at when it hits 95-100% accuracy. Go back into the file and set the epoch to in or around that range to prevent overfitting (AKA before it begins to only accept exact matches of its training data). Now with your epochs set, run the model again and you are ready for the next step.

#### Testing your model
Now that you have a trained model, you are ready to see how it does at classifying intents. Run *intent_module_evaluator.py* to load in your model and test it in the project terminal. Write out a few new variations on your intents commands and see if they are identified as you intended them to be. If they aren't, go back to training and keep adding more intents, modifying your epochs, and if all else fails, change the batch side. 

A larger batch size provides a more accurate estimate of the gradient, which can lead to faster convergence. However, it may also result in overshooting the optimal solution or getting stuck in sharp minima. Smaller batch sizes, on the other hand, introduce more noise into the gradient estimate but can help the model generalize better by escaping sharp minima. Batch size can also influence the learning dynamics of the model. In general, larger batch sizes lead to smoother training curves and less fluctuation in the training loss. Smaller batch sizes can introduce more variability and make the training process less stable.

Now that you have your intent model, we are ready to move on to the next step. Before you do however, make sure to save your model training data and code in a safe place so you are able to retrain the model with new intents as you add new features to your project. Being able to reproduce your results and drop a new model in seamlessly is a huge advantage here. 

With that all out of the way, it is time to move on to entities.

### Entity System Creation
Creating your entity extraction system is the more nuanced and complex part of creating a natural language processing system. For this step, you really want to understand what inputs each of your intents needs and handle each type of input on a case by case basis.
