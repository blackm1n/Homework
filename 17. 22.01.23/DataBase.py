from Worker import Worker
from Position import Position


class DataBase:
    pos_table: list[Position]
    worker_table: list[Worker]

    def __init__(self) -> None:
        self.pos_table = []
        self.worker_table = []

    def append_worker(self, worker: Worker) -> None:
        self.worker_table.append(worker)
        self.sort_table(self.worker_table)

    def append_position(self, position: Position) -> None:
        self.pos_table.append(position)
        self.sort_table(self.pos_table)

    def remove_worker(self, worker_id: int) -> None:
        for w in self.worker_table:
            if w.id == worker_id:
                self.worker_table.remove(w)

    def remove_position(self, pos_id: int) -> None:
        for p in self.pos_table:
            if p.id == pos_id:
                self.pos_table.remove(p)

    def update_worker(self, worker: Worker) -> None:
        for id, w in enumerate(self.worker_table):
            if w.id == worker.id:
                self.worker_table[id] = worker

    def update_position(self, position: Position) -> None:
        for id, p in enumerate(self.pos_table):
            if p.id == position.id:
                self.pos_table[id] = position

    def search_worker(self, criteria: int, key: str, mode: int) -> str:
        output = ""
        if criteria != 2:
            key = int(key)
        data = [list(worker.export_data().values()) for worker in self.worker_table]
        for i, worker in enumerate(data):
            for j, value in enumerate(worker):
                if j == criteria - 1:
                    if (mode == 0 or mode == 3) and key == value:
                        output += f'{self.worker_table[i]}\n'
                    elif mode == 1 and key <= value:
                        output += f'{self.worker_table[i]}\n'
                    elif mode == 2 and key >= value:
                        output += f'{self.worker_table[i]}\n'
        return output

    def search_position(self, criteria: int, key: str, mode: int) -> str:
        output = ""
        if criteria == 1:
            key = int(key)
        data = [list(position.export_data().values()) for position in self.pos_table]
        for i, position in enumerate(data):
            for j, value in enumerate(position):
                if j == criteria - 1:
                    if (mode == 0 or mode == 3) and key == value:
                        output += f'{self.pos_table[i]}\n'
                    elif mode == 1 and key <= value:
                        output += f'{self.pos_table[i]}\n'
                    elif mode == 2 and key >= value:
                        output += f'{self.pos_table[i]}\n'
        return output

    def sort_table(self, table: list) -> None:
        size = len(table)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if table[j].id < table[min_index].id:
                    min_index = j
            table[i], table[min_index] = table[min_index], table[i]

    def select_table(self, table: int) -> str:
        output: str = ""

        if table == 1:
            for w in self.worker_table:
                output += f'{w}\n'
        elif table == 2:
            for p in self.pos_table:
                output += f'{p}\n'

        return output

    def export_data(self) -> dict:
        output: dict = {"workers": [worker.export_data() for worker in self.worker_table], "positions": [pos.export_data() for pos in self.pos_table]}
        return output
