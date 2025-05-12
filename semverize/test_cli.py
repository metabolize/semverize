from click.testing import CliRunner
from .cli import semverize


def test_cli_coercible() -> None:
    runner = CliRunner()
    result = runner.invoke(
        semverize,
        ["1.0"],
    )
    assert result.exit_code == 0
    assert result.output == "1.0.0"


def test_cli_not_coercible() -> None:
    runner = CliRunner()
    result = runner.invoke(
        semverize,
        ["1.0.post1"],
    )
    assert result.exit_code == 1
    assert (
        result.output.strip()
        == "Error: Can't convert a PEP 440 version with a post component to SemVer"
    )
