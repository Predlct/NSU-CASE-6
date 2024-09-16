from textblob import TextBlob
from translate import Translator


def get_russian_text_stats(input_text):
    text = input_text.replace('!!!', '!')
    text = text.replace('???', '?')
    text = text.replace('...', '.')
    blob = TextBlob(text)
    ru_vowel_letters = 'аоуэыяёеюи'

    sentences_count = len(blob.sentences)
    words_count = len(blob.words)

    syllables_count = len([x for x in text.lower() if x in ru_vowel_letters])
    average_sentence_length = len(blob.words) / len(blob.sentences)
    average_word_length = syllables_count / len(blob.words)

    readability_index = 206.835 - 1.3 * (len(blob.words) / len(blob.sentences)) - 60.1 * (
            syllables_count / len(blob.words))

    translator = Translator(from_lang='RU', to_lang="EN")
    text = translator.translate(text)
    print(text)
    translate_blob = TextBlob(text)
    text_objectivity_analysis = (1 - translate_blob.subjectivity) * 100
    text_sentiment_analysis = translate_blob.sentiment.polarity

    print(f'Кол-во предложений: {sentences_count}')
    print(f'Кол-во слов: {words_count}')
    print(f'Кол-во слогов: {syllables_count}')
    print(f'Средняя длина предложения в словах: {average_sentence_length}')
    print(f'Средняя длина слова в слогах: {average_word_length}')
    print(f'Индекс удобочитаемости Флеша: {readability_index}')

    if readability_index > 80:
        print('Читается очень легко (для младших школьников).')
    elif 50 < readability_index <= 80:
        print('Простой текст (для школьников).')
    elif 25 < readability_index <= 50:
        print('Текст немного трудно читать (для студентов).')
    else:
        print('Текст трудно читается (для выпускников ВУЗов).')

    print(f'Объективность текста: {text_objectivity_analysis}%')

    if text_sentiment_analysis > 0.5:
        print('Положительная тональность.')
    elif 0 < text_sentiment_analysis <= 0.5:
        print('Нейтральная тональность')
    else:
        print('Отрицательная тональность.')
