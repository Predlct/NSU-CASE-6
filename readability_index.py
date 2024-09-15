from textblob import TextBlob
from langdetect import detect
import syllables

text = input('Введите текст: ')
text = text.replace('!!!', '!')
text = text.replace('???', '?')
blob = TextBlob(text)

ru_vowel_letters = 'аоуэыяёеюи'
en_vowel_letters = 'aeiouyAEIOUY'

print(f'Кол-во предложений: {len(blob.sentences)}')
print(f'Кол-во слов: {len(blob.words)}')

syllables_count = 0
if detect(text) != 'en':
    syllables_count = len([x for x in text.lower() if x in ru_vowel_letters])
    print(f'Кол-во слогов: {syllables_count}')
else:
    syllables_count = syllables.estimate(text.lower())
    print(f'Кол-во слогов: {syllables_count}')

print(f'Средняя длина предложения в словах: {len(blob.words) / len(blob.sentences)}')
print(f'Средняя длина слова в слогах: {syllables_count / len(blob.words)}')
