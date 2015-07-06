from math import radians, cos, sin, asin, sqrt
from csv import DictReader
from dominate import document
from dominate.tags import *
from collections import defaultdict

ISRAEL_LAT, ISRAEL_LON = 31.5, 34.75

lon1 = ISRAEL_LON
lat1 = ISRAEL_LAT

countries=defaultdict(list)


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km










def sheet_of_country(short_name,name,capital,populatin,land,continent):

            with open('{}.html'.format(short_name), 'w') as short_name:
                short_name.write('''
<html>
<head>
    <title>{}</title>
</head>
<body>
<a href="continent_{}.html">continent</a>
<h1>{}</h1>
<d1>

        <dt>Capital</dt>
        <dd>{}</dd>

        <dt>Population</dt>
        <dd>{:,d}</dd>

        <dt>Land Area</dt>
        <dd>{:,d} km<sup>2</sup></dd>

        <dt>Continent</dt>
        <dd>{}</dd>

<a href="index.html">bake to index</a>'
<a href="index1.html">bake to most population</a>'
</d1>
</body>
</html>'''.format(name,continent, name, capital, int(populatin),int(land)if land else 0, continent))



def sheet_of_continents(countries):
   for k,v in countries.items():
        doc=document(title="continent")
        with doc.head:
            with doc.body:
                h1(k)
                for x in v:
                    a(x['name'],href='{}.html'.format(x['short_name']))
                    br()
                a('bake to index',href="index.html")

        with open('continent_{}.html'.format(k),'w') as f:
            f.write(doc.render())





countries=defaultdict(list)

def sort_list(str):
    with open('countries.csv') as f:
        country = DictReader(f)
        return sorted(country,key=lambda x:int(x[str]),reverse=True)

def sheet_of_most_population():
    sortList=sort_list('population')
    doc=document(title="most population")
    with doc.head:
        with doc.body:
            h1("most poulation")
            for k in sortList:
                a(k['name'],href='{}.html'.format(k['short_name']))
                br()

    with open('index1.html','w') as f:
        f.write(doc.render())




with open('countries.csv') as f:
    reader = DictReader(f)


    with open('index.html', 'w') as index:
        index.write("<a href=index1.html>go to most population</a>")
        index.write('<ul>' + "\n")



        for d in reader:

            name = d['name']
            short_name = d['short_name']
            capital = d['capital']
            populatin = d['population']
            continent = d['continent']
            land = d['land']
            lon2 = float(d['lon'])
            lat2 = float(d['lat'])
            distance = haversine(lon1, lat1, lon2, lat2)


            sheet_of_country(short_name,name,capital,populatin,land,continent)

            countries[continent].append(d)



            index.write('\t<li><a href="{}.html">{}</a>:{:,f} km</li>'.format(short_name,name, distance))



        index.write('</ul>')

sheet_of_continents(countries)

sheet_of_most_population()




