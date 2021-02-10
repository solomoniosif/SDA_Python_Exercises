import json

class JSONOutput:
    def __init__(self, *args, **kwargs):
        pass

    def to_json(self):
        return json.dumps(self)


class SimpleRow(dict, JSONOutput):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def _headers(self):
        headers_width = max(len(str(k)) for k in self)
        headers = " | ".join(str(k).center(headers_width) for k in self)
        return f"| {headers} |" 

    def _values(self):
        headers_width = max(len(str(k)) for k in self)
        values = " | ".join(str(k).center(headers_width) for k in self.values())
        return f"| {values} |"

    def table(self):
        return f"{self._headers()}\n{self._values()}"


class SimpleTable(list, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def table(self):
        max_width = 0
        headers_width = max(len(str(k)) for k in self[0])
        max_width = headers_width
        for row in self:
            values_width = max(len(str(v)) for v in row.values())
            if values_width > max_width:
                max_width = values_width
        table = ""
        row_sep = "-+-".join((('-'*max_width).center(max_width) for k in self[0]))
        table += f"+-{row_sep}-+\n"
        headers = " | ".join(str(k).upper().center(max_width) for k in self[0])
        table += f"| {headers} |\n"
        table += f"|-{row_sep}-|\n"
        for i in range(len(self)):
            values = " | ".join(str(v).center(max_width) for v in self[i].values())
            if i == (len(self)):
                table += f"| {values} |"
            table += f"| {values} |\n"
        table += f"+-{row_sep}-+"
        return table


if __name__ == '__main__':
    row = SimpleRow(no=1, name="Mark", surname="O'Connor", nationality="Irish")
    print(row.table())
    print(row.to_json())
    print()

    row2 = SimpleRow(no=2, name="Ronnie", surname="O'Sullivan", nationality="English")
    row3 = SimpleRow(no=3, name="Neil", surname="Robertson", nationality="Australian")
    row4 = SimpleRow(no=4, name="Ding", surname="Junghui", nationality="Chinese")
    row5 = SimpleRow(no=5, name="Jud", surname="Trump", nationality="English")

    table = SimpleTable()
    table.append(row)
    table.append(row2)
    table.append(row3)
    table.append(row4)
    table.append(row5)
    print(table.table())
    print(table.to_json())