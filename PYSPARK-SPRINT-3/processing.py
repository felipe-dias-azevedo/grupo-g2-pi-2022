import unicodedata
from datetime import date, datetime
from difflib import SequenceMatcher

from pandas import DataFrame


class Process:
    def words_in_tweet(self, tweet: list):
        only_words_tweets = []
        for words in tweet:
            onlywords = []
            for word in words:
                onlywords.append(word[0])
            only_words_tweets.append(onlywords)
        return only_words_tweets

    def freq_tweet(self, tweets: DataFrame):
        frequency = []
        for tweet in tweets:
            count = tweet[1]
            for t in tweets:
                if t[0] == tweet[0]:
                    count += t[1]
            frequency.append([tweet[0], count])
        return frequency

    def no_accents_lower(self, text: str):
        noaccent = self.remove_special_chars(text)
        return noaccent.lower()
    
    def remove_special_chars(self, text: str):
        try:
            text = unicode(text, 'utf-8')
        except NameError:
            pass
        text = unicodedata.normalize('NFD', text) \
            .encode('ascii', 'ignore') \
            .decode("utf-8")
        return str(text)
    
    def get_date(datestr: str):
        return datetime.strptime(datestr[:-5], "%Y-%m-%dT%H:%M:%S")
    
    def is_similar(self, string_a: str, string_b: str, percentage=0.8) -> bool:
        sm = SequenceMatcher(a=string_a, b=string_b)
        return sm.ratio() >= percentage

    def get_age_from_birthdate(self, birthdate: str) -> int:
        born = datetime.strptime(birthdate, '%d/%m/%Y')
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_label_from_floatbool(self, label: float) -> str:
        return "Sim" if label >= 1 else "Não"


if __name__ == "__main__":
    p = Process()
    print(p.is_similar("S@o Pa*lo", "São Paulo"))
    print(p.is_similar("S@o Paulo", "São Paulo"))
