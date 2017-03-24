def companies(d, m, y):
    import urllib
    import urllib.request as req
    import re
    import json

    #handle day
    d = str(d + 40)

    #handle month
    if len(str(m)) == 1:
        m = '0' + str(m)
    else:
        m = str(m)
    
    #handle year
    y = str(y)[2:]

    reqstr = d+m+y
    
    api = req.urlopen('http://apis.is/company?socialnumber=%s' % reqstr)
    data = json.loads(api.read().decode('utf-8'))
    result = data['results']

    toReturn = []
    for i in result:
        if i['active'] == 1:
            toReturn.append(i['name'])
    return toReturn

x = companies(20, 12, 2013)
for i in x:
    print(i)
