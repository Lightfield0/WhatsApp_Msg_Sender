# WhatsApp Sender

WhatsApp Sender, bir GUI ile toplu WhatsApp mesajları göndermenizi sağlayan bir Python uygulamasıdır. Kullanıcılar Excel dosyasında bulunan alıcıların numaralarına, belirli bir metni ve isteğe bağlı bir resmi gönderebilir.

## Özellikler

- Bir Excel dosyasından birden çok alıcının telefon numarasını okur.
- Bir metni ve isteğe bağlı bir resmi toplu olarak gönderir.
- GUI, Tkinter ve ttkthemes kullanılarak oluşturulmuştur.
- İletişim kurmak için pywhatkit kütüphanesi kullanılır.

## Kullanım

1. "Select an Excel file" düğmesine tıklayarak, telefon numaralarını içeren bir Excel dosyası seçin.
2. "Message" alanına gönderilecek metni yazın.
3. İsteğe bağlı olarak, "Select an image" düğmesine tıklayarak gönderilecek bir resim seçin.
4. "Send WhatsApp" düğmesine tıklayarak toplu mesajı gönderin.

## Dikkat Edilmesi Gerekenler

- Telefon numaralarının Excel dosyasında 'Telefon' sütununda olması gerekmektedir.
- Toplu mesajın gönderilmesi için internet bağlantısı gereklidir.
- WhatsApp Web'in otomatik olarak açılması ve QR kodunun taranması gereklidir.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakın.
