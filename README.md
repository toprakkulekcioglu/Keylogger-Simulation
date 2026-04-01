# 🛡️ Endpoint Intelligence & Data Exfiltration Simulation

Bu proje, modern siber güvenlik tehditlerini ve uç nokta izleme mekanizmalarını anlamak amacıyla geliştirilmiş bir **Proof of Concept (PoC)** çalışmasıdır. Temel amacı, bir zararlı yazılımın (malware) kullanıcı etkileşimlerini nasıl takip edebileceğini ve toplanan verileri dış dünyaya nasıl sızdırabileceğini (Data Exfiltration) simüle etmektir.

##  Teknik Özellikler

- **Stealth Execution:** `--noconsole` parametresi ile paketlenerek, hedef sistemde herhangi bir GUI (arayüz) tetiklemeden arka plan servisi (background process) olarak çalışır.
- **Dependency-Free Architecture:** `PyInstaller` kullanılarak kütüphane bağımlılıkları statik olarak paketlenmiş (Static Linking), böylece hedef sistemde Python yorumlayıcısı gereksinimi ortadan kaldırılmıştır.
- **Asynchronous Exfiltration:** `threading` kütüphanesi kullanılarak, veri sızdırma işlemi ana süreçten bağımsız ve asenkron olarak gerçekleştirilir.
- **C2 (Command & Control) Simulation:** Toplanan veriler, HTTP POST metodu ile uzak bir sunucuya JSON formatında iletilmektedir.

## 🛠️ Teknoloji Yığını

- **Dil:** Python 3.13
- **Kritik Kütüphaneler:** - `pynput`: Hooking mekanizması ile I/O olaylarını izleme.
  - `requests`: Veri sızdırma (Exfiltration) kanalı.
  - `threading`: Çoklu iş parçacığı yönetimi.
- **Derleme:** PyInstaller (Standalone Executable)

## 📂 Proje Yapısı
- `monitor_service.py`: Sistemin mantıksal katmanını ve veri toplama algoritmasını içeren kaynak kod.
- `dist/`: Hedef sistemde çalışmaya hazır, paketlenmiş yürütülebilir dosya (Binary).

## ⚠️ Yasal Uyarı (Legal Disclaimer)

Bu yazılım sadece **eğitim ve siber güvenlik araştırmaları** için tasarlanmıştır. İzinsiz sistemlerde kullanılması y
