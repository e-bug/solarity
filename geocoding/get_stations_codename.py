import pickle


def getParsedStation(string):
    code_name = string.split('gre000z0')[0]
    code = code_name.split()[0]
    name = code_name.split()[1]

    return code, name


stationsFile = 'stations_minimum.txt'


stations_codename_dict = {}
with open(stationsFile) as fp:
    for line in fp:
        code, name = getParsedStation(line)
        stations_codename_dict[code] = name

pickle.dump(stations_codename_dict, open('stations_codename.p', 'wb'))
