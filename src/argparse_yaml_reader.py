import yaml
from typing import Dict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def parse_args(args=None) -> ArgumentParser.parse_args:
    """
    Function to parse command line arguments

    Args:
    args: list of strings to parse

    Returns:
    parsed_args: parsed arguments
    """
    argument_parser = ArgumentParser(
        description="Command line arguments for reading a configuration file",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    argument_parser.add_argument(
        "--configpath", type=str, help="Configuration file path"
    )
    return argument_parser.parse_args(args)


def yaml_reader(path: str) -> Dict:
    """
    Function to read YAML config file

    Args:
    path: path to the YAML file

    Returns:
    data: dictionary of data from the YAML file
    """
    try:
        with open(path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data
    except Exception as e:
        print(f"Error reading YAML file: {e}")


def main() -> None:
    """
    Main function to read YAML file
    """
    args = parse_args()
    configpath = args.configpath
    print(yaml_reader(path=configpath))


if __name__ == "__main__":
    main()