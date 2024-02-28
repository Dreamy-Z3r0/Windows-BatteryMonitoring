def parse_xml(keyValue):
    try:
        XML_file = open('./directives.xml', 'rt')
        XML_fileContents = XML_file.read()
        XML_file.close()

        delimiterIndex = keyValue.index('/')
        while (delimiterIndex >= 0):
            lookupValue = keyValue[:delimiterIndex]
            keyValue = keyValue[(delimiterIndex+1):]
            XML_fileContents = check_key(XML_fileContents, lookupValue)

        return XML_fileContents

    except:
        print("Directive file is missing.")

def check_key(XML_fileContents, keyValue, range=None):
    startPos = 0
    endPos = len(XML_fileContents) - 1

    if not(range is None):
        try:
            startPos = range[0]
            endPos = range[1]

            if ((-1 == endPos) | ((len(XML_fileContents) - 1) == endPos)):
                XML_fileContents = XML_fileContents[startPos:]
            else:
                XML_fileContents = XML_fileContents[startPos:endPos+1]
                
        except:
            print(f"Invalid XML look-up parameter: range = {range}")
            print("Expected: range = [Start position, End position]\n")
            return 0

    keyPair = []
    keyPair.append('<' + keyValue + '>')
    keyPair.append('</' + keyValue + '>')

    key_startPos = XML_fileContents.index(keyPair[0]) + len(keyPair[0]) + 1
    key_endPos = XML_fileContents.index(keyPair[1]) - 1

    validityFlag = (key_startPos >= 0) & (key_endPos >= 0)
    validityFlag &= (key_startPos < key_endPos)

    if not(validityFlag):
        return False

    keyValue = XML_fileContents[key_startPos : key_endPos]
    return keyValue

if __name__ == '__main__':
