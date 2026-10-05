class Seq:
    """Класс для работы с биологическими последовательностями.
    
    Хранит загловок FASTA-записи и последовательностью
    Позволяет получить длину последовательности, уникальный алфавит и
    определить тип последовательности
    """

    def __init__(self, header, sequence):
        """Создает объект последовательности.
        
        Parameters
        ----------
        header : str
            Заголовок FASTA-записи без символа '>'.
        sequence : str
            Биологическая последовательность.
        """
        self.__header = header
        self.__sequence = sequence

    def __str__(self):
        """Возвращает последовательность в формате FASTA.
         
        Returns
        -------
        str
            Заголовок с символом '>' и последовательность. 
        """
        return f">{self.__header}\n{self.__sequence}"
    
    @property
    def length(self):
        """Возвращает длину последовательности.
        
        Returns
        -------
        int
            Количество символов в последовательности.
        """
        return len(self.__sequence)
    
    @property
    def alphabet(self):
        """Возвращает уникальный алфавит последовательности.
        
        Returns
        -------
        set
            Множество уникальных символов последовательности.
        """
        return set(self.__sequence)
    
    @property
    def type(self):
        """Определяет тип биологической последовательности.
        
        Returns
        -------
        str
            'nucleotide' для нуклеотидной последовательности
            или 'protein' для белковой последовательности.
        """
        nucleotide_alphabet = set ("ACGTURYSWKMBDHNVN")

        for symbol in self.__sequence.upper():
            if symbol not in nucleotide_alphabet:
                return "protein"
        
        return "nucleotide"
    