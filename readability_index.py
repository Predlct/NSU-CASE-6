from textblob import TextBlob
from ruts import BasicStats
from langdetect import detect

text = "War doesn't show who's right, just who's left."
text = text.replace('!!!', '!')
text = text.replace('???', '?')
blob = TextBlob(text)

print(f'Кол-во предложений: {len(blob.sentences)}')
print(f'Кол-во слов: {len(blob.words)}')

if detect(text) != 'en':
    bs = BasicStats(text)
    print(f'Кол-во слогов: {bs.get_stats()['n_syllables']}')
