class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        
    def get_word_count(self):
        return len(self.sentence.split())
    
    def get_shortest_word(self):
        list_of_words = self.sentence.split()
        shortest_word = list_of_words[0]
        for word in list_of_words:
            if(len(word) < len(shortest_word)):
                shortest_word = word
        return len(shortest_word)
    
    def get_longest_word(self):
        list_of_words = self.sentence.split()
        longest_word = list_of_words[0]
        for word in list_of_words:
            if(len(word) > len(longest_word)):
                longest_word = word
        return len(longest_word)
