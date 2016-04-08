import xml.etree.ElementTree as ET
import requests


def check_open():
    print "\n-- FALL 2016 Course Checker by Wayne --\n"

    # course = {'department': 'ECE', 'number': 408, 'crn': 58790}
    # url = 'http://courses.illinois.edu/cisapp/explorer/schedule/2016/fall/{}/{}/{}.xml'.format(course['department'], course['number'], course['crn'])
    # r = requests.get(url)
    # xml = r.text

    # For testing with localXML #
    with open('test.xml', 'r') as xml:
        xml=xml.read()

    try:
        root = ET.fromstring(xml)
    except:
        print "Class doesn't exist :("
        return
    avail = root.find('enrollmentStatus').text
    if avail == "CrossListOpen" or avail == "Open":
        return 1
    elif avail == "CrossListOpen (Restricted)":
        return 1
    else:
        return 0

if __name__ == '__main__':
    if check_open():
        print "OPEN"
    else:
        print "CLOSED"
    raw_input("\nPress any key to exit...")
