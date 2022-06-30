from os import listdir, system
from os.path import isfile, join, abspath, dirname
import pandas as pd
import csv

# format csv
'''
"word1";"перевод1"
"word2";"transcription2";"перевод2"
"word3";"перевод3";"example1";"пример1"
"word4";"transcription4";"перевод4";"example1";"пример1";"example2";"пример2"
'''

BASE_DIR = abspath(join(dirname(__file__)))
DATA_DIR = BASE_DIR + '/data/'



PATH_FILE_XLSX = DATA_DIR + 'irregular_verbs.xlsx'
PATH_FILE_CSV = DATA_DIR + 'result.csv'


def decode(file_input, file_output):
    df = pd.read_excel(
        file_input,
        header=None,
        index_col=None,
        names=['get', 'infinitive', 'past_simple', 'past_participle', 'translation'],
        )
    df_selected_only = df[df['get'] == '+'].filter(items=['infinitive', 'past_simple', 'past_participle', 'translation'])
    df_result = pd.DataFrame(columns=['word', 'перевод', 'verb_form', 'форма глагола'])
    
    for row in df_selected_only.itertuples(index=False):
        data_for_upd = {
            'word': [row.infinitive, row.past_simple, row.past_participle],
            'перевод': [row.translation, row.translation, row.translation],
            'verb_form': ['Infinitive', 'Past Simple', 'Past Participle'],
            'форма глагола': ['Инфинитив', 'Прошедшее время', 'Страдательное причастие']
        }
        df_update = pd.DataFrame(data_for_upd, )
        df_result = pd.concat([df_result, df_update])
    pd.set_option('display.max_rows', None)
    df_result_clean = df_result.replace(to_replace=r'\n', value=', ', regex=True)
    print(df_result_clean)
    df_result_clean.to_csv(file_output,
        sep=";",
        index=False,
        header=False,
        encoding='utf-8',
        line_terminator = '\r',
    )



def main():
    all_files = [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f))]
    xlsx_files = list(filter(lambda x: ".xlsx" in x, all_files))
    for filename in xlsx_files:
        PATH_FILE_XLSX = DATA_DIR + filename
        PATH_FILE_CSV = DATA_DIR + '.'.join([filename.split(".")[0], 'csv'])
        decode(PATH_FILE_XLSX, PATH_FILE_CSV)


if __name__ == '__main__':
    main()
