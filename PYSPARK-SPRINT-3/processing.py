import re
import unicodedata
from datetime import date, datetime
from difflib import SequenceMatcher
import nltk
from nltk.tokenize import RegexpTokenizer
from LeIA import leia

from pandas import DataFrame, Series


def round_range(value, start: int, stop: int, step: int) -> int:
    values = list(range(start, stop + 1, step))
    min_val = min(values)
    max_val = max(values)
    stepper = (max_val - min_val) / len(values)
    ranger = (value - min_val) / stepper
    return values[int(ranger)]


def get_sentiment_of_value(df: DataFrame, word):
    valor = df.loc[df['frequent'].apply(lambda freq: word in freq)]['sentiment'].mean()
    if valor > 0:
        return "Positivo"
    elif valor == 0:
        return "Neutro"
    else:
        return "Negativo"


def words_in_tweet(tweet: list):
    only_words_tweets = []
    for words in tweet:
        onlywords = []
        for word in words:
            onlywords.append(word[0])
        only_words_tweets.append(onlywords)
    return only_words_tweets


def freq_tweet_day(tweets: Series):
    frequency = []
    for tweet in tweets:
        count = tweet[1]
        for t in tweets:
            if t[0] == tweet[0]:
                count += t[1]
        frequency.append([tweet[0], count])
    return ', '.join(map(lambda f: str(f[0]), frequency[:3]))


def freq_tweet(tweets: DataFrame):
    frequency = []
    for tweet in tweets:
        count = tweet[1]
        for t in tweets:
            if t[0] == tweet[0]:
                count += t[1]
        frequency.append([tweet[0], count])
    return frequency


def remove_special_chars(text: str):
    text = unicodedata.normalize('NFD', text) \
        .encode('ascii', 'ignore') \
        .decode("utf-8")
    return str(text)


def no_accents_lower(text: str):
    noaccent = remove_special_chars(text)
    return noaccent.lower()


def get_date(datestr: str):
    return datetime.strptime(datestr[:-5], "%Y-%m-%dT%H:%M:%S")


def is_similar(string_a: str, string_b: str, percentage=0.8) -> bool:
    sm = SequenceMatcher(a=string_a, b=string_b)
    return sm.ratio() >= percentage


def get_age_from_birthdate(birthdate: str) -> int:
    born = datetime.strptime(birthdate, '%d/%m/%Y')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_label_from_floatbool(label: float) -> str:
    return "Sim" if label >= 1 else "Não"


def get_label_from_bool(value: bool) -> str:
    return "Sim" if value else "Não"


def analyze_tweet_sentiment(text: str):
    sentiment_analyzer = leia.SentimentIntensityAnalyzer()
    result = sentiment_analyzer.polarity_scores(text)
    return result["compound"]


def analyze_tweet_frequency(text: str):
    text_nolinks = re.sub(r'http\S+', '', text)
    regexp = RegexpTokenizer(r'\w+')
    onlytext = ' '.join(regexp.tokenize(text_nolinks))
    words = nltk.word_tokenize(onlytext)
    stopwords = nltk.corpus.stopwords.words("portuguese")
    wordslower = [w.lower() for w in words]
    frequency = nltk.FreqDist([word for word in wordslower if
                          word not in stopwords and not is_profane(word)])
    return frequency.most_common(10)


def analyze_tweet_verified(user_id: str, users: list[dict]) -> bool:
    userfound = next((u for u in users if u["id"] == user_id), {"verified": False})
    return userfound["verified"]


def is_profane(text: str) -> bool:
    with open("tweets/profanity_ptbr.txt") as f:
        profane_words = tuple(map(lambda x: x.lower().replace('\n', ''), f.readlines()))
    return text.startswith(profane_words)


if __name__ == "__main__":
    print(is_similar("S@o Pa*lo", "São Paulo"))
    print(is_similar("S@o Paulo", "São Paulo"))
