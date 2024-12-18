Mama Miktarı Sorgulama
Bu proje, bir video veya webcam kullanarak mama miktarını tespit etmeye yönelik bir uygulama sunmaktadır. Kullanıcılar, videolarındaki renkleri analiz ederek mama miktarının ne kadar olduğunu belirleyebilirler. Proje, renk tespiti ve bilgisayarla görme (computer vision) tekniklerini kullanarak bu işlemi gerçekleştirmektedir.

## Özellikler
- **Video Tabanlı Mama Miktarı Tespiti**: Kullanıcılar, video dosyasını seçerek mama miktarını analiz edebilirler.
- **Webcam ile Mama Miktarı Tespiti**: Anlık olarak webcam görüntüsü üzerinden mama miktarını analiz etme imkanı sağlar.
- **Renk Tespiti**: Mavi, kırmızı ve yeşil renkler arasındaki alanlar analiz edilerek mama oranı belirlenir.
- **Yüzeydeki Renk Bazlı Durum Bilgisi**: Ekranda, mama miktarı hakkında kullanıcıya anlık bilgi verilir.

## Gereksinimler
Projenin çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:
- **OpenCV**: Görüntü işleme ve video işleme için kullanılır.
- **NumPy**: Sayısal işlemler için kullanılır.
- **PIL (Pillow)**: Görüntülerin GUI üzerinde gösterilmesi için kullanılır.
- **Tkinter**: GUI arayüzü oluşturulması için kullanılır.
