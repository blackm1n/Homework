class Address:
    id: int
    person_id: int
    address_name: str
    comment: str

    def __init__(self, id: int, person_id: int, address_name: str, comment: str) -> None:
        self.id = id
        self.person_id = person_id
        self.address_name = address_name
        self.comment = comment

    def __repr__(self) -> str:
        return f'id: {self.id}  Чей адрес: {self.person_id}  Адрес: {self.address_name}  Комментарий: {self.comment}'

    def export_data(self) -> dict:
        return {"id": self.id, "person_id": self.person_id, "address_name": self.address_name, "comment": self.comment}
