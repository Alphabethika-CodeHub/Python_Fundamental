with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()
    close_this_file.close()

print(setup)
