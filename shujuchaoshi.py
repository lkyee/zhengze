import requests
import re
import time

URL = 'http://192.168.194.122:10141/'
for i in range(102):
    res = requests.get(URL)
    #print(res.content)
    result = re.findall(r"<code>+\d+\D+\d+\D+\d+\D+\d+\D+\d+\D+\d+", res.content)
    str1 = result[0]
    str_result = str1[6:]
    #print(eval(str_result))
    final = eval(str_result)

    #print(type(final))
    time.sleep(0.5)
    data = {'answer': str(final)}
    response = requests.post('http://192.168.194.122:10141/api/answer', data=data)
    print(response.text)
    time.sleep(0.1)
