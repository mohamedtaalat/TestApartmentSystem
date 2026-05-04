🏢 Apartment System Testing Framework

A comprehensive automated testing framework for the Apartment Rental System, combining UI testing, API testing, and data-driven testing using modern Python tools.

🚀 Tech Stack
🧪 Test Framework: Pytest
🌐 UI Automation: Selenium WebDriver
🔗 API Testing: Requests
📊 Data-Driven Testing: Pytest parametrization / DDT
🐍 Language: Python
📂 Project Structure
TestApartmentSystem/
│
├── tests/
│   ├── ui/                # Selenium UI test cases
│   ├── api/               # API test cases using requests
│   ├── data/              # Test data (JSON, CSV, etc.)
│
├── pages/                 # Page Object Model (POM)
├── utils/                 # Helpers (config, drivers, etc.)
├── conftest.py            # Pytest fixtures
├── requirements.txt       # Dependencies
├── pytest.ini             # Pytest configuration
└── README.md
⚙️ Installation
Clone the repository:
git clone https://github.com/mohamedtaalat/TestApartmentSystem.git
cd TestApartmentSystem
Create virtual environment:
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
Install dependencies:
pip install -r requirements.txt
▶️ Running Tests
Run all tests
pytest -v
Run UI tests only
pytest tests/ui -v
Run API tests only
pytest tests/api -v
Run specific test file
pytest tests/ui/test_login.py -v
🌐 UI Testing (Selenium)
Uses Page Object Model (POM) for maintainability
Supports browser automation (Chrome, Edge, etc.)
Covers main flows like:
Login / Register
Apartment listing
Booking actions
Example
def test_login_valid(driver):
    login_page = LoginPage(driver)
    login_page.login("test@example.com", "123456")
    assert login_page.is_logged_in()
🔗 API Testing (Requests)
Tests backend endpoints directly
Validates:
Status codes
Response body
Authentication
Example
import requests

def test_get_apartments():
    response = requests.get("http://localhost:5000/api/apartments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
📊 Data-Driven Testing (DDT)

Supports running the same test with multiple datasets.

Example using pytest parametrize:
import pytest

@pytest.mark.parametrize("email,password", [
    ("valid@test.com", "123456"),
    ("invalid@test.com", "wrongpass"),
])
def test_login(email, password):
    assert login(email, password) is not None
🧩 Fixtures (Pytest)

Reusable setup & teardown logic:

WebDriver setup
Base URL configuration
Authentication tokens

Example:

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
📈 Reporting

Run with HTML report:

pytest --html=report.html
🛠️ Best Practices Used
Page Object Model (POM)
Separation of concerns (UI / API / Data)
Reusable fixtures
Clean test structure
Scalable architecture
🤝 Contribution
Fork the repo
Create a new branch
Commit changes
Open Pull Request
📌 Future Improvements
CI/CD integration (GitHub Actions)
Allure reporting
Dockerized test execution
Parallel test execution
👨‍💻 Author

Mohamed Talat

⭐ Notes

This project is designed for learning + real-world automation practices, combining frontend and backend testing in one framework.
