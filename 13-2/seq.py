class Seq:

    def __init__(self, header, sequence):
        self.__header = header
        self.__sequence = sequence

    def __str__(self):
        return f">{self.__header}\n{self.__sequence}"
    
    @property
    def length(self):
        return len(self.__sequence)
    
    @property
    def alphabet(self):
        return set(self.__sequence)
    
    @property
    def type(self):
        nucleotide_alphabet = set ("ACGTURYSWKMBDHNVN")

        for symbol in self.__sequence.upper():
            if symbol not in nucleotide_alphabet:
                return "protein"
        
        return "nucleotide"