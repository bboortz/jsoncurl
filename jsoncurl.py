#!/usr/bin/env python3


import argparse
import json

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


progname = "jsoncurl"



class jsoncurl(object):

    def __init__(self):
        pass

    def get_jsonparsed_data(self, url):
        """Receive the content of ``url``, parse it as JSON and return the
           object.
        """

        response = urlopen(url)
        data = str(response.read())
        return json.loads(data)

class jsonprint(object):

    def __init__(self):
        pass

    def prints(self, json, element=None):
        if element == None:
            print(json)
        else:
            try:
                print(json[element])
            except KeyError:
                print("element <%s> not found in json" % element)




parser = argparse.ArgumentParser(prog=progname, description='Curl like tool for json data.')
parser.add_argument('-e', '--extract-element', dest='extract_element', help='extract an element')
parser.add_argument('URL', help='the url to request')
args = vars( parser.parse_args() )


jc = jsoncurl()
jp = jsonprint()


json_data = jc.get_jsonparsed_data( args['URL'] )
if args['extract_element']:
    jp.prints(json_data, args['extract_element'] )
else:
    jp.prints(json_data)

