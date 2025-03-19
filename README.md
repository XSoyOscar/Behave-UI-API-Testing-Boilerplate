# 🧪 Behave UI & API Testing Boilerplate 🚀

A **Behave** boilerplate designed to streamline the creation of UI and API test automation frameworks. 
This repository serves as a foundation for building scalable and maintainable test automation solutions, utilizing:

- ✅ **Page Object Model (POM)** for UI automation with **Selenium**
- ✅ **API testing with Requests**
- ✅ **Configurable settings in a Python class**
- ✅ **Built-in logging** for debugging
- ✅ **Allure Reports for detailed test results**
- ✅ **Headless execution support**
- ✅ **Modular and scalable structure**
- ✅ **Compatible with CI/CD (GitHub Actions, GitLab, Jenkins)**

This boilerplate uses **[OrangeHRM Demo](https://opensource-demo.orangehrmlive.com)** for UI testing and **[ReqRes](https://reqres.in/api)** as the reference API.

---

## 📺 Project Structure

```
📦 Behave-UI-API-Testing-Boilerplate
└── 📂 api_clients    # API interaction logic (Base & Users)
   ├── 📚 base_api.py
   └── 📚 users_api.py
├── 📂 features           # Behave test scenarios
   ├── 📂 api              # API tests
   │   └── 📚 users.feature
   ├── 📂 ui               # UI tests
   │   └── 📚 login.feature
   ├── 📂 steps            # Step definitions for Behave
   │   ├── 📚 api_steps.py
   │   └── 📚 ui_steps.py
   ├── 📚 environment.py   # Global Behave configurations
├── 📂 pages              # Page Object Model (Selenium)
   ├── 📚 base_page.py
   └── 📚 login_page.py
├── 📂 reports            # Test execution reports
   └── 📂 allure-results
├── 📂 utils              # Utility files (config, logging, helpers)
   ├── 📚 config.py
   ├── 📚 logger.py
├── 📚 behave.ini         # Behave configuration
├── 📚 requirements.txt   # Dependencies
├── 📚 test_execution.log # Execution logs
├── 📚 LICENSE            # License
├── 📚 .gitignore         # Files to ignore in Git
└── 📚 README.md          # Documentation
```

---

## 🛠️ Installation

1️⃣ **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/behave-ui-api-boilerplate.git
   cd behave-ui-api-boilerplate
   ```

2️⃣ **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3️⃣ **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

Edit **`config.py`** to set up test settings:
```python
class Config:
    BROWSER = "chrome"  # Options: chrome, firefox
    BASE_URL = "https://opensource-demo.orangehrmlive.com" # UI Base URL
    API_URL = "https://reqres.in/api"  # API Base URL
    HEADLESS = True  # Run UI tests in headless mode
    LOG_LEVEL = "INFO"  # Logging level (DEBUG, INFO, ERROR)
```

---

## 🚀 Running Tests

### ✅ **Run UI Tests**
```bash
behave --tags=ui
```

### ✅ **Run API Tests**
```bash
behave --tags=api
```

### ✅ **Run All Tests**
```bash
behave
```

---

## 📊 Generating Test Reports

### 🏆 **Using Allure Reports (Recommended)**
**Install Allure if you haven't:**
```bash
pip install allure-behave
```

**Run tests and generate reports:**
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

**To view reports in the browser:**
```bash
allure serve reports/allure-results
```

---

## 📝 License
This project is licensed under the **MIT License**. Feel free to use and modify it!

---

## 🤝 Contributions
💡 **Want to improve this project?** Feel free to **open an issue** or submit a **pull request**. 🚀

