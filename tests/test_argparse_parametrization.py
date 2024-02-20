from src.argparse_yaml_reader import main
import pytest
import shlex

test_cases = [
    (
        "--configpath 'src/yaml_configs/config.yml'",  # Valid path
        "{'rest': {'url': 'https://example.com/', 'port': 3001}, 'details': 'A Demo Website'}",
    ),
    (
        "--configpath 'path/to/nonexistent/file.yml'",  # Nonexistent file
        "`configpath` must be a valid file path. Provided path: `path/to/nonexistent/file.yml` does not exist.",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_cases)
def test_argparse_yaml_reader(capsys, command, expected_output):
    main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert expected_output in output


# Test cases
test_cases_sys_exit = [
    (
        "",  # No argument passed
        "the following arguments are required: --configpath",
    ),
    (
        "--wrong_argument 'src/yaml_configs/config.yml'",  # Wrong argument name
        "the following arguments are required: --configpath",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_argparse_yaml_reader_sys_exit(capsys, command, expected_output):
    with pytest.raises(SystemExit):  # Expecting SystemExit due to argparse error
        main(shlex.split(command))
    captured = capsys.readouterr()  # Capture both stdout and stderr
    output = captured.out + captured.err  # Combine stdout and stderr
    assert expected_output in output
