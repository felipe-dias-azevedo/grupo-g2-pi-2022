from datetime import date, datetime
from difflib import SequenceMatcher


class Process:
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
