############     1
import requests
res = requests.post("http://127.0.0.1:8000/api/robots",json={"model":"R4","version":"D3","created":"2022-12-31 23:59:59"})
print(res.json())
##############
