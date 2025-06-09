# Add imports for Tkinter GUI at the top
import tkinter as tk
from tkinter import messagebox
import time
import threading
# NZ Tax & GST Calculator


def calculate_income_tax(income):
    tax = 0
    brackets = [
        (14000, 0.105),  # 10.5% for income up to $14,000
        (48000, 0.175),  # 17.5% for income from $14,001 to $48,000
        (70000, 0.3),    # 30% for income from $48,001 to $70,000
        (180000, 0.33),  # 33% for income from $70,001 to $180,000
        (float('inf'), 0.39)  # 39% for income over $180,000
    ]

    thresholds = [0, 14000, 48000, 70000, 180000]

    for i in range(len(brackets)):
        lower = thresholds[i]
        upper = brackets[i][0]
        rate = brackets[i][1]

        if income > lower:
            taxable = min(income, upper) - lower
            tax += taxable * rate
    return round(tax, 2)

def calculate_gst(price, gst_rate=0.15):
    gst_amount = price * gst_rate
    total_price = price + gst_amount
    return round(gst_amount, 2), round(total_price, 2)

def expense_tracker():
    print("\n=== Expense Tracker ===")
    expenses = []
    while True:
        description = input("Enter expense description (or 'done' to finish): ")
        if description.lower() == 'done':
            break
        amount = float(input("Enter amount spent: $"))
        category = input("Enter category (e.g. food, transport, etc.): ")
        expenses.append((description, amount, category))

    # Write to CSV
    import csv
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Amount", "Category"])
        writer.writerows(expenses)

    # Summarize per category
    summary = {}
    for _, amount, category in expenses:
        summary[category] = summary.get(category, 0) + amount

    print("\n>> Expense Summary:")
    for cat, total in summary.items():
        print(f"{cat.capitalize()}: ${total:.2f}")

    print("\nExpenses saved to expenses.csv")

def main():
    pass  # CLI disabled, using GUI only

def show_splash():
    splash = tk.Tk()
    splash.title("Welcome")
    splash.geometry("300x150")
    label = tk.Label(splash, text="Launching Finance Toolkit...", font=("Arial", 14))
    label.pack(expand=True)
    splash.after(2000, splash.destroy)
    splash.mainloop()

# GUI for NZ Tax Calculator
def launch_gui():
    def show_tax_calculator():
        def calculate_tax():
            try:
                income = float(entry_income.get())
                tax = calculate_income_tax(income)
                kiwisaver = round(income * 0.03, 2)
                sl_threshold = 22828
                student_loan = round(max(0, income - sl_threshold) * 0.12, 2)
                total_deductions = tax + kiwisaver + student_loan
                net_income = round(income - total_deductions, 2)

                result_text = (
                    f"Total Income Tax: ${tax:,.2f}\n"
                    f"KiwiSaver (3%): ${kiwisaver:,.2f}\n"
                    f"Student Loan: ${student_loan:,.2f}\n"
                    f"Total Deductions: ${total_deductions:,.2f}\n"
                    f"Net Income: ${net_income:,.2f}"
                )
                messagebox.showinfo("Tax Summary", result_text)
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

        window = tk.Toplevel(root)
        window.title("NZ Tax Calculator")

        tk.Label(window, text="Enter Annual Income (NZD):").pack(pady=5)
        entry_income = tk.Entry(window)
        entry_income.pack(pady=5)
        tk.Button(window, text="Calculate Tax", command=calculate_tax).pack(pady=10)

    def show_gst_calculator():
        def calculate_gst_gui():
            try:
                price = float(entry_price.get())
                gst_amount, total = calculate_gst(price)
                result_text = (
                    f"GST Amount: ${gst_amount:,.2f}\n"
                    f"Total Price (incl. GST): ${total:,.2f}"
                )
                messagebox.showinfo("GST Summary", result_text)
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

        window = tk.Toplevel(root)
        window.title("GST Calculator")

        tk.Label(window, text="Enter Price (excl. GST):").pack(pady=5)
        entry_price = tk.Entry(window)
        entry_price.pack(pady=5)
        tk.Button(window, text="Calculate GST", command=calculate_gst_gui).pack(pady=10)

    def show_expense_tracker():
        def add_expense():
            desc = entry_desc.get()
            try:
                amt = float(entry_amt.get())
                cat = entry_cat.get()
                expenses.append((desc, amt, cat))
                entry_desc.delete(0, tk.END)
                entry_amt.delete(0, tk.END)
                entry_cat.delete(0, tk.END)
                messagebox.showinfo("Added", f"Added {desc} - ${amt:.2f} ({cat})")
            except ValueError:
                messagebox.showerror("Invalid input", "Enter a valid amount.")

        def export_expenses():
            import csv
            with open("expenses_gui.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Description", "Amount", "Category"])
                writer.writerows(expenses)
            messagebox.showinfo("Saved", "Expenses saved to expenses_gui.csv")

        expenses = []
        window = tk.Toplevel(root)
        window.title("Expense Tracker")

        tk.Label(window, text="Description").pack()
        entry_desc = tk.Entry(window)
        entry_desc.pack()

        tk.Label(window, text="Amount").pack()
        entry_amt = tk.Entry(window)
        entry_amt.pack()

        tk.Label(window, text="Category").pack()
        entry_cat = tk.Entry(window)
        entry_cat.pack()

        tk.Button(window, text="Add Expense", command=add_expense).pack(pady=5)
        tk.Button(window, text="Export to CSV", command=export_expenses).pack(pady=5)

    root = tk.Tk()
    root.title("Finance Toolkit")

    tk.Label(root, text="Select an option").pack(pady=10)
    tk.Button(root, text="Tax Calculator", command=show_tax_calculator).pack(pady=5)
    tk.Button(root, text="GST Calculator", command=show_gst_calculator).pack(pady=5)
    tk.Button(root, text="Expense Tracker", command=show_expense_tracker).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()
if __name__ == "__main__":
    splash_thread = threading.Thread(target=show_splash)
    splash_thread.start()
    splash_thread.join()
    launch_gui()
