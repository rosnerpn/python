import speedtest
import requests
import telebot

bot = telebot.TeleBot("SEU_TOKEN")
canalid = 'SEU_ID'

def verificar_velocidade_internet():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  
    upload_speed = st.upload() / 10**6    
    return download_speed, upload_speed

def get_ip():
    
    response = requests.get("https://api.ipify.org")
    return response.text

def send_message(chat_id, message):
    bot.send_message(chat_id, message)


def main():
    download_speed, upload_speed = verificar_velocidade_internet() 
    print(f'Velocidade de Download: {download_speed:.2f} Mbps')  
    print(f'Velocidade de Upload: {upload_speed:.2f} Mbps') 
    message = f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps"
    send_message(canalid,message)  

if __name__ == '__main__':
    main()