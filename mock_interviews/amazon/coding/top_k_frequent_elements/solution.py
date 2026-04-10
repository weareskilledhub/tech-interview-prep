# tools klasörü içindeki benchmark fonksiyonunu projeye dahil edilir.
# Bu fonksiyon sayesinde kodun çalışma süresi, bellek kullanımı ve CPU kullanımı ölçülebilir.
from tools.benchmark import benchmark

# top_k_frequent adında bir fonksiyon tanımlanır.
# Bu fonksiyonun amacı:
# Verilen nums listesi içinde en sık geçen k elemanı bulmaktır.
def top_k_frequent(nums, k):
    """
    Return the k most frequent elements.

    Args:
        nums (list[int]): List of integers.
        k (int): Number of most frequent elements to return.

    Returns:
        list[int]: The k most frequent elements.
    """
    # frequency adında boş bir sözlük oluşturulur.
    # Bu sözlük, her bir sayının kaç kez göründüğünü saymak için kullanılacaktır.
    # Yapı:
    # key   -> sayı
    # value -> kaç kere geçtiği (frekans)
    frequency = {}

    # nums listesindeki her bir num için döngü başlatılır.
    # Bu döngü, her bir numun kaç kez göründüğünü saymak için frequency sözlüğünü doldurur.
    # Örneğin, nums = [1, 1, 1, 2, 2, 3] için frequency sözlüğü şu şekilde olacaktır:
    # {1: 3, 2: 2, 3: 1}
    for num in nums:
        # Eğer num zaten frequency sözlüğünde varsa, sayacını 1 artırır.
        if num in frequency:
            frequency[num] += 1
        else:
            # Eğer num frequency sözlüğünde yoksa, onu sözlüğe ekler ve sayacını 1 olarak başlatır.
            frequency[num] = 1

    # bucket adında bir liste oluşturulur.
    # Bu liste, frequency sözlüğündeki frekanslara göre sayıları gruplamak için kullanılacaktır.
    # index = frekans
    # value = o frekansta olan sayılar
    # bucket listesi, nums listesinin uzunluğundan bir fazla eleman içerecek şekilde oluşturulur.
    # Maksimum frekans len(nums) olabilir.
    # Çünkü bir sayı en fazla nums listesinin uzunluğu kadar görünebilir (örneğin, nums = [1, 1, 1, 1] için 1 sayısı 4 kez görünebilir).
    # bucket listesi, her bir frekans için o frekansa sahip sayıları içeren alt listeler içerir.
    # Örneğin, nums = [1, 1, 1, 2, 2, 3] için bucket listesi şu şekilde olacaktır:
    # bucket[0] = []       # Hiçbir sayı 0 kez görünmez
    # bucket[1] = [3]      # 3 sayısı 1 kez görünür
    # bucket[2] = [2]      # 2 sayısı 2 kez görünür
    # bucket[3] = [1]      # 1 sayısı 3 kez görünür
    # bucket[4] = []       # Hiçbir sayı 4 kez görünmez
    bucket = [[] for _ in range(len(nums) + 1)]

    # frequency sözlüğündeki her bir sayı için, sayacına göre bucket'a ekleme yapılır.
    for n in frequency:
        # frequency sözlüğünden n sayısının kaç kez göründüğü alınır.
        # Bu sayı, bucket listesinde n sayısının eklenmesi gereken indeksi belirler.
        count = frequency[n] 
        # n sayısı, bucket listesinde count indeksine eklenir.
        # Örneğin, frequency sözlüğünde 1 sayısı 3 kez göründüğü için, bucket[3] listesine 1 eklenir.
        bucket[count].append(n)

    # result adında boş bir liste oluşturulur.
    # Bu liste, en sık geçen k elemanı saklamak için kullanılacaktır.
    result = []

    # bucket listesi sondan başa doğru taranır çünkü en yüksek frekansa sahip sayılar bucket'ın sonlarında bulunur.
    for i in range(len(bucket) - 1, 0, -1):

        # bucket listesi sondan başa doğru taranırken, her bir frekans için o frekansta olan sayılar result listesine eklenir.
        # Örneğin, bucket[3] listesinde 1 sayısı varsa, bu sayı result listesine eklenir.
        for num in bucket[i]:
            # num sayısı result listesine eklenir.
            result.append(num)

            # Eğer result listesinde k eleman varsa, bu noktada en sık geçen k eleman bulunmuş demektir ve result listesi döndürülür.
            # Örneğin, k = 2 için, result listesinde 1 ve 2 sayıları varsa, bu noktada result listesi döndürülür.
            if len(result) == k: 
                return result

# Time Complexity: O(n) 
# Listeyi birkaç kez dolaşılır:
# 1. frequency sözlüğünü oluşturmak için nums listesini bir kez dolaşırız (O(n)).
# 2. frequency sözlüğündeki her bir sayı için bucket listesine ekleme yapmak için frequency sözlüğünü bir kez dolaşırız (O(n)).
# 3. bucket listesi sondan başa doğru taranır ve en sık geçen k eleman bulunur (O(n)).
# Ama sıralama yok, nested loop yok (tam anlamıyla n² değil)
# Bu yüzden lineer.

# Space Complexity: O(n) 
# freq → n kadar yer tutar
# bucket → n kadar yer tutar
# result → k kadar yer tutar (genel olarak O(n) olarak kabul edilir)

# Bu blok sadece dosya doğrudan çalıştırıldığında devreye girer.
# Eğer bu dosya başka bir dosya içinden import edilirse bu kısım çalışmaz.
if __name__ == "__main__":
    test_cases = [
        {
            # Örnek giriş listesi
            "nums": [1, 1, 1, 2, 2, 3],
            # Bulunması istenen en sık geçen eleman sayısı
            "k": 2,
            # Beklenen sonuç
            "expected": [1, 2],
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1],
        },
        {
            "nums": [4, 4, 4, 5, 5, 6, 6, 6, 6],
            "k": 2,
            "expected": [6, 4],
        },
        {
            "nums": [1, 2, 3, 4],
            "k": 1,
            "expected_options": [[1], [2], [3], [4]],
        },
        {
            "nums": [5, 5, 5, 5],
            "k": 1,
            "expected": [5],
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        nums = case["nums"]
        k = case["k"]

        try:
            # benchmark fonksiyonu ile top_k_frequent fonksiyonunun performansı ölçülür.
            # benchmark:
            # - top_k_frequent fonksiyonu çağırılır
            # - sonucu alınır
            # - çalışma süresi ölçülür
            # - peak memory değeri ölçülür
            # - peak CPU kullanımı ölçülür
            # Burada top_k_frequent fonksiyonuna verilen parametreler:
            # nums ve k'dır.
            stats = benchmark(top_k_frequent, nums, k)

            # stats["result"] içinde top_k_frequent fonksiyonunun çıktısı bulunur.
            result = stats["result"]

            if "expected" in case:
                passed = sorted(result) == sorted(case["expected"])
                expected_display = case["expected"]
            else:
                passed = any(sorted(result) == sorted(option) for option in case["expected_options"])
                expected_display = case["expected_options"]

            print(f"Test Case {i}")
            print(f"Input: nums = {nums}, k = {k}")
            print(f"Expected: {expected_display}")
            print(f"Result: {result}")
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
            print(f"Input: nums = {nums}, k = {k}")
            print("Solution is not implemented yet.")
            print(f"Details: {e}")
            print("-" * 50)
            break