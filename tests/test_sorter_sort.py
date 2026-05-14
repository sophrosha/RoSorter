from src.sorter.sort import Sort


class SortProbe(Sort):
    def __init__(self):
        self.copied = []
        self.messages = []

    def printf(self, code, *args):
        self.messages.append((code, args))

    def code_return(self, code, *args):
        return code.format(*args) if args else code

    def copy(self, file_name, path, name_folder):
        self.copied.append((file_name, path, name_folder))


class FakeTqdm:
    def __init__(self, iterable, position=0):
        self.iterable = iterable
        self.position = position
        self.descriptions = []

    def __iter__(self):
        return iter(self.iterable)

    def set_description(self, description):
        self.descriptions.append(description)


def test_sort_skips_extensions_not_listed_when_names_use_wildcard(monkeypatch):
    monkeypatch.setattr("src.sorter.sort.tqdm", FakeTqdm)
    monkeypatch.setattr("src.sorter.sort.sleep", lambda seconds: None)
    probe = SortProbe()

    probe.sort(
        [("report", ".pdf"), ("notes", ".txt")],
        "/downloads",
        ["txt"],
        [["*", "*"]],
    )

    assert probe.copied == [("notes.txt", "/downloads", "txt")]


def test_sort_moves_all_files_when_files_use_wildcard(monkeypatch):
    monkeypatch.setattr("src.sorter.sort.tqdm", FakeTqdm)
    monkeypatch.setattr("src.sorter.sort.sleep", lambda seconds: None)
    probe = SortProbe()

    probe.sort(
        [("report", ".pdf"), ("notes", ".txt")],
        "/downloads",
        ["*"],
        [["*", "*"]],
    )

    assert probe.copied == [
        ("report.pdf", "/downloads", "pdf"),
        ("notes.txt", "/downloads", "txt"),
    ]
