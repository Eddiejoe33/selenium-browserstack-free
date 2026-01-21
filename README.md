## Selenium Automation Framework (Python)

This project is a Selenium-based automation testing framework built with Python and PyTest, following the Page Object Model (POM) design pattern.

### Tech Stack
- Python
- Selenium WebDriver
- PyTest
- GitHub Actions (CI)
- Linux environment

### Framework Structure
- pages/: Page Object classes
- tests/: Test cases
- core/: WebDriver and base test setup
- utils/: Utility and helper functions
- config/: Environment and configuration settings

### How to Run Tests
1. Create a virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Run tests:
   pytest

### CI/CD
Tests are automatically executed using GitHub Actions on push.
