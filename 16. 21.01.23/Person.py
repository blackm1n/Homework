import datetime as dt


class Person:
    id: int
    full_name: str
    birth_date: dt.date
    status: str

    def __init__(self, id: int, full_name: str, birth_date: dt.date, status: str) -> None:
        self.id = id
        self.full_name = full_name
        self.birth_date = birth_date
        self.status = status

    def __repr__(self) -> str:
        return f'id: {self.id}  ФИО: {self.full_name}  Д/р: {self.birth_date}  Статус: {self.status}'

    def export_data(self) -> dict:
        return {"id": self.id, "full_name": self.full_name, "birth_date": str(self.birth_date), "status": self.status}
