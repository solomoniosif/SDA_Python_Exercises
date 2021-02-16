import json


class JSONOutput:
    def __init__(self, *args, **kwargs):
        pass

    def to_json(self):
        return json.dumps(self)


class SimpleRow(dict, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _headers(self):
        header_width = max(len(str(k)) for k in self)
        headers = " | ".join(str(k).center(header_width) for k in self)
        return f"| {headers} |"

    def _values(self):
        header_width = max(len(str(k)) for k in self)
        values = " | ".join(str(v).center(header_width) for v in self.values())
        return f"| {values} |"

    def table(self):
        return f"{self._headers()}\n{self._values()}"


class SimpleTable(list, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def table(self):
        if len(self) == 0:
            return
        rows = (r._values() for r in self)
        return "\n".join([self[0]._headers(), *rows])


if __name__ == "__main__":
    table = SimpleTable()
    table.extend(
        [
            SimpleRow(no=1, name="Mark", surname="O'Connor", nationality="Irish"),
            SimpleRow(no=2, name="Adam", surname="Kowalski", nationality="Polish"),
            SimpleRow(no=3, name="Doria", surname="Alvarado", nationality="Spanish"),
        ]
    )
    print(table.table())
    print(table.to_json())
