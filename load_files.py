import pandas as pd

def read_vocab(file_path):
    file = pd.ExcelFile(file_path)
    noun_definitions_df = pd.read_excel(file, sheet_name="1781 Nouns")
    noun_articles_df = pd.read_excel(file, sheet_name="Article - Noun")
    return noun_definitions_df, noun_articles_df

noun_definitions_df, noun_articles_df = read_vocab('vocab.xlsx')