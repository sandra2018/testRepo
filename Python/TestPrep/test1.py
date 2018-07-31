destinationAbsPath = os.path.abspath(destinationPath)
fullPath = os.path.join(destinationAbsPath, filename)
if os.path.exists(fullPath):
    #os.chmod(fullPath, 0777)
    with open(os.path.join(fullPath, 'r')) as testFile:
        testLine = testFile.read().strip()
        # split into fields
        line = testLine.split()
        ipAddress = line[0]
        status = line[5]
        match = re.search("[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}",ipAddress)
        if status == 200:
            if match:
                if match in successAttempts:
                    count = successAttempts[match]
                    successAttempts[match] = count++
                else:
                    successAttempts.update(match, 1)

    testFile.close()
    for keys, values in successAttempts.items():
        print "{}\t{}".format(keys, values)

else:
    print('file not found')