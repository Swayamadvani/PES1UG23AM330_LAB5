PYTHON CODE QUALITY AND STATIC ANALYSIS

-- Overview--

This project demonstrates code quality improvement and static analysis using industry-grade Python tools such as Pylint, Flake8, and Bandit.
It focuses on identifying and fixing issues in a given codebase to achieve a perfect 10/10 quality rating and ensure security compliance.
🧠 Objectives
Apply code style and linting tools to assess Python code.
Fix syntax, indentation, and documentation issues.
Detect and mitigate potential security flaws.
Generate structured reports using automation.

🧩 Tools Used
Tool	Purpose
Pylint	Checks code quality, style, and programming errors
Flake8	Detects syntax errors and enforces PEP8 compliance
Bandit	Scans for common security vulnerabilities in Python code



⚙️ Running the Analysis Locally
1. Install the tools
pip install pylint flake8 bandit
2. Run the analysis
pylint cleaned_inventory_system.py > reports/pylint_report.txt
flake8 cleaned_inventory_system.py > reports/flake8_report.txt
bandit -r cleaned_inventory_system.py -f txt -o reports/bandit_report.txt
3. Review reports
All reports are saved inside the reports/ folder.

🏁 Results
All static analysis checks passed successfully.
Final Pylint score: 10.00/10
Code is fully compliant with PEP8 and free from common vulnerabilities.

👨‍💻 Author
Name: Swayam Advani

SRN: PES1UG23AM330

Course: AIML

