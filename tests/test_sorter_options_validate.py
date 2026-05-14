import pytest

from src.sorter.options_validate import OptionsValidate


class OptionsProbe(OptionsValidate):
    def __init__(self, catalogs):
        self.catalogs = catalogs
        self.messages = []

    def printf(self, code, *args):
        self.messages.append((code, args))


def test_validate_options_returns_required_and_optional_values():
    probe = OptionsProbe(
        {
            "downloads": {
                "path": "/tmp/downloads",
                "files": ["txt", "pdf"],
                "names": [{"txt": "Texts"}, {"pdf": "Docs"}],
                "ignore": ["skip.txt"],
            }
        }
    )

    path_file, files, ignore, names = probe.validate_options("downloads")

    assert path_file == "/tmp/downloads"
    assert files == ["txt", "pdf"]
    assert ignore == ["skip.txt"]
    assert names == [["txt", "Texts"], ["pdf", "Docs"]]


def test_validate_options_uses_defaults_for_optional_values():
    probe = OptionsProbe(
        {
            "downloads": {
                "path": "/tmp/downloads",
                "files": ["txt"],
            }
        }
    )

    path_file, files, ignore, names = probe.validate_options("downloads")

    assert path_file == "/tmp/downloads"
    assert files == ["txt"]
    assert ignore is None
    assert names == []


def test_validate_options_exits_when_required_option_is_missing():
    probe = OptionsProbe({"downloads": {"path": "/tmp/downloads"}})

    with pytest.raises(SystemExit):
        probe.validate_options("downloads")

    assert ("missing_option", ("files",)) in probe.messages
