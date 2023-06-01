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

- **Machine learning for intent** - You can train a intent classification system using a recurrent neural network (RNN) architecture with an LSTM (Long Short-Term Memory) layer to identify the intent as a whole.
- **RegEx for entities** - A rule based approach can be taken for entities you know will be consistent, like time, dates, links, etc you can use a RegEx expression to extract these entities.
- **FuzzyWuzzy for entities** - For entities which are explicitly named, like the names of devices, variables, etc which are prone to being misspelled by users
- **Machine learning for entities** - You can train a Named Entity Recognition (NER) to identify entities which are explicitly named. NER helps in extracting structured information from unstructured text when tools like FuzzyWuzzy won't cut it. 
-- **Machine learning for free form entities** - You can train a custom Conditional Random Field (CRF) or Recurrent Neural Network (RNN) to pick out parts of your user input which might be more complex, like a description which the user desires to set for a variable, a situation where multiple variables are updated in one command (not recommended but possible), etc
