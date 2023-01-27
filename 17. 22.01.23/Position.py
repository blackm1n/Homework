class Position:
    id: int
    title: str

    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title

    def __repr__(self) -> str:
        return f'ID: {self.id}  Должность: {self.title}'

    def export_data(self) -> dict:
        return {"id": self.id, "title": self.title}
