from seq import Seq

class FastaReader:
    """Класс для чтения файлов в формате FASTA.
     
    Читает FASTA-файл по отдельным записям и возвращает объекты класса Seq
    """
    def __init__(self, filename):
        """Создает объект для чтения FASTA-файла.
        
        Parameters
        ----------
        filename : str
            Имя или путь к FASTA-файлу.
        """
        self.__filename = filename

    def read(self):
        """Читает FASTA-файл и возвращает записи по одной.
        
        Каждая FASTA-запись преобразуется в объект класса Seq.
        Используется генератор, поэтому весь файл не загружается 
        в пямять целиком.
        
        Yeilds
        ------
        Seq
            Объект последовательности из очередной FASTA-записи.
        
        Raises
        ------
        ValueError
            Если последовательность встречается без заголовка или
            заголовок не содержит в себе последовательности.
        """
        with open (self.__filename, "r") as file:
            header = None
            sequence = []

            for line in file:
                line = line.strip()

                if line.startswith(">"):
                    if header is not None:
                        if not sequence:
                            raise ValueError ("После заголовка отсутствует последовательность")

                        yield Seq (header, "".join(sequence))

                    header = line [1:]
                    sequence = []

                else:
                    if header is None: 
                        raise ValueError ("Файл не соответствует формату FASTA")

                    if line:
                        sequence.append(line)

            if header is not None:
                if not sequence:
                    raise ValueError ("После заголовка отсутствует последовательность")
                 
                yield Seq (header, "".join(sequence))
        
        
        