# math modülü, matematiksel işlemler yapmak için kullanılan bir Python kütüphanesidir.
import math
# tools klasörü içindeki benchmark fonksiyonunu projeye dahil edilir.
# Bu fonksiyon sayesinde kodun çalışma süresi, bellek kullanımı ve CPU kullanımı ölçülebilir.
from tools.benchmark import benchmark


# distance adında bir fonksiyon tanımlanır.
# fonksiyonun amacı:
# İki nokta arasındaki Öklid mesafesini hesaplamaktır.
# Öklid mesafesi, iki nokta arasındaki düz çizgi mesafesidir ve şu formülle hesaplanır:
# √((x2-x1)^2 + (y2-y1)^2)
def distance(p1, p2):
    """
    İki nokta arasındaki Öklid mesafesi:
    √((x2-x1)^2 + (y2-y1)^2)
    """
    # math.sqrt fonksiyonu, verilen sayının karekökünü döndürür.

    # (p1[0] - p2[0]) ** 2 ifadesi, p1 ve p2 noktalarının x koordinatları arasındaki farkın karesini hesaplar.
    # (p1[1] - p2[1]) ** 2 ifadesi, p1 ve p2 noktalarının y koordinatları arasındaki farkın karesini hesaplar.
    # Bu iki kare toplamının karekökü, p1 ve p2 noktaları arasındaki Öklid mesafesini verir.    

    # Örneğin, p1 = (0, 0) ve p2 = (3, 4) için distance(p1, p2) fonksiyonu şu şekilde hesaplanır:
    # (p1[0] - p2[0]) ** 2 = (0 - 3) ** 2 = (-3) ** 2 = 9
    # (p1[1] - p2[1]) ** 2 = (0 - 4) ** 2 = (-4) ** 2 = 16
    # Toplam = 9 + 16 = 25
    # Karekök = √25 = 5.0
    # Bu nedenle, distance((0, 0), (3, 4)) fonksiyonu 5.0 döndürecektir, 
    # çünkü (0, 0) ve (3, 4) noktaları arasındaki Öklid mesafesi 5.0'dır.
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# brute_force adında bir fonksiyon tanımlanır.
# fonksiyonun amacı:
# verilen noktalar arasındaki en küçük Öklid mesafesini bulmaktır.
# Nokta sayısı az olduğunda (<=3), tüm çiftleri deneyerek en küçük mesafeyi bulur.
# Örneğin, points = [(0, 0), (3, 4), (7, 7)] için brute_force fonksiyonu 5.0 döndürecektir.
# Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve diğer nokta çiftleri arasında daha küçük bir mesafe yoktur.
def brute_force(points):
    """
    Küçük veri setlerinde (<=3 nokta),
    tüm nokta çiftlerini karşılaştırarak minimum mesafeyi döndürür.
    """
    # min_dist değişkeni, şu ana kadar bulunan en küçük mesafeyi saklar.
    # Başlangıçta sonsuz olarak atanır, böylece herhangi bir gerçek mesafe bu değerden daha küçük olacaktır.
    # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için min_dist başlangıçta float("inf") olarak atanır.
    # Daha sonra (0, 0) ve (3, 4) noktaları arasındaki mesafe hesaplandığında min_dist 5.0 olarak güncellenir.
    min_dist = float("inf")

    # points listesindeki her bir nokta çifti için döngü başlatılır.
    # Bu döngü, tüm nokta çiftlerini deneyerek en küçük mesafeyi bulur.
    # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için şu nokta çiftleri incelenir:
    # (0, 0) ve (3, 4) → mesafe = 5.0
    # (0, 0) ve (7, 7) → mesafe = √((7-0)^2 + (7-0)^2) = √98 ≈ 9.899
    # (3, 4) ve (7, 7) → mesafe = √((7-3)^2 + (7-4)^2) = √25 = 5.0
    # Bu çiftler arasında en küçük mesafe 5.0'dır, bu yüzden brute_force fonksiyonu 5.0 döndürecektir.
    for i in range(len(points)):
        # points listesindeki her bir nokta için, o noktadan sonraki tüm noktalarla çiftler oluşturulur.
        # Bu şekilde her nokta çifti sadece bir kez incelenir.
        # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için i=0 olduğunda j=1 ve j=2 için çiftler incelenir.
        # i=1 olduğunda j=2 için çift incelenir. i=2 olduğunda j için herhangi bir değer kalmaz, bu yüzden döngü sona erer.
        # Bu yöntem, her nokta çifti için mesafe hesaplaması yaparak en küçük mesafeyi bulur.
        for j in range(i + 1, len(points)):
            # distance fonksiyonu, points[i] ve points[j] noktaları arasındaki Öklid mesafesini hesaplar.
            # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için i=0 ve j=1 olduğunda distance(points[0], points[1]) = distance((0, 0), (3, 4)) = 5.0 olarak hesaplanır.
            # Bu mesafe, min_dist ile karşılaştırılır ve min_dist güncellenir.
            # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için i=0 ve j=1 olduğunda min_dist başlangıçta float("inf") olduğu için min_dist 5.0 olarak güncellenir.
            # i=0 ve j=2 olduğunda distance(points[0], points[2]) = distance((0, 0), (7, 7)) ≈ 9.899 olarak hesaplanır, ancak min_dist 5.0 olduğu için min_dist güncellenmez.
            # i=1 ve j=2 olduğunda distance(points[1], points[2]) = distance((3, 4), (7, 7)) = 5.0 olarak hesaplanır, ancak min_dist zaten 5.0 olduğu için min_dist güncellenmez.
            # Sonuç olarak, brute_force fonksiyonu 5.0 döndürecektir.
            dist = distance(points[i], points[j])
            min_dist = min(min_dist, dist)

    # brute_force fonksiyonu, tüm nokta çiftlerini deneyerek bulunan en küçük mesafeyi döndürür.
    # Örneğin, points = [(0, 0), (3, 4), (7, 7)] için brute_force fonksiyonu 5.0 döndürecektir.
    return min_dist


