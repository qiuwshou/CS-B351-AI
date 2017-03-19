from InferenceEngine import *
from Tools import *

class RuleBasedSystem:
    ###
    # a class defining a production system
    ###
    def __init__(self, rules, workingMemory):
        ###
        # initialization function to do necessary conversions for inference engine
        # and instantiate the production system
        ###
        self.rules = rules
        self.workingMemory = workingMemory

        # necessary for inference engine, NO TOUCHING
        self.workingMemoryList = [parseStringToArray(x) for x in self.workingMemory]

    def generateInferences(self):
        ###
        # calls the inference engine to update the working memory
        ###
        self.workingMemoryList = inferNewFacts(self.rules, self.workingMemoryList)
        self.workingMemory = [parseArrayToString(x) for x in self.workingMemoryList]

class Rule:
    ###
    # a class for holding all of the components of a rule (i.e. name, antecedent, consequents)
    ###
    def __init__(self, name, antecedents, consequents):
        ###
        # initialization function that will convert necessary things for inference
        # engine and instantiate instance of rule
        ###
        self.name = name
        self.antecedents = antecedents
        self.consequents = consequents

        # necessary for inference engine, NO TOUCHING
        self.antecedentList = [parseStringToArray(x) for x in self.antecedents]
        self.consequentList = [parseStringToArray(x) for x in self.consequents]


def tagSentence(sentence):
    # a function that will take in a sentence and tag it
    ###
    WorkingMemory = []
    
    
    rule1 = Rule("1st-rule", ["BEGIN_SENTENCE precedes ?word1"], ["?word1 = Noun", "?word1 = Noun"])
    rule2 = Rule("2nd-rule", ["?word1 precedes ?word2", "?word1 = Verb"], ["?words = Adverbs"])
    rule3 = Rule("3rd-rule", ["?word1 precedes ?word2", "?word2 = Noun", "?word2 = Pronoun", "?word2 = Adjective"], ["?word1 = Adjective"])
    rule4 = Rule("4th-rule", ["?word1 precedes ?word2", "?word2 = Pronoun","?word2 = Noun"], ["?word1 = Determiners"])
    rule5 = Rule("5th-rule", ["?word1 precedes ?word2", "?word2 = Verb"], ["?word1 = Noun"])
    rule6 = Rule("6th-rule", ["?word1 precedes ?word2", "?word2 = Verb", "?word3 precedes ?word4", "?word4 precedes ?word1", "?word3 = Preposition", "?word4 = Determiner"], ["?word1 = Noun"]) 
    rule7 = Rule("7th-rule", ["?word1 precedes ?word2", "?word1 = Noun", "?word1 = Pronoun"], ["?word2 = Verb"])
    rule8 = Rule("8th-rule", ["?word1 precedes ?word2", "?word1 = Verb"], ["?word2 = Preposition"])
    Rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8]
    
                            

    word_list = sentence.split()
    clear_list = []
    for word in word_list:
        if word != " ":
        #remove punctuation and convert to lowercase
            for p in list(punctuation):
                word = word.replace(p, '')
            word = word.lower()
            clear_list.append(word)
                 
    begin_fact = "BEGIN_SENTENCE precedes " + clear_list[0]
    end_fact = clear_list[-1] + " precedes END_SENTENCE"
    WorkingMemory.append(begin_fact)
    size = len(clear_list)
        for i in range(1, size-1):
            WorkingMemory.append(clear_list[i]
    WorkingMemory.apeend(end_fact)

    system = RuleBasedSystem(Rules, WorkingMemory)
    system.generateInferences()

    pass
