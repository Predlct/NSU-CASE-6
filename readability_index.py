from textblob import TextBlob
from langdetect import detect

text = input('Введите текст: ')
text = text.replace('!!!', '!')
text = text.replace('???', '?')
blob = TextBlob(text)

ru_vowel_letters = 'аоуэыяёеюи'
en_vowel_letters = 'aeiouy'

print(f'Кол-во предложений: {len(blob.sentences)}')
print(f'Кол-во слов: {len(blob.words)}')

if detect(text) != 'en':
    print(f'Кол-во слогов: {len([x for x in text.lower() if x in ru_vowel_letters])}')
else:
    count = 0
    for word in text.split():
        if word[0] in en_vowel_letters:
            count += 1
        for index in range(1, len(word)):
            if word[index] in en_vowel_letters and word[index - 1] not in en_vowel_letters:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
    print(f'Кол-во слогов: {count}')
