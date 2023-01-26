class Number:
    id: int
    person_id: int
    phone_number: int
    comment: str

    def __init__(self, id: int, person_id: int, phone_number: int, comment: str) -> None:
        self.id = id
        self.person_id = person_id
        self.phone_number = phone_number
        self.comment = comment

    def __repr__(self) -> str:
        return f'id: {self.id}  Чей телефон: {self.person_id}  Тел: {self.phone_number}  Коммент: {self.comment}'

    def export_data(self) -> dict:
        return {"id": self.id, "person_id": self.person_id, "phone_number": self.phone_number, "comment": self.comment}
