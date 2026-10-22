# 🎓 Student Lab Portfolio — BCA AI (2026 Batch)

**Student Name:** JYOTI BHATT  
**Roll Number:** `2610997404`  
**Section:** Section E  
**Batch:** BCA AI 2026 Batch  
**Repository:** `sec-e-2610997404-jyoti`  

---

## 🚀 Initial Setup (One-time only)

When you start for the first time, open your terminal (Command Prompt, PowerShell, or Git Bash) and clone this repository to your laptop/system:

```bash
git clone https://github.com/chitkara-bca-ai-2026/sec-e-2610997404-jyoti.git
```
*(After cloning, open the cloned folder in VS Code via **File → Open Folder**)*

---

## 📂 Repository Structure

This repository is your central coursework portfolio across lab courses. Keep your work organized inside their respective subject folders:

* **`Python/`** — Python Programming lab assignments and solutions.
* **`CST/`** — Client Side Technology (HTML, CSS, JS) lab exercises.

```text
sec-e-2610997404-jyoti/
├── README.md
│
├── Python/                                  <--- [Python Programming]
│   ├── Lab_01/
│   │   └── solution.py                      (No log needed for past labs)
│   ├── ...
<<<<<<< HEAD
│   └── Lab_09/
│       ├── solution.py                      (Write clean, complete code)
│       └── output.txt                       (Run solution.py and paste output)
│
└── CST/                                     <--- [Client Side Technology]
    ├── HTML/
    │   └── Exercise_01/
    │       └── index.html
    └── CSS/
=======
│   ├── Lab_13/
│   │   ├── solution.py                      (Python program)
│   │   └── log.txt                          (Error & reflection log - Python only)
│   └── Lab_14/
│       ├── solution.py
│       └── log.txt
│
└── CST/                                     <--- [Client Side Technologies]
    ├── Lab_01/
    │   ├── html/
    │   │   └── index.html                   (HTML files inside html/)
    │   └── images/
    │       └── banner.png                   (Images inside images/)
    └── Lab_02/
        ├── html/
        │   └── index.html
        └── images/
            └── logo.png
>>>>>>> 0e9c4c11971356ac5907ff2195aa9e279d545a34
```

---

<<<<<<< HEAD
## 📌 Submission Workflow

Whenever you complete a new lab experiment:

1. Create a lab subfolder inside the appropriate subject folder (e.g. `Python/Lab_09/` or `CST/HTML/Lab_01/`).
2. Add your solution code file (`solution.py` or `index.html`).
3. Add terminal output log file (`output.txt` for Python labs).
4. Commit and push your changes to GitHub:

```bash
git add .
git commit -m "Add Lab 09 solution and output"
=======
## 📝 Learning & Error Log (`log.txt`) — Python Labs Only (Lab 13 Onwards)

> ⚠️ **Note:** `log.txt` is strictly required for **Python** labs starting from Lab 13. Your **CST** labs do **not** require a `log.txt` (unless your CST teacher asks for one).

For each Python lab (starting Lab 13), create a simple Notepad text file named **`log.txt`** inside that lab's folder (`Python/Lab_XX/log.txt`).

Write casually in plain words just like rough notes—record your honest thoughts, any syntax/logic bugs you encountered, and how you solved them:

### Example `log.txt`:
```text
Lab Reflection:

1. Approach:
Used a while loop to take input numbers until user entered 0, and a for loop to calculate the sum.

2. Errors Faced:
- Error 1: Infinite loop! Program kept running and didn't stop.
  Fix: Realized I forgot to increment the counter `i += 1` inside the while loop.
- Error 2: IndentationError: expected an indented block.
  Fix: Corrected 4-space tab indentation inside the loop body.

3. Output:
Tested with inputs 5, 10, 15, 0. Output printed: "Total Sum = 30".
```

---

## 🔄 Daily Git Commands

Whenever you add or update your code:

```bash
# 1. Stage your files
git add .

# 2. Commit your work
git commit -m "Add Python Lab 13 solution and log"

# 3. Push to your repository
>>>>>>> 0e9c4c11971356ac5907ff2195aa9e279d545a34
git push origin main
```
