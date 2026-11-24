# test_app.py
import runpy
from pathlib import Path

import app

APP_PATH = Path(app.__file__)


def test_main_prints_greeting(capsys):
    app.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Jenkins!\n"
    assert captured.err == ""


def test_main_returns_none():
    assert app.main() is None


def test_running_as_script_calls_main(capsys):
    runpy.run_path(str(APP_PATH), run_name="__main__")
    assert capsys.readouterr().out == "Hello, Jenkins!\n"


def test_importing_module_does_not_run_main(capsys):
    runpy.run_path(str(APP_PATH), run_name="app")
    assert capsys.readouterr().out == ""
