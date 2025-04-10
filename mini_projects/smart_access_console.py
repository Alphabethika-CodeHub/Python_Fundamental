# Level 1: Input password (while loop)
correct_password = "python123"

print("🔒 Welcome to Smart Access Console")
attempt = ""

while attempt != correct_password:
    attempt = input("🧪 Enter your password: ")
print("✅ Password accepted!\n")

# Level 2: Validasi umur (if-else)
age = int(input("🎂 Enter your age: "))

if age < 17:
    print("🚫 You must be 17+ to continue. Exiting...")
    exit()
else:
    print("🔓 Age verified. Access granted.\n")

# Level 3: Pilih role (match-case)
role = input("🎭 Choose your role (admin/editor/viewer): ").lower()

def get_role_permissions(role):
    match role:
        case "admin":
            return "📂 Full access to the system."
        case "editor":
            return "📝 Can edit contents."
        case "viewer":
            return "👁️ View-only mode."
        case _:
            return "❌ Role not recognized."

print(get_role_permissions(role), "\n")

# Level 4: Data Filtering (for loop + continue/break)
print("📄 Checking recent activities (skip 'internal', stop at 'shutdown'):")
logs = ["login", "viewed dashboard", "internal", "edit profile", "shutdown", "logout"]

for log in logs:
    if log == "internal":
        continue
    if log == "shutdown":
        print("⚠️ System shutdown detected. Stopping log check...")
        break
    print(f"🕒 Activity: {log}")
print()

# Level 5: Data Processing (list comprehension)
scores = [65, 80, 45, 90, 50, 72, 30]
passed = [score for score in scores if score >= 60]
