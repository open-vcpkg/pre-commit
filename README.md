# vcpkg precommit hooks

This repository provides [vcpkg](https://vcpkg.io/) hooks for [pre-commit](https://pre-commit.com/).

The following section assumes that you [installed pre-commit](https://pre-commit.com/index.html#install) and run `pre-commit install` in your repository.

## Features

- Formats manifests using the vcpkg `format-manifest` command
- Automatically downloads the appropriate vcpkg binary for your platform
- Cross-platform support (Windows, Linux, macOS)
- Works with x64 and ARM64 architectures
- Caches the vcpkg binary for better performance

## Installation

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/open-vcpkg/pre-commit
    rev: v1.0.0  # Use the ref you want to point at
    hooks:
    -   id: vcpkg-format-manifest
```

## Usage

Once installed, the hook will automatically run on any commits that modify `vcpkg.json` files.

You can also run the hook manually:

```bash
pre-commit run vcpkg-format-manifest --all-files
```

## Development

To contribute to this hook:

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
4. Install pre-commit:
   ```bash
   pre-commit install
   ```

## License

MIT