# strip_closest adında bir fonksiyon tanımlanır.
# Bu fonksiyonun amacı:
# strip_closest fonksiyonu, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol eder ve eğer varsa bu mesafeyi döndürür. 
# Eğer strip içinde d'den küçük bir mesafe bulunmazsa, fonksiyon d'yi döndürür.
# strip, orta çizgiye yakın noktaları içerir ve d, şu ana kadar bulunan minimum mesafeyi temsil eder.
# Örneğin, strip = [(1, 1), (2, 2), (3, 3)] ve d = 1.5 için strip_closest fonksiyonu 1.4142135623730951 döndürecektir.
# Çünkü (1, 1) ve (2, 2) noktaları arasındaki mesafe √((2-1)^2 + (2-1)^2) = √2 ≈ 1.4142135623730951'dir ve bu mesafe d'den küçüktür. 
# Diğer nokta çiftleri arasındaki mesafe ise d'den büyük olduğu için dikkate alınmaz.
# Örneğin, strip = [(1, 1), (2, 2), (3, 3)] ve d = 1.0 için strip_closest fonksiyonu 1.0 döndürecektir.
def strip_closest(strip, d):
    """
    strip: orta çizgiye yakın noktalar
    d: şu ana kadar bulunan minimum mesafe

    Amaç: strip içinde d'den küçük mesafe var mı bakmak
    """
    # min_dist değişkeni, şu ana kadar bulunan en küçük mesafeyi saklar.
    # Başlangıçta d olarak atanır, çünkü strip içinde d'den küçük bir mesafe bulunmazsa d döndürülecektir.
    # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] ve d = 1.5 için min_dist başlangıçta 1.5 olarak atanır.
    min_dist = d

    # strip zaten y'ye göre sıralı geliyor
    # strip listesindeki her bir nokta için döngü başlatılır.
    # Bu döngü, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol eder.
    # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] için şu nokta çiftleri incelenir:
    # (1, 1) ve (2, 2) → mesafe = √((2-1)^2 + (2-1)^2) = √2 ≈ 1.4142135623730951
    # (1, 1) ve (3, 3) → mesafe = √((3-1)^2 + (3-1)^2) = √8 ≈ 2.8284271247461903
    # (2, 2) ve (3, 3) → mesafe = √((3-2)^2 + (3-2)^2) = √2 ≈ 1.4142135623730951
    # Bu çiftler arasında d'den küçük mesafe 1.4142135623730951'dir, bu nedenle strip_closest fonksiyonu 1.4142135623730951 döndürecektir.
    for i in range(len(strip)):
        # strip listesindeki her bir nokta için, o noktadan sonraki birkaç nokta ile çiftler oluşturulur.
        # Bu şekilde her nokta çifti sadece bir kez incelenir ve sadece yakın olan birkaç noktaya bakılır.
        # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] için i=0 olduğunda j=1 ve j=2 için çiftler incelenir.
        # i=1 olduğunda j=2 için çift incelenir. i=2 olduğunda j için herhangi bir değer kalmaz, bu yüzden döngü sona erer.
        # Bu yöntem, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol ederken gereksiz mesafe hesaplamalarını önler.
        j = i + 1

        # Sadece yakın olan birkaç noktaya bakılır
        # strip zaten y'ye göre sıralı olduğu için daha uzak nokta çiftlerinin mesafesi d'den büyük olacaktır.
        # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] ve d = 1.5 için i=0 olduğunda j=1 ve j=2 için çiftler incelenir.
        # i=0 ve j=1 olduğunda distance(strip[0], strip[1]) = distance((1, 1), (2, 2)) ≈ 1.4142135623730951 olarak hesaplanır ve min_dist 1.4142135623730951 olarak güncellenir.
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            # distance fonksiyonu, strip[i] ve strip[j] noktaları arasındaki Öklid mesafesini hesaplar.
            # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] için i=0 ve j=1 olduğunda distance(strip[0], strip[1]) = distance((1, 1), (2, 2)) ≈ 1.4142135623730951 olarak hesaplanır.
            # Bu mesafe, min_dist ile karşılaştırılır ve min_dist güncellenir.
            # Örneğin, strip = [(1, 1), (2, 2), (3, 3)] için i=0 ve j=1 olduğunda min_dist başlangıçta 1.5 olduğu için min_dist 1.4142135623730951 olarak güncellenir.
            # i=0 ve j=2 olduğunda distance(strip[0], strip[2]) = distance((1, 1), (3, 3)) ≈ 2.8284271247461903 olarak hesaplanır, ancak min_dist 1.4142135623730951 olduğu için min_dist güncellenmez.
            # i=1 ve j=2 olduğunda distance(strip[1], strip[2]) = distance((2, 2), (3, 3)) ≈ 1.4142135623730951 olarak hesaplanır, ancak min_dist zaten 1.4142135623730951 olduğu için min_dist güncellenmez.
            # Sonuç olarak, strip_closest fonksiyonu 1.4142135623730951 döndürecektir.
            dist = distance(strip[i], strip[j])
            min_dist = min(min_dist, dist)
            j += 1

    return min_dist


