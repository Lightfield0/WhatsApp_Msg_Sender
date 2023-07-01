import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime
import pandas as pd
import pywhatkit as kit
from ttkthemes import ThemedStyle

image_path = None

def format_phone_number(nums):
    formatted_nums = []
    nums = str(nums).split(",")  
    for num in nums:
        num = num.strip()  
        if num.startswith("0"):  
            num = "+90" + num[1:]
        # Yeni satır: Parantez ve boşlukları kaldır
        num = num.replace(" ", "").replace("(", "").replace(")", "")
        formatted_nums.append(num)
    return formatted_nums

def send_whatsapp():
    # Mesajı al
    message = message_entry.get()

    # Excel dosyasını oku ve 'Telefon' sütunundan numaraları al
    df = pd.read_excel(file_path)
    ditce = {
    "Telefon":["05058836845","05057474088"]
    }
    df = pd.DataFrame(ditce)
    receivers = []
    for i in df['Telefon'].apply(format_phone_number):
        for a in i:
            receivers.append(a)

    # Şimdiki zamanı al
    now = datetime.now()

    # Şimdiki saati ve dakikayı al
    time_hour = now.hour
    time_minute = now.minute + 2  # Hemen sonraki dakika için ayarla

    for receiver in receivers:

        if message and image_path:  # Mesaj ve resim varsa
            kit.sendwhats_image(receiver=str(receiver).strip(), img_path=image_path, caption=message, wait_time=20)
        elif message:  # Sadece mesaj varsa
            # kit.sendwhatmsg(str(receiver).strip(), message, time_hour, time_minute)
            kit.sendwhatmsg_instantly(phone_no=str(receiver).strip(), message=message, wait_time=10)

        else:
            print(f"No message to send for {str(receiver).strip()}")
        time_minute += 1  # bir sonraki mesajı bir dakika sonra gönderir
        if time_minute > 59:  # dakika 60'a ulaşırsa, saat değerini bir artırır ve dakikayı sıfırlar
            time_minute = 0
            time_hour += 1

def select_excel():
    global file_path
    file_path = filedialog.askopenfilename()
    excel_label['text'] = f"Selected file: {file_path}"

def select_image():
    global image_path
    image_path = filedialog.askopenfilename()
    img_label['text'] = f"Selected image: {image_path}"

# Ana pencereyi oluştur
window = tk.Tk()
window.title("WhatsApp Sender")

# Temayı belirle
style = ThemedStyle(window)
style.set_theme("plastik")

# Entry ve Label widgetlarını oluştur
excel_button = ttk.Button(window, text="Select an Excel file", command=select_excel)
excel_button.pack(pady=10)

excel_label = ttk.Label(window, text="")
excel_label.pack()

message_label = ttk.Label(window, text="Message:")
message_label.pack(pady=10)

message_entry = ttk.Entry(window)
message_entry.pack()

img_button = ttk.Button(window, text="Select an image", command=select_image)
img_button.pack(pady=10)

img_label = ttk.Label(window, text="")
img_label.pack()

# Send butonunu oluştur
send_button = ttk.Button(window, text="Send WhatsApp", command=send_whatsapp)
send_button.pack(pady=10)

# GUI'nin çalışması için mainloop'u çağır
window.mainloop()
