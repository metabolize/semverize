# semverize

[![version](https://img.shields.io/pypi/v/semverize?style=flat-square)][pypi]
[![python version](https://img.shields.io/pypi/pyversions/semverize?style=flat-square)][pypi]
[![license](https://img.shields.io/pypi/l/semverize?style=flat-square)][pypi]
![](https://img.shields.io/badge/coverage-100%25-brightgreen?style=flat-square)
![types](https://img.shields.io/badge/types-mypy-brightgreen?style=flat-square)

Coerce PEP 440 to SemVer, when possible.

[pypi]: https://pypi.org/project/semverize/


## Usage

```pyconsole
pep440_to_semver("1.0a2")
> "1.0.0-alpha.2"
```


```console
$ semverize 1.0a2
1.0.0-alpha.2

$ semverize bargle
Error: Invalid version: 'bargle'
```


## License

The project is licensed under the Apache License, Version 2.0.