# closest_pair_recursive adında bir fonksiyon tanımlanır.
# Bu fonksiyonun amacı:
# verilen noktalar arasındaki en küçük Öklid mesafesini bulmaktır.
# Bu fonksiyon, böl ve fethet yaklaşımını kullanarak noktaları x ve y koordinatlarına göre sıralar ve en küçük mesafeyi hesaplar.
# Örneğin, points = [(0, 0), (3, 4), (7, 7)] için closest_pair_recursive fonksiyonu 5.0 döndürecektir.
# Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve diğer nokta çiftleri arasında daha küçük bir mesafe yoktur.
def closest_pair_recursive(px, py):
    """
    px: x'e göre sıralı noktalar
    py: y'ye göre sıralı noktalar
    """
    # n değişkeni, px listesindeki nokta sayısını saklar.
    # Örneğin, px = [(0, 0), (3, 4), (7, 7)] için n = 3 olacaktır.
    n = len(px)

    # Küçük problem → brute force
    # Eğer nokta sayısı 3 veya daha az ise, brute_force fonksiyonu çağrılır ve en küçük mesafe döndürülür.
    # Örneğin, px = [(0, 0), (3, 4)] için n = 2 olduğu için brute_force(px) fonksiyonu çağrılır ve 5.0 döndürülür.
    if n <= 3:
        return brute_force(px)

    # Ortadan böl
    # mid değişkeni, px listesinin ortasındaki indeks değerini saklar.
    mid = n // 2
    # mid_point değişkeni, px listesinin ortasındaki noktayı saklar.
    mid_point = px[mid]

    # Sol ve sağ noktolar olarak parçalanir
    # px_left ve px_right listeleri, px listesini ortadan bölerek sol ve sağ parçaları oluşturur.
    # Örneğin, px = [(0, 0), (3, 4), (7, 7)] için mid = 1 olduğu için mid_point = (3, 4) olacaktır.
    # px_left = [(0, 0)] ve px_right = [(3, 4), (7, 7)] olacaktır.
    px_left  = px[:mid]
    px_right = px[mid:]

    # px_left'teki noktaların py listesinde de bulunması gerekir, 
    # bu yüzden px_left'teki noktaların tuple'larını içeren bir set oluşturulur.
    px_left_set = set(map(tuple, px_left))

    # py_left ve py_right listeleri, py listesini px_left_set'e göre bölerek sol ve sağ parçaları oluşturur.
    # Örneğin, py = [(0, 0), (3, 4), (7, 7)] için px_left_set = {(0, 0)} olacaktır.
    # py_left = [(0, 0)] ve py_right = [(3, 4), (7, 7)] olacaktır.
    # py_left listesi, py listesindeki noktalar arasında px_left_set'te bulunan noktaları içerir.
    # py_right listesi, py listesindeki noktalar arasında px_left_set'te bulunmayan noktaları içerir.
    # Bu şekilde, px_left ve py_left listeleri aynı noktaları içerirken, px_right ve py_right listeleri aynı noktaları içerir.
    # Örneğin, px_left = [(0, 0)] ve py_left = [(0, 0)] olacaktır, px_right = [(3, 4), (7, 7)] ve py_right = [(3, 4), (7, 7)] olacaktır.
    # Bu bölme işlemi, böl ve fethet yaklaşımının bir parçasıdır ve her iki parçanın da aynı noktaları içermesini sağlar.
    py_left  = [p for p in py if tuple(p) in px_left_set]
    py_right = [p for p in py if tuple(p) not in px_left_set]

    # Sol ve sağ parçalar için rekürsif olarak en küçük mesafe bulunur.
    # closest_pair_recursive fonksiyonu, sıralanmış noktalar listesini alır
    # böl ve fethet yaklaşımını kullanarak en küçük mesafeyi hesaplar.
    # Örneğin, px_left = [(0, 0)] ve py_left = [(0, 0)] için closest_pair_recursive(px_left, py_left) fonksiyonu brute_force(px_left) fonksiyonunu çağırır ve 0.0 döndürür.
    # px_right = [(3, 4), (7, 7)] ve py_right = [(3, 4), (7, 7)] için closest_pair_recursive(px_right, py_right) fonksiyonu brute_force(px_right) fonksiyonunu çağırır ve 5.0 döndürür.
    # Bu şekilde, sol parçanın en küçük mesafesi 0.0 ve sağ parçanın en küçük mesafesi 5.0 olarak bulunur.
    # Bu mesafeler, böl ve fethet yaklaşımının bir parçasıdır ve her iki parçanın da en küçük mesafesini bulmamızı sağlar.
    dist_left = closest_pair_recursive(px_left, py_left)
    dist_right = closest_pair_recursive(px_right, py_right)

    # En küçük mesafe
    # dist_left ve dist_right değişkenleri, sol ve sağ parçaların en küçük mesafelerini saklar.
    # d değişkeni, dist_left ve dist_right arasında daha küçük olan değeri saklar.
    # Örneğin, dist_left = 0.0 ve dist_right = 5.0 için d = min(dist_left, dist_right) ifadesi 0.0 olarak hesaplanır.
    # Bu şekilde, sol ve sağ parçaların en küçük mesafesini karşılaştırarak genel olarak en küçük mesafeyi bulmamızı sağlar.
    # Bu mesafe, böl ve fethet yaklaşımının bir parçasıdır ve her iki parçanın da en küçük mesafesini bulmamızı sağlar.
    # Örneğin, px = [(0, 0), (3, 4), (7, 7)] için closest_pair_recursive(px, py) fonksiyonu 5.0 döndürecektir.
    # Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve diğer nokta çiftleri arasında daha küçük bir mesafe yoktur.
    d = min(dist_left, dist_right)

    # Orta çizgiye yakın noktalar (strip)
    # Strip, orta çizgiye yakın noktaları içerir ve bu noktalar arasında en küçük mesafe kontrol edilir.
    # Örneğin, d = 5.0 ve mid_point = (3, 4) için strip = [(0, 0), (3, 4)] olacaktır.

    strip = []
    # py listesindeki her bir nokta için döngü başlatılır.
    for point in py:
        # point[0] - mid_point[0] ifadesi, point noktasının x koordinatı ile mid_point noktasının x koordinatı arasındaki farkı hesaplar.
        # abs(point[0] - mid_point[0]) ifadesi, bu farkın mutlak değerini alır, böylece farkın pozitif veya negatif olmasına bakılmaksızın sadece büyüklüğü dikkate alınır.
        # abs(point[0] - mid_point[0]) < d ifadesi, point noktasının x koordinatının mid_point noktasının x koordinatına olan uzaklığının d'den küçük olup olmadığını kontrol eder.
        # Eğer abs(point[0] - mid_point[0]) < d ise, bu noktalar arasındaki mesafe d'den küçük olabilir, bu yüzden point noktası strip listesine eklenir.
        # Örneğin, d = 5.0 ve mid_point = (3, 4) için point = (0, 0) olduğunda abs(point[0] - mid_point[0]) = abs(0 - 3) = 3 < 5.0 olduğu için (0, 0) noktası strip listesine eklenir.
        # point = (3, 4) olduğunda abs(point[0] - mid_point[0]) = abs(3 - 3) = 0 < 5.0 olduğu için (3, 4) noktası strip listesine eklenir.
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    # Strip kontrolü
    # strip_closest fonksiyonu, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol eder ve eğer varsa bu mesafeyi döndürür.
    # Eğer strip içinde d'den küçük bir mesafe bulunmazsa, fonksiyon d'yi döndürür.
    # Örneğin, strip = [(0, 0), (3, 4)] ve d = 5.0 için strip_closest(strip, d) fonksiyonu 5.0 döndürecektir.
    # Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve bu mesafe d'ye eşittir, bu yüzden strip_closest fonksiyonu d'yi döndürecektir.
    # Eğer strip = [(0, 0), (3, 4)] ve d = 6.0 için strip_closest(strip, d) fonksiyonu 5.0 döndürecektir.
    # Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve bu mesafe d'den küçüktür, bu yüzden strip_closest fonksiyonu 5.0'ı döndürecektir.
    # Bu şekilde, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol ederek genel olarak en küçük mesafeyi bulmamızı sağlar.
    # Örneğin, px = [(0, 0), (3, 4), (7, 7)] için closest_pair_recursive(px, py) fonksiyonu 5.0 döndürecektir.
    return min(d, strip_closest(strip, d))


