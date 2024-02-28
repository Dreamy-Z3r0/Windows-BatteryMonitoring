def parse_xml(keyValue, XML_fileContents=None):
    try:
        if (XML_fileContents is None):
            XML_file = open('./directives.xml', 'rt')
            XML_fileContents = XML_file.read()
            XML_file.close()

        try:
            delimiterIndex = keyValue.index('/')
        except:
            delimiterIndex = -1
        finally:
            lookupValue = keyValue[:delimiterIndex]
            if (-1 == delimiterIndex):
                lookupValue = keyValue

            XML_fileContents = check_key(XML_fileContents, lookupValue)
            if (-1 == delimiterIndex):
                return XML_fileContents
            else:
                delimiterIndex += 1
                keyValue = keyValue[delimiterIndex:]
                return parse_xml(keyValue, XML_fileContents)

    except:
        print("Directive file is missing, has format error(s), or does not contain the tag of interest.")

def check_key(XML_fileContents, keyValue):
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
    print(parse_xml('save_location/battery_report_'))
    print(parse_xml('save_location/battery_all_info'))
    print(parse_xml('file_name/battery_report'))
    print(parse_xml('file_name/battery_all_info'))