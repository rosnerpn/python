from speedtest import Speedtest
from requests import get
ip_externo = get('https://api.ipify.org').text
st = Speedtest()
mb = 10**-6


print(f"IP Externo: {ip_externo}")
print('Testando Velocidade da Internet...')
download = st.download()*mb
upload = st.upload()*mb
print('Velocidade de Download: {:.2f} MB'.format(download))
print('Velocidade de Upload: {:.2f} MB'.format(upload))
