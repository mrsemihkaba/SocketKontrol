# IP Adresi ve Soket Kontrolü

Açıklama:
Bu proje, kullanıcının girdiği bir URL'ye ait IP adreslerini otomatik olarak bulur ve belirtilen port numarası üzerinden soket kontrolü yapar. Projede kullanılan `socket` modülü, Python'da ağ programlaması için kullanılan bir modüldür.

Proje Adımları:
1. Kullanıcıdan bir URL alınır.
2. `socket.getaddrinfo()` fonksiyonu kullanılarak URL'ye ait IP adresleri alınır.
3. IP adresleri ekrana yazdırılır.
4. Kullanıcıdan bir port numarası alınır.
5. Her bir IP adresi için soket kontrolü yapılır:
   a. `socket.socket()` fonksiyonu ile bir soket oluşturulur.
   b. Soketin zaman aşımı süresi ayarlanır.
   c. IP adresi ve port numarası kullanılarak sokete bağlanılır.
   d. Bağlantı başarılıysa, "IP adresi:port" şeklinde bir mesaj yazdırılır.
   e. Bağlantı başarısızsa, "IP adresi:port" şeklinde bir hata mesajı yazdırılır.
   f. Soket kapatılır.

Bu proje, kullanıcının girdiği URL'ye ait IP adreslerini bulmayı ve belirtilen port üzerinde soket kontrolü yapmayı sağlar. Böylece ağ bağlantısıyla ilgili sorunları tespit etmek ve kontrol etmek için kullanılabilir.

