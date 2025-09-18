# Python CI/CD Demo

<!-- Build Status -->
[![CI Pipeline](https://github.com/username/python-cicd-demo/workflows/CI%20Pipeline/badge.svg)](https://github.com/username/python-cicd-demo/actions)
[![Security Analysis](https://github.com/username/python-cicd-demo/workflows/Security%20Analysis/badge.svg)](https://github.com/username/python-cicd-demo/actions)
[![Documentation](https://github.com/username/python-cicd-demo/workflows/Documentation/badge.svg)](https://github.com/username/python-cicd-demo/actions)
[![Release](https://github.com/username/python-cicd-demo/workflows/Release/badge.svg)](https://github.com/username/python-cicd-demo/actions)

<!-- Code Quality -->
[![codecov](https://codecov.io/gh/username/python-cicd-demo/branch/main/graph/badge.svg)](https://codecov.io/gh/username/python-cicd-demo)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<!-- Version and Dependencies -->
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-blue.svg)](https://python-poetry.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- Project Info -->
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue.svg)](https://username.github.io/python-cicd-demo/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/)
[![Renovate](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)

A comprehensive Python CI/CD demonstration project showcasing modern software engineering best practices, automated testing, security scanning, and deployment strategies.

## 🎯 Project Overview

This repository serves as a hands-on guide for beginners to learn professional software development workflows. It demonstrates:

- **Modern Python Development**: Poetry for dependency management, src layout, type hints
- **Automated Quality Assurance**: Pre-commit hooks, linting, security scanning, comprehensive testing
- **CI/CD Pipeline**: GitHub Actions workflows for testing, security, releases, and documentation
- **Documentation**: Sphinx-generated docs with automatic deployment to GitHub Pages
- **Containerization**: Docker best practices with multi-stage builds and security hardening

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/docs/#installation)
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/python-cicd-demo.git
   cd python-cicd-demo
   ```

2. **Install dependencies**:
   ```bash
   make install
   ```

3. **Run the application**:
   ```bash
   poetry run python -m python_cicd_demo.main
   ```

4. **Run tests**:
   ```bash
   make test
   ```

## 📁 Project Structure

```
├── .github/
│   ├── workflows/          # GitHub Actions CI/CD pipelines
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── pull_request_template.md
├── src/
│   └── python_cicd_demo/   # Main application code
├── tests/                  # Test suite
├── docs/                   # Sphinx documentation
├── .pre-commit-config.yaml # Pre-commit hook configuration
├── pyproject.toml          # Poetry configuration and project metadata
├── Dockerfile             # Container configuration
└── Makefile               # Development commands
```

## 🛠 Development Workflow

### Available Commands

```bash
make help          # Show all available commands
make install       # Install dependencies and pre-commit hooks
make test          # Run tests with coverage
make lint          # Run linting and security checks
make format        # Format code with black and isort
make docs          # Build documentation
make clean         # Clean build artifacts
```

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality:

- **Code Formatting**: Black, isort
- **Security Scanning**: Bandit
- **General Quality**: Trailing whitespace, YAML validation, large file checks

Install hooks after cloning:
```bash
poetry run pre-commit install
```

## 🔧 CI/CD Pipeline

### Workflows

1. **CI Pipeline** (`.github/workflows/ci.yml`):
   - Runs on every push and pull request
   - Linting and security scanning
   - Multi-version Python testing (3.8, 3.9, 3.10, 3.11)
   - Code coverage reporting

2. **Security Analysis** (`.github/workflows/security.yml`):
   - CodeQL static analysis
   - Dependency review for pull requests
   - Scheduled weekly security scans

3. **Release** (`.github/workflows/release.yml`):
   - Automated semantic versioning
   - Changelog generation
   - Package building and artifact uploads

4. **Documentation** (`.github/workflows/docs.yml`):
   - Sphinx documentation building
   - Automatic deployment to GitHub Pages

### Environment Setup

Create the following secrets in your GitHub repository:

- `CODECOV_TOKEN`: For code coverage reporting
- Additional secrets as needed for your specific deployment targets

## 🧪 Testing Strategy

The project implements a comprehensive testing approach:

- **Unit Tests**: Fast, isolated tests for individual functions
- **Integration Tests**: Testing component interactions
- **Coverage Reporting**: Minimum 80% coverage requirement
- **Property-Based Testing**: Using Hypothesis for edge case discovery

Run specific test types:
```bash
poetry run pytest tests/unit/           # Unit tests only
poetry run pytest tests/integration/    # Integration tests only
poetry run pytest --cov-report=html     # Generate HTML coverage report
```

## 🔒 Security

Security is integrated throughout the development lifecycle:

- **Static Analysis**: Bandit for Python security issues
- **Dependency Scanning**: GitHub's Dependabot and dependency review
- **Secret Scanning**: GitHub's secret scanning enabled
- **Container Security**: Non-root user, minimal base image, security patches

## 📚 Documentation

Documentation is automatically built and deployed to GitHub Pages:

- **API Documentation**: Auto-generated from docstrings
- **User Guides**: Comprehensive guides for setup and usage
- **Best Practices**: Explanations of CI/CD patterns and decisions

View documentation locally:
```bash
make docs
make docs-serve  # Serve on http://localhost:8000
```

## 🐳 Docker Support

Build and run the containerized application:

```bash
docker build -t python-cicd-demo .
docker run -p 8000:8000 python-cicd-demo
```

The Docker image follows security best practices:
- Non-root user
- Minimal attack surface
- Health checks
- Multi-stage builds (when applicable)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure they pass (`make test`)
5. Run linting (`make lint`) and fix any issues
6. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
7. Push to your fork and submit a pull request

### Conventional Commits

This project uses Conventional Commits for automated versioning:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Python Poetry](https://python-poetry.org/) for dependency management
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [Sphinx](https://www.sphinx-doc.org/) for documentation
- [pytest](https://pytest.org/) for testing framework
- The Python community for excellent tooling and best practices

## 📞 Support

- **Documentation**: [Project Documentation](https://username.github.io/python-cicd-demo/)
- **Issues**: [GitHub Issues](https://github.com/username/python-cicd-demo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/username/python-cicd-demo/discussions)

---

**Note**: This is a demonstration project designed for educational purposes. Please replace placeholder values (like `username` in URLs) with your actual repository information.
