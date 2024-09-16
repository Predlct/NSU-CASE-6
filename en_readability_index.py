from textblob import TextBlob
import en_local

def get_english_text_stats(input_text):
    text = input_text.replace('!!!', '!')
    text = text.replace('???', '?')
    text = text.replace('...', '.')
    blob = TextBlob(text)
    en_vowel_letters = 'aeiouy'

    sentences_count = len(blob.sentences)
    words_count = len(blob.words)

    syllables_count = len([x for x in text.lower() if x in en_vowel_letters])
    average_sentence_length = len(blob.words) / len(blob.sentences)
    average_word_length = syllables_count / len(blob.words)

    readability_index = 206.835 - 1.015 * (words_count / sentences_count) - 84.6 * (
            syllables_count / words_count)

    text_objectivity_analysis = (1 - blob.subjectivity) * 100
    text_sentiment_analysis = blob.sentiment.polarity

    print(f'{en_local.QUANTITY_SENTENCES}: {sentences_count}')
    print(f'{en_local.QUANTITY_WORDS}: {words_count}')
    print(f'{en_local.QUANTITY_SYLLABLES}: {syllables_count}')
    print(f'{en_local.AVERAGE_LEN_SENTENCE_ON_WORDS}: {average_sentence_length}')
    print(f'{en_local.AVERAGE_LEN_WORD_ON_SYLLABLES}: {average_word_length}')
    print(f'{en_local.READABILITY_INDEX}: {readability_index}')

    if readability_index > 80:
        print(f'{en_local.MORE_THEN_80}')
    elif 50 < readability_index <= 80:
        print(f'{en_local.LESS_THEN_80}')
    elif 25 < readability_index <= 50:
        print(f'{en_local.LESS_THEN_50}')
    else:
        print(f'{en_local.LESS_THEN_25}')

    print(f'{en_local.OBJECTIVITY}: {text_objectivity_analysis}%')

    if text_sentiment_analysis > 0.5:
        print(f'{en_local.POSITIVE}')
    elif 0 < text_sentiment_analysis <= 0.5:
        print(f'{en_local.NEUTRAL}')
    else:
        print(f'{en_local.NEGATIVE}')