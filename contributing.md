# Contributing to TalentHawk

Thank you for your interest in contributing to TalentHawk! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by creating an issue on our GitHub repository. When filing an issue, please include:

- A clear and descriptive title
- A detailed description of the issue
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment information (OS, browser, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for enhancements! Please create an issue on our GitHub repository with:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Any relevant examples, mockups, or screenshots
- An explanation of why this enhancement would be useful

### Pull Requests

We actively welcome pull requests:

1. Fork the repository
2. Create a new branch from `main`
3. Make your changes
4. Run tests to ensure they pass
5. Submit a pull request to the `main` branch

### Development Setup

1. Clone your fork of the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
3. Run tests to ensure everything is working:
   ```bash
   python -m unittest discover -s tests
   ```

### Coding Style

Please follow these guidelines for code style:

- Use [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use 4 spaces for indentation (not tabs)
- Use descriptive variable and function names
- Comment your code as needed
- Keep functions and methods focused on a single responsibility

### Testing

All new features and bug fixes should include tests. We use the `unittest` framework for testing.

### Documentation

Changes to functionality should be documented. We use Markdown for documentation.

## Pull Request Process

1. Update the README.md or documentation with details of changes to the interface, if applicable.
2. Update the tests to cover your changes.
3. The PR should work for Python 3.8, 3.9, and 3.10.
4. Write a clear PR description explaining the changes you've made.

## License

By contributing to TalentHawk, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
