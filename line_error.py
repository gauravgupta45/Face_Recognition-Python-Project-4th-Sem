with open("names_list.txt", 'r+') as fd:
    lines = fd.readlines()
    fd.seek(0)
    fd.writelines(line for line in lines if line.strip())
    fd.truncate()