# closest_pair adında bir fonksiyon tanımlanır.
# Bu fonksiyonun amacı:
# verilen noktalar arasındaki en küçük Öklid mesafesini bulmaktır.
# Örneğin, points = [(0, 0), (3, 4), (7, 7)] için closest_pair fonksiyonu 5.0 döndürecektir.
# Çünkü (0, 0) ve (3, 4) noktaları arasındaki mesafe √((3-0)^2 + (4-0)^2) = 5.0'dır ve diğer nokta çiftleri arasında daha küçük bir mesafe yoktur.
def closest_pair(points):
    """
    Return the minimum Euclidean distance between any two distinct points.

    Args:
        points (list[tuple[int, int] | tuple[float, float]]):
            A list of 2D points represented as (x, y).

    Returns:
        float: Minimum Euclidean distance between any two points.
               Return 0.0 if fewer than two points are provided.
    """
    # 2'den az nokta varsa mesafe yok demektir, bu yüzden 0.0 döndürülür.
    # Örneğin, points = [(1, 2)] için sadece bir nokta vardır.
    # Bu nedenle herhangi iki nokta arasındaki mesafe tanımlanamaz, bu yüzden 0.0 döndürülür.
    if len(points) < 2:
        return 0.0
 
    # sorted fonksiyonu, verilen iterable'ı sıralar ve yeni bir liste döndürür.
    # key parametresi, sıralama için kullanılacak bir fonksiyon belirtir.
    # lambda ifadesi, tek kullanımlık anonim bir fonksiyon tanımlar.

    # X'e göre sıralama
    # px listesi, points listesini x koordinatına göre sıralar.
    # lambda p: (p[0], p[1]) ifadesi, her bir nokta p için bir tuple döndürür.
    # Bu tuple, önce x koordinatına göre sıralama yapar, eğer x koordinatları eşitse y koordinatına göre sıralama yapar.
    # Örneğin, points = [(3, 4), (1, 2), (1, 1)] için px listesi şu şekilde olacaktır:
    # px = [(1, 1), (1, 2), (3, 4)]
    px = sorted(points, key=lambda p: (p[0], p[1]))

    # Y'ye göre sıralama
    # lambda p: (p[1], p[0]) ifadesi, her bir nokta p için bir tuple döndürür.
    # Bu tuple, önce y koordinatına göre sıralama yapar, eğer y koordinatları eşitse x koordinatına göre sıralama yapar.
    # Örneğin, points = [(3, 4), (1, 2), (1, 1)] için py listesi şu şekilde olacaktır:
    #  py = [(1, 1), (1, 2), (3, 4)]
    py = sorted(points, key=lambda p: (p[1], p[0]))

    # closest_pair_recursive fonksiyonu, sıralanmış noktalar listesini alır
    # böl ve fethet yaklaşımını kullanarak en küçük mesafeyi hesaplar.
    return closest_pair_recursive(px, py)


