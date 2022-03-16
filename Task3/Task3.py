import re
from bs4 import BeautifulSoup
from urllib import request

# Python 3.8.10
# David Gomez

# URL
url = "http://www.aemet.es/es/eltiempo/prediccion/municipios/santander-id39075"

# Extract html
html =request.urlopen(url).read()

# Get raw text
raw = BeautifulSoup(html, 'html.parser').get_text()

def main():
    '''Main function executed when running this file.'''
    # Temperature values are after "Temperatura mínima y máxima"
    index = raw.find("Temperatura mínima y máxima")
    # Temperature values are before "Temperatura térmica mínima y máxima"
    index2 = raw.find("Sensación térmica mínima y máxima")

    # Let's work with this section
    text = raw[index:index2]

    # Temperature values are numbers
    matches = re.findall('[0-9]+', text)
    t = []
    for m in matches:
        t.append(int(float(m)))
    
    # Print final result
    print(f'The maximum temperature expected for today is: {t[1]}ºC')

if __name__ == "__main__":
    main()