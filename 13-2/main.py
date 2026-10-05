"""Демонстрационная программа для работы с FASTA-файлами.

Показывает работу классов Seq и FastaReader.
"""

from fasta_reader import FastaReader

reader = FastaReader("example.fasta")

for seq in reader.read():
    print(seq)
    print("Длина: ",seq.length)
    print("Алфавит: ",seq.alphabet)
    print("Тип: ", seq.type)
    print()