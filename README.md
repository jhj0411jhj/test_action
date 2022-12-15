# test_action

[![GitHub Actions Demo](https://github.com/jhj0411jhj/test_action/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/jhj0411jhj/test_action/actions/workflows/github-actions-demo.yml)

This is a repo for testing Github Actions.

This is the `README.md` file.

## For Python Packaging

See [pyproject.toml](pyproject.toml) and [MANIFEST.in](MANIFEST.in).

Tutorial:
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://setuptools.pypa.io/en/latest/userguide/quickstart.html

Commands:
```bash
# Build
python -m build --sdist --wheel

# Check
tar tf dist/*.tar.gz
unzip -l dist/*.whl
twine check dist/*

# Upload
twine upload --repository testpypi dist/*

# Install
pip install -i https://test.pypi.org/simple/ ${package_name}
```

## For pytest

See `[tool.pytest.ini_options]` in [pyproject.toml](pyproject.toml).

Example command:
```bash
pytest -rap test
pytest -h  # show help
```

Documentation: https://docs.pytest.org/

## For GitHub Actions

See [.github/workflows](.github/workflows).

Tutorial: https://docs.github.com/en/actions/quickstart

End of README.md
