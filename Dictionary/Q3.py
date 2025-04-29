#7.3
dept_salaries = {
    101: [50000, 60000, 55000],
    102: [45000, 47000],
    103: [70000, 72000, 68000]
}


for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: \n Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")
