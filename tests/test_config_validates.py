import pytest

from src.config.config import ValidateFileConfig
from src.config.validates import ConfigOptionValidate


class ConfigProbe(ValidateFileConfig, ConfigOptionValidate):
    def __init__(self, input_answer="n"):
        self.messages = []
        self.input_answer = input_answer

    def printf(self, code, *args):
        self.messages.append((code, args))

    def inputf(self, code):
        self.messages.append((code, ()))
        return self.input_answer


def test_contains_values_accepts_required_sections():
    probe = ConfigProbe()
    config = {"settings": {}, "directories": {}}

    assert probe.contains_values(config) is None


def test_contains_values_exits_on_unknown_section():
    probe = ConfigProbe()
    config = {"settings": {}, "directories": {}, "extra": {}}

    with pytest.raises(SystemExit):
        probe.contains_values(config)

    assert ("found_error_option", ("extra",)) in probe.messages


def test_contains_values_exits_when_required_section_is_missing():
    probe = ConfigProbe()
    config = {"settings": {}}

    with pytest.raises(SystemExit):
        probe.contains_values(config)

    assert ("missing_settings_directories", ()) in probe.messages


def test_validate_settings_returns_language_and_settings():
    probe = ConfigProbe()
    settings = {}
    config = {
        "settings": {
            "logging": "ru-RU",
            "logs": True,
            "daemon": False,
            "timeout": "60m",
            "gui": False,
            "silent": True,
        }
    }

    language, result = probe.validate_settings(config, settings)

    assert language == "ru-RU"
    assert result == {
        "logs": True,
        "daemon": False,
        "timeout": "60m",
        "gui": False,
        "silent": True,
    }


def test_validate_settings_exits_on_unknown_option():
    probe = ConfigProbe()
    config = {"settings": {"unknown": True}}

    with pytest.raises(SystemExit):
        probe.validate_settings(config, {})

    assert ("mission_option", ("unknown",)) in probe.messages


def test_validate_directories_returns_known_options():
    probe = ConfigProbe()
    catalogs = {}
    config = {
        "directories": {
            "downloads": {
                "path": "/tmp/downloads",
                "files": ["txt"],
                "names": [{"txt": "Docs"}],
                "ignore": ["skip.txt"],
            }
        }
    }

    result = probe.validate_directories(config, catalogs)

    assert result == {
        "downloads": {
            "path": "/tmp/downloads",
            "files": ["txt"],
            "names": [{"txt": "Docs"}],
            "ignore": ["skip.txt"],
        }
    }


def test_validate_directories_exits_on_unknown_option():
    probe = ConfigProbe()
    config = {
        "directories": {
            "downloads": {
                "path": "/tmp/downloads",
                "files": ["txt"],
                "wrong": True,
            }
        }
    }

    with pytest.raises(SystemExit):
        probe.validate_directories(config, {})

    assert ("found_error_option_dir", ("wrong", "downloads")) in probe.messages


def test_validate_catalogs_creates_missing_directory_when_user_confirms(tmp_path):
    target = tmp_path / "downloads"
    probe = ConfigProbe(input_answer="y")
    catalogs = {"downloads": {"path": str(target)}}

    probe.validate_catalogs(catalogs)

    assert target.is_dir()
    assert ("create_catalog", ()) in probe.messages
    assert ("creating_catalog", ()) in probe.messages
