from textblob import TextBlob
import en_local

def get_text_input():
    """Gets the text"""
    return input("Waiting for the text: ")

def analyze_text_stats(input_text):
    """Removes duplicate characters. Counts the number of sentences, words and syllables in the text."""
    cleaned_text = input_text.replace('!!!', '!').replace('???', '?').replace('...', '.')
    blob = TextBlob(cleaned_text)

    sentences_count = len(blob.sentences)
    words_count = len(blob.words)
    cnt = 0
    for i in range(len(blob)):
        if blob[i] in 'АЕЁИОУЫЭЮЯаеёиоуыэюя' or blob[i] in 'aeiouyAEIOUY':
          cnt+=1
    syllables_count = cnt / words_count
    return sentences_count, words_count, syllables_count

def calculate_average_lengths(sentences_count, words_count, syllables_count):
    """Calculates the average length of a sentence and a word."""
    average_sentence_length = words_count / sentences_count
    average_word_length = syllables_count / words_count
    return average_sentence_length, average_word_length

def calculate_readability_and_sentiment(words_count, sentences_count, syllables_count, blob):
    """"Calculates the index of readability, objectivity and mood of the text."""
    readability_index = 0
    if blob[0].upper() in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
        readability_index = 206.835 - 1.3 * average_word_length - 60.1 * syllables_count
    else:
        readability_index = 206.835 - 1.015 * avearge_word_lenght - 84.6 * syllables_count
    objectivity_analysis = (1 - blob.subjectivity) * 100
    sentiment_analysis = blob.sentiment.polarity

    return readability_index, objectivity_analysis, sentiment_analysis

def print_statistics(sentences_count, words_count, syllables_count,
                     average_sentence_length, average_word_length,
                     readability_index, objectivity_analysis, sentiment_analysis):
    """Displays text analysis statistics."""
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

    print(f'{en_local.OBJECTIVITY}: {objectivity_analysis}%')

    if sentiment_analysis > 0.5:
        print(f'{en_local.POSITIVE}')
    elif 0 < sentiment_analysis <= 0.5:
        print(f'{en_local.NEUTRAL}')
    else:
        print(f'{en_local.NEGATIVE}')

def main():
    """Main function for the text analysis"""
    input_text = get_text_input()
    
    sentences_count, words_count, syllables_count = analyze_text_stats(input_text)
    
    average_sentence_length, average_word_length = calculate_average_lengths(sentences_count, words_count, syllables_count)
    
    blob = TextBlob(input_text)
    readability_index, objectivity_analysis, sentiment_analysis = calculate_readability_and_sentiment(words_count, sentences_count, syllables_count, blob)
    
    print_statistics(sentences_count, words_count, syllables_count,
                     average_sentence_length, average_word_length,
                     readability_index, objectivity_analysis, sentiment_analysis)

if __name__ == "__main__": main()
