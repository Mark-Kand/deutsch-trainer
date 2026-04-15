import pandas as pd

VOCAB_FILE_PATH = "vocab.xlsx"

class Trainer:
    def __init__(self, train_mode, lesson_length):
        self.train_mode = train_mode
        self.file_path = VOCAB_FILE_PATH
        self.lesson_length = lesson_length
        self.vocab = self._load_vocab()
        self.lesson_vocab = self._create_lesson()
        self.score = 0
    
    def _load_vocab(self):
        file = pd.ExcelFile(self.file_path)
        if self.train_mode == "Definitions":
            vocab = pd.read_excel(file, sheet_name="1781 Nouns", header=None)
        elif self.train_mode == "Articles":
            vocab = pd.read_excel(file, sheet_name="Article - Noun", header=None)
        return vocab
    
    def _create_lesson(self):
        lesson_vocab = self.vocab.sample(n=self.lesson_length)
        return lesson_vocab
    
    def present_word(self):
        for index, row in self.lesson_vocab.iterrows():
            yield row[0], row[1]
    
    def check_answer(self):
        pass