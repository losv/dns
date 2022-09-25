import requests

dns='a'
domen = 'nkt.ru'
list_geo = []

def dns_rec (domen, dns):
    URL_AUTH = 'https://dns.google.com/resolve'
    for i in dns:
        params = {'name': domen, 'type': i}
        r = requests.get(URL_AUTH, params=params)
        res = r.json()
        list_dns_a = [res['Answer'][l]['data'] for l in range(len(res['Answer']))]
    return list_dns_a

def geo_ip(ip):
    URL = ''
    KEY = ''

    for i in ip:
        params = {'apiKey': KEY, 'ip': i}
        try:
            r = requests.get(URL, params=params)
            res = r.json()
            list_geo.append([res['country_name'], res['organization'], res['city'], i])
        except:
            print('domen error')
    return list_geo
d = geo_ip(dns_rec(domen, dns))

for i in range(len(d)):
    print('Страна где находится IP {}, город {},  Организация {}, IP {}'.format(d[i][0], d[i][2], d[i][1], d[i][3]))
