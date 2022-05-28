from datetime import date, datetime

class Process:
    
    def get_age_from_birthdate(self, birthdate: str) -> int:
        born = datetime.strptime(birthdate, '%d/%m/%Y')
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get_label_from_floatbool(self, label: float) -> str:
        return "Sim" if label >= 1 else "Não"