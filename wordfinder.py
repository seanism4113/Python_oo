from random import randint

class WordFinder:
    """ Word Finder: finds random words from a dictionary 
    
    >>> wf = WordFinder("simple.txt")
    235886 words were read
    
    >>> wf.random() in self.word_list
    True
    """

    def __init__ (self, text_file, word_list = []):
        """ Initialize text file, word list, and read file method"""

        self.text_file = text_file
        self.word_list = word_list
        self.read_file()

    def __repr__(self):
        """ Output for new Wordfinder instance"""

        return f"{len(self.word_list)} words were read"

    def read_file(self):
        """ Read file and append words to list.  Strip spaces/blanks"""

        file = open(self.text_file, 'r')

        for line in file:
            self.word_list.append(line.strip())

        file.close()

    def random(self):
        """ Return random word """
        return self.word_list[randint(0,len(self.word_list))]

class SpecialWordFinder(WordFinder):
    """ Specialized word finder that excludes blank lines and comments"""

    def read_file(self):
        """ Return list with blanks and comments removed """

        with open(self.text_file, 'r') as file:
            return [line.strip() for line in file
                if line.strip() and not line.startswith('#')]
            


