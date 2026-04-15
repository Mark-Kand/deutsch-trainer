import pandas as pd

class Trainer:
    def __init__(self, train_mode, file_path):
        self.train_mode = train_mode
        self.file_path = file_path
        self.vocab = self._load_vocab()
    
    def _load_vocab(self):
        file = pd.ExcelFile(self.file_path)
        if self.train_mode == "Definitions":
            vocab = pd.read_excel(file, sheet_name="1781 Nouns")
        elif self.train_mode == "Articles":
            vocab = pd.read_excel(file, sheet_name="Article - Noun")
        return vocab