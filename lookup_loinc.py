import requests
from requests.auth import HTTPBasicAuth
import os
import json
from dotenv import load_dotenv

load_dotenv()

base_url = 'https://fhir.loinc.org/CodeSystem/$lookup?system=http://loinc.org&code='

in_directory = 'files'
out_directory = 'output'

in_filename = 'loincs.txt'
out_filename = 'output.txt'

new_line = '\n'
delim = ','

input_file = os.path.join(in_directory, in_filename)
output_file = os.path.join(out_directory, out_filename)

basic_auth_un = os.environ['UN']
basic_auth_pw = os.environ['PW']

try:
    reader = open(input_file)
except:
    print('cannot open file for reading')
    exit()

try:
    output = open(output_file, 'w')

except:
    print('cannot open file for writing')
    exit()

for line in reader:
    loinc = line.strip(new_line)
    url = base_url + loinc

    response = requests.get(url, auth=HTTPBasicAuth(
        basic_auth_un, basic_auth_pw))

    if response.status_code == 200:
        res = response.json()
        loinc_description = res['parameter'][1]['valueString']
    else:
        loinc_description = 'error - status code: ' + str(response.status_code)
        print(str(response.status_code))

    output_line = loinc + delim + loinc_description + new_line
    output.write(output_line)

reader.close()
output.close()
