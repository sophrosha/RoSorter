from src.sorter.copy import Copy


class CopyProbe(Copy):
    def __init__(self):
        self.messages = []

    def printf(self, code, *args):
        self.messages.append((code, args))


def test_copy_moves_file_to_created_directory(tmp_path):
    source = tmp_path / "report.txt"
    source.write_text("content", encoding="utf-8")
    probe = CopyProbe()

    probe.copy("report.txt", str(tmp_path), "Docs")

    assert not source.exists()
    assert (tmp_path / "Docs" / "report.txt").read_text(encoding="utf-8") == "content"
    assert ("found_error_catalog", ("report.txt",)) in probe.messages
