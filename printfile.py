def printfile(file):
    try:
        contents = file.read()
        print(file)
    finally:
        file.close()
