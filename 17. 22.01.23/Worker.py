class Worker:
    id: int
    full_name: str
    age: int
    salary: int
    pos_id: int

    def __init__(self, id: int, worker_name: str, age: int, salary: int, pos_id: int = 0) -> None:
        self.id = id
        self.full_name = worker_name
        self.age = age
        self.salary = salary
        self.pos_id = pos_id

    def __repr__(self) -> str:
        return f'ID: {self.id}  ФИО: {self.full_name}  Возраст: {self.age}  Зарплата: {self.salary}  ID Должности: {self.pos_id}'

    def export_data(self) -> dict:
        return {"id": self.id, "full_name": self.full_name, "age": self.age, "salary": self.salary, "pos_id": self.pos_id}
