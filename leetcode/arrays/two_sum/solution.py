# tools klasörü içindeki benchmark fonksiyonunu projeye dahil ediyoruz.
# Bu fonksiyon sayesinde kodun çalışma süresi, bellek kullanımı ve CPU kullanımı ölçülebilir.
from tools.benchmark import benchmark

# two_sum adında bir fonksiyon tanımlıyoruz.
# Bu fonksiyonun amacı:
# Verilen nums listesi içinde toplamı target değerine eşit olan iki sayının index'ini bulmak.
def two_sum(nums, target):
    # seen adında boş bir sözlük oluşturuyoruz.
    # Bu sözlükte daha önce gördüğümüz sayıları tutacağız.
    # Yapı şu şekilde olacak:
    # anahtar (key) = sayı
    # değer (value) = o sayının index'i
    seen = {}

    # enumerate(nums) kullanarak liste üzerinde dolaşıyoruz.
    # i   -> o anki elemanın index'i
    # num -> o anki elemanın değeri
    for i, num in enumerate(nums):
        # Şu anki sayı ile hedef toplamı oluşturmak için hangi sayıya ihtiyaç duyduğumuzu hesaplıyoruz.
        # Örneğin:
        # target = 9 ve num = 2 ise
        # diff = 7 olur
        diff = target - num

        # Eğer ihtiyaç duyduğumuz sayı (diff) daha önce görülmüşse,
        # bu demektir ki:
        # önceki sayı + şu anki sayı = target
        if diff in seen:
            # O zaman sonucu döndürüyoruz.
            # seen[diff] -> daha önce gördüğümüz tamamlayıcı sayının index'i
            # i          -> şu anki sayının index'i
            return [seen[diff], i]

        # Eğer diff sözlükte yoksa,
        # şu anki sayıyı ve index'ini sözlüğe ekliyoruz.
        # Böylece sonraki adımlarda bu sayı başka bir elemanın tamamlayıcısı olabilir.
        seen[num] = i

    # Eğer hiçbir iki sayı target değerini vermiyorsa boş liste döndürüyoruz.
    # LeetCode'un bu sorusunda genelde her zaman bir çözüm olduğu varsayılır,
    # ama bu satır yine de güvenli bir kapanış sağlar.
    return []


# Bu blok sadece dosya doğrudan çalıştırıldığında devreye girer.
# Eğer bu dosya başka bir dosya içinden import edilirse bu kısım çalışmaz.
if __name__ == "__main__":
    # Örnek giriş listesi
    nums = [2, 7, 11, 15]
    # Hedef toplam değeri
    target = 9
    # benchmark fonksiyonu ile two_sum fonksiyonunu çalıştırıyoruz.
    # benchmark:
    # - two_sum fonksiyonunu çağırır
    # - sonucu alır
    # - çalışma süresini ölçer
    # - peak memory değerini ölçer
    # - peak CPU kullanımını ölçer
    # Burada two_sum fonksiyonuna verilen parametreler:
    # nums ve target
    stats = benchmark(two_sum, nums, target)

    # Fonksiyonun döndürdüğü gerçek sonucu yazdırıyoruz.
    # stats["result"] içinde two_sum fonksiyonunun çıktısı bulunur.
    print("Result:", stats["result"])

    # Kodun çalışma süresini milisaniye cinsinden yazdırıyoruz.
    # .4f ifadesi virgülden sonra 4 basamak gösterir.
    print(f"Runtime: {stats['runtime_ms']:.4f} ms")

    # Peak memory, yani kod çalışırken ulaşılan en yüksek bellek kullanımını MB cinsinden yazdırıyoruz.
    print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
    # Kod çalışırken ulaşılan en yüksek CPU kullanım yüzdesini yazdırıyoruz.
    print(f"Peak CPU: {stats['peak_cpu_percent']:.4f}%")
