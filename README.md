![image](https://github.com/user-attachments/assets/084422aa-3ed6-4f8c-8bf4-9c26d961430d)# 🧾 NZ Finance Toolkit

A Python GUI app for **New Zealand personal finance tasks** — built for students, self-employed workers, and anyone who needs simple, local financial tools.

> Created by **Irvin Buquiran** | Built with 🐍 Python + Tkinter

---

## ✨ Features

- ✅ **Income Tax Calculator**  
  Calculates tax using NZ IRD brackets with:
  - KiwiSaver (3%) deduction
  - Student Loan (12% over $22,828)

- ✅ **GST Calculator**  
  Calculates GST and total price for goods/services (15%).

- ✅ **Expense Tracker**  
  Lets you log expenses with categories and export to CSV.

- ✅ **Full GUI interface**  
  Menu navigation + popup summaries (Tkinter).

- ✅ **Splash screen on startup**  
  Looks professional and gives loading feedback.

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/49b9dfad-d90e-44f7-9933-903729859bfd)



---

## 🚀 How to Run

### Option 1: Run via Python

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/nz-finance-toolkit.git
cd nz-finance-toolkit
```

2. Run it:
```bash
python nz_finance_toolkit.py
```

---

### Option 2: Run as Executable (Windows/Mac)

#### 🪟 Windows
```bash
pip install pyinstaller
pyinstaller --onefile --windowed nz_finance_toolkit.py
```

#### 🍎 macOS
```bash
pip install py2app
python setup.py py2app
```

---

## 📂 Files Included

- `nz_finance_toolkit.py` – Main Python application
- `expenses_gui.csv` – Expense log (auto-generated)
- `README.md` – This file
- `tax_summary.csv`, `gst_summary.csv` – Optional CSV outputs

---

## 💼 Built With

- [Python 3.10+](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CSV module](https://docs.python.org/3/library/csv.html)

---

## 🧠 Credits

Made by **Irvin Buquiran**  
MIT Business School, Accounting + Python Portfolio 2025  
Feel free to connect via [LinkedIn](https://www.linkedin.com/) or GitHub.

---

## 🛡 License

MIT License — free to use, share, and remix.
