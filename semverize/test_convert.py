import pytest
from . import pep440_to_semver


def test_pep440_to_semver() -> None:
    assert pep440_to_semver("1.0.0") == "1.0.0"
    assert pep440_to_semver("1.0.0a1") == "1.0.0-alpha.1"
    assert pep440_to_semver("1.0.0b1") == "1.0.0-beta.1"
    assert pep440_to_semver("1.0.0rc1") == "1.0.0-rc.1"
    assert pep440_to_semver("1.0.0.dev1") == "1.0.0+dev.1"
    assert pep440_to_semver("1.0.0b1.dev1") == "1.0.0-beta.1+dev.1"
    assert pep440_to_semver("1.0.0a1.dev1") == "1.0.0-alpha.1+dev.1"
    assert pep440_to_semver("1.0.0rc1.dev1") == "1.0.0-rc.1+dev.1"
    assert pep440_to_semver("1.0") == "1.0.0"
    assert pep440_to_semver("1") == "1.0.0"


def test_pep440_to_semver_errors() -> None:
    with pytest.raises(
        ValueError,
        match="Can't convert a PEP 440 version with a local component to SemVer",
    ):
        pep440_to_semver("1.0.0+local")
    with pytest.raises(
        ValueError,
        match="Can't convert a PEP 440 version with a non-zero epoch to SemVer",
    ):
        pep440_to_semver("1!1.0.0")
    with pytest.raises(
        ValueError,
        match="Can't convert a PEP 440 version with a post component to SemVer",
    ):
        assert pep440_to_semver("1.0.0.post1") == "1.0.0+post.1"
