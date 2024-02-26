def xml_to_dict():
    try:
        xml_file = open('./directives.xml', 'rt')
        xml_file_contents = xml_file.read()
        xml_file.close()

    except:
        print("Directive file is missing.")

def check_key(xml_file_contents, key_value, range=None):
    startPos = 0
    endPos = len(xml_file_contents) - 1

    if not(range is None):
        try:
            startPos = range[0]
            endPos = range[1]

            if ((-1 == endPos) | ((len(xml_file_contents) - 1) == endPos)):
                xml_file_contents = xml_file_contents[startPos:]
            else:
                xml_file_contents = xml_file_contents[startPos:endPos+1]
                
        except:
            print(f"Invalid XML look-up parameter: range = {range}")
            print("Expected: range = [Start position, End position]\n")
            return 0

    keyPair = []
    keyPair.append('<' + key_value + '>')
    keyPair.append('</' + key_value + '>')

    key_startPos = xml_file_contents.index(keyPair[0]) + len(keyPair[0]) + 1
    key_endPos = xml_file_contents.index(keyPair[1]) - 1

    validityFlag = (key_startPos >= 0) & (key_endPos >= 0)
    validityFlag &= (key_startPos < key_endPos)

    if not(validityFlag)
        return False

    key_value = xml_file_contents[key_startPos : key_endPos]
    return key_value