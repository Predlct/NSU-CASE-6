from ru_readability_index import get_russian_text_stats
from en_readability_index import get_english_text_stats

language_choose = input('Select text languages (ru/en): ')
text = input('Введите текст: ')

if language_choose == 'ru':
    get_russian_text_stats(text)
elif language_choose == 'en':
    get_english_text_stats(text)
else:
    print('Язык введён неверно!')
