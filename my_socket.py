import socket

def ip_adreslerini_al(url):
    try:
        ip_adresleri = socket.getaddrinfo(url, None)
        ip_listesi = [addr[4][0] for addr in ip_adresleri]
        return ip_listesi
    except socket.gaierror:
        print(f"{url} adresinin IP adresi alınamadı.")
        return []

def soket_kontrolu_yap(ip_adresi, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip_adresi, port))

        print(f"{ip_adresi}:{port} adresine başarıyla bağlanıldı.")
    except socket.error:
        print(f"{ip_adresi}:{port} adresine bağlantı başarısız.")
    finally:
        sock.close()

url = input("Site URL'sini girin: ")
ip_adresleri = ip_adreslerini_al(url)

if ip_adresleri:
    print(f"{url} adresine ait IP adresleri:")
    for ip_adresi in ip_adresleri:
        print(ip_adresi)

    port = int(input("Port numarasını girin: "))

    for ip_adresi in ip_adresleri:
        soket_kontrolu_yap(ip_adresi, port)