# Time Complexity: O(n log n) 
# - Böl ve fethet yaklaşımı nedeniyle noktaların sıralanması O(n log n) zaman alır.
# - Her bölme işlemi O(n) zaman alır, ancak bu işlemler toplamda O(n log n) zaman karmaşıklığına sahiptir.
# strip_closest fonksiyonu, strip içindeki noktalar arasında d'den küçük bir mesafe olup olmadığını kontrol ederken O(n) zaman alır.
# Ancak strip_closest fonksiyonu sadece belirli nokta çiftlerini kontrol eder ve bu çiftlerin sayısı genellikle sabittir (en fazla 6 nokta), bu yüzden strip_closest fonksiyonunun zaman karmaşıklığı O(1) olarak kabul edilir.
# Bu nedenle, genel olarak closest_pair fonksiyonunun zaman karmaşıklığı O(n log n) olarak kabul edilir.
# strip_closest fonksiyonunun zaman karmaşıklığı O(n) olarak kabul edilirse, closest_pair fonksiyonunun zaman karmaşıklığı O(n log n + n) = O(n log n) olarak kalır, çünkü O(n log n) terimi baskındır.

# Space Complexity: O(n) 
# - Sıralanmış noktalar listeleri (px ve py) O(n) alan kullanır.
# - Rekürsif çağrılar nedeniyle ek O(n) alan kullanılır.
# strip listesi, orta çizgiye yakın noktaları içerir ve bu noktaların sayısı genellikle O(n) olabilir, bu nedenle strip listesi O(n) alan kullanır.
# distance fonksiyonu O(1) alan kullanır (sadece iki nokta arasındaki mesafeyi hesaplamak için sabit miktarda alan kullanır).
# Ancak, strip_closest fonksiyonunun space complexity'si O(n) olarak kabul edilirse, closest_pair fonksiyonunun space complexity'si O(n) olarak kalır, çünkü O(n) terimi baskındır.
# brute_force fonksiyonu O(1) alan kullanır (sadece birkaç nokta için mesafe hesaplaması yapar ve ek bir veri yapısı kullanmaz).
# Bu nedenle, brute_force fonksiyonunun space complexity'si O(1) olarak kabul edilir, ancak closest_pair fonksiyonunun genel space complexity'si O(n) olarak kalır, çünkü O(n) terimi baskındır.
# px_left_set gibi ek veri yapıları O(n) alan kullanır, ancak bu da closest_pair fonksiyonunun genel space complexity'si O(n) olarak kalır, çünkü O(n) terimi baskındır.
# Genel olarak, closest_pair fonksiyonunun space complexity'si O(n) olarak kabul edilir, çünkü sıralanmış noktalar listeleri, rekürsif çağrılar ve strip listesi gibi ek veri yapıları O(n) alan kullanır.


