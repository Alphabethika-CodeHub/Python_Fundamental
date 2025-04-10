print("This is The Convention of Python")

print("""
Urutan Import Library/Package Pada Python:
# Standard Library
import os
import sys

# Third-Party Packages
import requests

# Local Application
from mymodule import app
""")


print("""
Konvensi Utama Python (PEP 8) :
Jenis	                Contoh	            Gaya
Variable	            total_harga	        snake_case
Function	            get_data()	        snake_case
Class	                UserProfile	        PascalCase
Constant	            MAX_RETRIES = 5	    UPPER_CASE
Private (konvensi)	    _hidden_var	        Underscore
""")

# 4 Spaces For Indentation
# 2 Blank Lines to Separate Functions
def salam():
    nama = "JP. Morgan"
    print(f"Halo!, {nama}")


def greetings():
    name = "John"
    print(f"Hola!, {name}")


print(salam(), greetings())

# Always Use 'is' or 'is not' to Compare 'None'
# if results is None:
#     return False




