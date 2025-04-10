print("""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:
Equals                      : a == b
Not Equals                  : a != b
Less than                   : a < b
Less than or equal to       : a <= b
Greater than                : a > b
Greater than or equal to    : a >= b

Reference: https://www.w3schools.com/python/python_conditions.asp
""")


# If-Else Statement
age = 18
if age >= 17:
    print("Kamu sudah cukup umur untuk membuat KTP.")
else:
    print("Kamu belum cukup umur.")


# For Loop + Continue/Break
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 4:
        continue  # Lewati angka 4
    if num == 6:
        break  # Berhenti saat angka 6
    print(num)


# While Loop dengan Input Validasi
password = ""

while password != "python123":
    password = input("Masukkan password: ")

print("Password benar! Akses diberikan.")


# List Comprehension dengan Kondisi
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64]


# Match-Case (Python 3.10+)
def get_role(level):
    match level:
        case "admin":
            return "Full access granted."
        case "editor":
            return "Edit access granted."
        case "viewer":
            return "View-only access."
        case _:
            return "Unknown role."

print(get_role("editor"))

# If Statements as Guards
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

# Data Processing Using List Comprehension
scores = [65, 80, 45, 90, 50, 72, 30]
passed = [score for score in scores if score >= 60]

print("📊 Filtered passed scores:", passed)




