import pytest
import shlex
from src.argparse_yaml_reader import arguments
from typer.testing import CliRunner
from src.typer_yaml_reader import app

# Fixture to get user inputs
@pytest.fixture
def get_user_input(request):
    yaml_location = str(request.config.getoption("--yaml_location"))
    expected_output = str(request.config.getoption("--expected_output"))
    return yaml_location, expected_output


# Testing argparse_yaml_reader()
def test_argparse_yaml_reader(capsys, get_user_input):
    yaml_location, expected_output = get_user_input
    arguments(shlex.split(yaml_location))
    output = capsys.readouterr().out.rstrip()
    assert output == expected_output

runner = CliRunner()

# Testing typer_yaml_reader()
def test_typer_yaml_reader(get_user_input):
    yaml_location, expected_output = get_user_input
    result = runner.invoke(app, shlex.split(yaml_location))
    assert result.exit_code == 0
    assert expected_output in result.stdout

