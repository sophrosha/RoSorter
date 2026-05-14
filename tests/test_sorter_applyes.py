from src.sorter.applyes import Applies


class AppliesProbe(Applies):
    def __init__(self):
        self.messages = []

    def printf(self, code, *args):
        self.messages.append((code, args))


def test_apply_ignore_removes_all_ignored_files():
    probe = AppliesProbe()
    content = [
        ("one", ".txt"),
        ("two", ".log"),
        ("keep", ".md"),
    ]

    result = probe.apply_ignore(["one.txt", "two.log"], content, "downloads")

    assert result == [("keep", ".md")]
    assert ("found_ignore", ("downloads",)) in probe.messages
    assert ("deleted_ignore", ("one.txt",)) in probe.messages
    assert ("deleted_ignore", ("two.log",)) in probe.messages


def test_apply_ignore_keeps_content_without_ignore_option():
    probe = AppliesProbe()
    content = [("report", ".pdf")]

    result = probe.apply_ignore(None, content, "downloads")

    assert result == content
    assert probe.messages == []


def test_apply_names_removes_files_with_custom_names():
    content = [
        ("invoice", ".pdf"),
        ("photo", ".jpg"),
        ("notes", ".txt"),
    ]
    names = [["invoice", "Docs"], ["photo", "Images"]]

    result = Applies.apply_names(names, content)

    assert result == [("notes", ".txt")]
