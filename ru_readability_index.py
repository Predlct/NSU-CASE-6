from textblob import TextBlob
from translate import Translator

import ru_local


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
    translate_blob = TextBlob(text)
    text_objectivity_analysis = (1 - translate_blob.subjectivity) * 100
    text_sentiment_analysis = translate_blob.sentiment.polarity

    print(f'{ru_local.QUANTITY_SENTENCES}: {sentences_count}')
    print(f'{ru_local.QUANTITY_WORDS}: {words_count}')
    print(f'{ru_local.QUANTITY_SYLLABLES}: {syllables_count}')
    print(f'{ru_local.AVERAGE_LEN_SENTENCE_ON_WORDS}: {average_sentence_length}')
    print(f'{ru_local.AVERAGE_LEN_WORD_ON_SYLLABLES}: {average_word_length}')
    print(f'{ru_local.READABILITY_INDEX}: {readability_index}')

    if readability_index > 80:
        print(f'{ru_local.MORE_THEN_80}')
    elif 50 < readability_index <= 80:
        print(f'{ru_local.LESS_THEN_80}')
    elif 25 < readability_index <= 50:
        print(f'{ru_local.LESS_THEN_50}')
    else:
        print(f'{ru_local.LESS_THEN_25}')

    print(f'{ru_local.OBJECTIVITY}: {text_objectivity_analysis}%')

    if text_sentiment_analysis > 0.5:
        print(f'{ru_local.POSITIVE}')
    elif 0 < text_sentiment_analysis <= 0.5:
        print(f'{ru_local.NEUTRAL}')
    else:
        print(f'{ru_local.NEGATIVE}')
