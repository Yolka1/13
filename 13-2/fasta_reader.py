from seq import Seq

class FastaReader:
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open (self.__filename, "r") as file:
            header = None
            sequence = []

            for line in file:
                line = line.strip()

                if line.startwith(">"):
                    if header is not None:
                        if not sequence:
                            raise ValueError ("После заголовка отсутствует последовательность")

                        yield Seq (header, "".join(sequence))

                else:
                    if header is None: 
                        raise ValueError ("Файл не соответствует формату FASTA")

                    if line:
                        sequence.append(line)

            if header is not None:
                if not sequence:
                    raise ValueError ("После заголовка отсутствует последовательность")
                 
                yield Seq (header, "".join(sequence))
        
        
        