🎭 UI Automation – Playwright Framework

🔹 Project Overview

This repository contains a UI Automation Testing framework built using Playwright.
The framework is designed to automate web application testing with fast execution, reliable assertions, and clean test structure.

This project demonstrates my hands-on experience in UI automation, modern testing tools, and automation best practices, suitable for QA / Automation Engineer roles.

🔹 Tech Stack & Tools

Automation Tool: Playwright

Programming Language: Python

Test Runner: Playwright Test

Assertions: Built-in Playwright assertions

Browser Support: Chromium, Firefox, WebKit

IDE:  PyCharm

Version Control: Git & GitHub

CI Ready: Yes (Jenkins)

🔹 Framework Structure
UI_Automation_Playwright
│
├── tests/               → Test scenarios
├── pages/               → Page Object Model (POM)
├── utils/               → Reusable utilities
├── test-data/           → Test data files
├── playwright.config.js → Playwright configuration
├── package.json         → Dependencies and scripts
└── README.md            → Project documentation

🔹 Key Features Implemented

UI automation using Playwright

Page Object Model (POM) design

Cross-browser testing (Chromium, Firefox, WebKit)

Auto-waiting for elements (stable tests)

Screenshot and video capture on failure

Headless and headed execution support

Reusable test utilities and configuration

🔹 Sample Test Scenarios Covered

User login and logout flow

Form validations

Navigation and UI element verification

Positive and negative test cases

Handling alerts, popups, and waits

Responsive UI testing (if applicable)

🔹 How to Run the Project

Clone the repository:

git clone <repository-url>


Install dependencies:

npm install


Run all tests:

npx playwright test


Run tests in headed mode:

npx playwright test --headed


View test report:

npx playwright show-report
