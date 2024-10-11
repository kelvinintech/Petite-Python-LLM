import tensorflow as tf

class LearningLanguageModel:
    def __init__(self):
        pass 
#helps your llm learn
#a class is a blueprint for creating objects
#this class will encapsulate all functions attributes for the Petitle

    def train(self, training_data):
        print("Training the model with the following data:")
        for data in training_data:
            print(f'Processing: {data}')

    def evaluate(self, test_data):
        print("Evaluating the model with the following test data:")
        for data in test_data:
            print(f'Processing: {data}')

    def explain_concept(self, concept):
        explanations = {
        "variables": "Variables are like boxes where you can store information.",
        "functions": "Functions are reusable pieces of code that perform a specific task.",
        "loops": "Loops allow you to repeat a block of code multiple times.",
        "lists": "Lists are ordered collections of items.",
    }
        return explanations.get(concept.lower(), "Sorry, I don't have information on that concept.")

#resonsible for accessing the performance of the model
#evaluation is crucial to determine how well the model learned
