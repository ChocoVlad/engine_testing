# QA Automation Engineer – Test Assignment #2 (V. Kazarin)

## Project Structure

```
 ├── helpers
 │   └── output_helper.py               # Helper functions for processing output data
 ├── checkers
 │   ├── figure_checker.py              # Helper utilities for figure data
 │   └── test_checker.py                # Helper functions for test assertions
 ├── engine2d
 │   ├── engine.py                      # Core engine functionality for 2D drawing
 │   └── figures
 │       ├── base_figure.py             # Base class for all figures
 │       └── {some_figure}.py           # Specific figure implementations
 ├── tests
 │   └── integration
 │        ├── test_engine.py            # Integration tests for engine
 │        ├── test_figures.py           # Integration tests for figures
 │   └── unit
 │        ├── test_engine.py            # Unit tests for engine
 │        ├── test_figures.py           # Unit tests for figures
 └── README.md
```

## Running the Tests

1. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install the dependencies**

```bash
pip install -r requirements.txt
```

3. **Run unit tests**

```bash
pytest --alluredir=allure-results ./tests/unit/
```

4. **Run integration tests**

```bash
pytest --alluredir=allure-results ./tests/integration/
```

## Allure Report

1. **Install Allure**

```bash
brew install allure
```

1. **Run allure server**

```bash
allure serve allure-results
```