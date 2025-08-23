import tkinter as tk
from tkinter import messagebox
from GPA_Calc_class import course, calc

grades = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

class GPACALC:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")

        self.calculator = calc(grades) 

        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20, pady=20)

        self.rows = []  # Use 'rows' everywhere for consistency

        # Header labels
        header = tk.Frame(self.frame)
        header.pack()
        tk.Label(header, text='Grade', width=10).pack(side=tk.LEFT, padx=2)
        tk.Label(header, text='Credits', width=10).pack(side=tk.LEFT, padx=2)
        tk.Label(header, text="").pack(side=tk.LEFT, padx=2)  # Spacer

        self.add_row()  # Start with one row

        # Bottom frame for action buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 20))

        # "Add Class" button
        self.add_button = tk.Button(self.button_frame, text='Add Class', command=self.add_row)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=10)

        # "Submit All" button
        self.submit_button = tk.Button(self.button_frame, text='Submit All', command=self.submit)
        self.submit_button.pack(side=tk.LEFT, padx=5, pady=10)

    def add_row(self):
        row_frame = tk.Frame(self.frame)
        row_frame.pack(pady=2)

        grade_entry = tk.Entry(row_frame, width=10)
        grade_entry.pack(side=tk.LEFT, padx=2)
        credit_entry = tk.Entry(row_frame, width=10)
        credit_entry.pack(side=tk.LEFT, padx=2)

        delete_btn = tk.Button(row_frame, text="Delete", command=lambda: self.delete_row(row_frame))
        delete_btn.pack(side=tk.LEFT, padx=2)

        self.rows.append((grade_entry, credit_entry, row_frame))

    def delete_row(self, row_frame):
        for idx, (grade_entry, credit_entry, rf) in enumerate(self.rows):
            if rf == row_frame:
                rf.destroy()
                self.rows.pop(idx)
                break

    def submit(self):
        self.calculator.courses.clear()
        errors = []

        for idx, (grade_entry, credit_entry, rf) in enumerate(self.rows, 1):
            grade = grade_entry.get().strip().upper()
            credit_str = credit_entry.get().strip()

            if grade not in grades:
                errors.append(f"Class {idx}: Invalid grade '{grade}'.")
                continue
            try:
                credits = float(credit_str)
                if credits <= 0:
                    errors.append(f"Class {idx}: Credits must be positive.")
                    continue
            except ValueError:
                errors.append(f"Class {idx}: Credits '{credit_str}' are not a valid number.")
                continue

            try:
                self.calculator.add_course(grade, credits)
            except ValueError as e:
                errors.append(str(e))

        if errors:
            messagebox.showerror("Input Error", "\n".join(errors))
            return

        gpa = self.calculator.calculator_gpa()
        letter = self.calculator.gpa_to_letter(gpa) if gpa > 0 else 'N/A'

        messagebox.showinfo("GPA Result", f"Your GPA is: {gpa:.2f} ({letter})" if gpa > 0 else "No valid classes entered.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPACALC(root)
    root.mainloop()