# Bu blok sadece dosya doğrudan çalıştırıldığında devreye girer.
# Eğer bu dosya başka bir dosya içinden import edilirse bu kısım çalışmaz.
if __name__ == "__main__":
    test_cases = [
        {
            # Örnek giriş listesi
            "points": [(0, 0), (3, 4), (7, 7)],
            # Beklenen sonuç
            "expected": 5.0,
        },
        {
            "points": [(1, 1), (2, 2), (10, 10)],
            "expected": math.sqrt(2),
        },
        {
            "points": [(5, 5)],
            "expected": 0.0,
        },
        {
            "points": [],
            "expected": 0.0,
        },
        {
            "points": [(0, 0), (0, 1), (10, 10)],
            "expected": 1.0,
        },
    ]

    tolerance = 1e-4

    for i, case in enumerate(test_cases, start=1):
        points = case["points"]
        expected = case["expected"]

        try:
            # benchmark fonksiyonu ile closest_pair fonksiyonunun performansı ölçülür.
            # benchmark:
            # - closest_pair fonksiyonu çağırılır
            # - sonucu alınır
            # - çalışma süresi ölçülür
            # - peak memory değeri ölçülür
            # - peak CPU kullanımı ölçülür
            # Burada closest_pair fonksiyonuna verilen parametreler:
            # points'dur.
            stats = benchmark(closest_pair, points)

            # stats["result"] içinde closest_pair fonksiyonunun çıktısı bulunur.
            result = stats["result"]

            passed = abs(result - expected) <= tolerance

            print(f"Test Case {i}")
            print(f"Input: points = {points}")
            print(f"Expected: {expected:.4f}")
            print(f"Result: {result:.4f}")
            print(f"Pass: {passed}")

            # Kodun çalışma süresi, milisaniye cinsinden yazdırılır.
            # .4f ifadesi virgülden sonra 4 basamak gösterir.
            print(f"Runtime: {stats['runtime_ms']:.4f} ms")

            # Kodun çalışması sırasında ulaşılan maksimum bellek miktarı megabayt cinsinden yazdırılır.
            print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")

            # Kodun çalışması sırasında ulaşılan maksimum CPU kullanım yüzdesi yazdırılır.
            print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
            print("-" * 50)

        except NotImplementedError as e:
            print(f"Test Case {i}")
            print(f"Input: points = {points}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break