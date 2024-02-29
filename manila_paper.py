from unidecode import unidecode;
import pandas;
import requests;

req = requests.Session()
dfs = pandas.read_html("https://www.worlddata.info/capital-cities.php");
for df in dfs:
    cities = df['Capital City'];
    for city in cities:        
        city_name = city.replace(" ", "_");
        city_name = unidecode(city_name);
        r = req.get("https://en.wiktionary.org/w/index.php?title="+city_name+"_paper");
        if r.status_code==200:
            print(city);
        else:
            r = req.get("https://en.wiktionary.org/w/index.php?title="+city_name.lower()+"_paper");
            if r.status_code==200:
                print(city);
            
