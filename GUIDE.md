# Tech Interview Prep - Student Guide

Bu repository, öğrencilerin teknik mülakatlara düzenli ve kontrollü şekilde hazırlanması için oluşturulmuştur.

Bu repo içinde iki ana çalışma alanı vardır:

- `leetcode/` → LeetCode problem çözümleri
- `mock_interviews/` → Amazon, Meta, Google ve Microsoft coding mock interview çözümleri

---

## 1. Repository amacı

Bu repository'nin amacı:

- problem çözme pratiği yapmak
- temiz kod yazmak
- çözüm mantığını açıklayabilmek
- time complexity ve space complexity düşünme alışkanlığı kazanmak
- branch, commit ve pull request gibi Git/GitHub çalışma düzenini öğrenmek

---

## 2. Genel çalışma mantığı

Bu repo içinde çalışma düzeni şöyledir:

- Öğretmen problem klasörünü ve problem açıklamasını hazırlar.
- Öğrenci kendi branch'inde çözüm geliştirir.
- Öğrenci çözümü tamamladıktan sonra commit atar.
- Öğrenci kendi branch'ini GitHub'a push eder.
- Öğrenci Pull Request (PR) açar.
- Öğretmen çözümü inceler ve uygun bulursa `main` branch'e merge eder.

---

## 3. Önemli kurallar

### 3.1 Doğrudan `main` branch üzerinde çalışmayın

Her öğrenci kendi feature branch'inde çalışmalıdır.

**Yanlış:**
- `main` branch üzerinde çözüm geliştirmek

**Doğru:**
- yeni bir branch açıp o branch üzerinde çözüm geliştirmek

---

### 3.2 `README.md` dosyasını öğretmen hazırlar

Problem açıklaması, örnek input-output ve complexity beklentisi gibi içerikler öğretmen tarafından hazırlanır.

Öğrenci tarafında ana odak dosya genelde:

- `solution.py`

olacaktır.

---

### 3.3 Her problem için klasör yapısına sadık kalın

Örnek:

```text
leetcode/
└── arrays/
    └── two_sum/
        ├── README.md
        └── solution.py
```

---

### 3.4 Boşuna yeni dosya üretmeyin

Aynı problem için rastgele yeni dosyalar açmayın.

**Yanlış:**
- `solution_final.py`
- `new_solution.py`
- `burak_solution_v2.py`

**Doğru:**
- mevcut `solution.py` dosyasını düzenlemek

---

### 3.5 Editör dosyalarını push etmeyin

Aşağıdaki gibi dosyalar repoya gönderilmemelidir:

- `.idea/`
- `.vscode/`
- `__pycache__/`
- `.venv/`

---

## 4. Branch açma standardı

Branch isimleri düzenli olmalıdır.

Önerilen format:

```text
feature/ismin-problem-adi
```

Örnekler:

```text
feature/burak-two-sum
feature/ayse-valid-parentheses
feature/ali-amazon-top-k-frequent
```

---

## 5. Öğrenci çalışma akışı

Aşağıdaki akış takip edilmelidir.

### Adım 1 - Repository'yi clone et

```bash
git clone REPOSITORY_URL
```

### Adım 2 - Repository klasörüne gir

```bash
cd tech-interview-prep
```

### Adım 3 - Güncel hali çek

```bash
git pull origin main
```

### Adım 4 - Yeni branch aç

```bash
git checkout -b feature/ismin-problem-adi
```

Örnek:

```bash
git checkout -b feature/burak-two-sum
```

### Adım 5 - İlgili problem klasörüne git ve çözümü yaz

Örnek dosya:

```text
leetcode/arrays/two_sum/solution.py
```

### Adım 6 - Kodunu test et

Örnek:

```bash
python -m leetcode.arrays.two_sum.solution
```

### Adım 7 - Değişiklikleri commit et

```bash
git add .
git commit -m "Solve two sum problem"
```

### Adım 8 - Branch'i GitHub'a push et

```bash
git push -u origin feature/ismin-problem-adi
```

### Adım 9 - Pull Request aç

GitHub üzerinden kendi branch'inizi `main` branch'ine karşı PR olarak açın.

---

## 6. Problem çözme standardı

Bir problem çözülürken şu başlıklar düşünülmelidir:

- Problem ne istiyor?
- En basit çözüm nedir?
- Daha iyi çözüm var mı?
- Hangi veri yapısı daha uygundur?
- Time complexity nedir?
- Space complexity nedir?

Öğrenciden beklenen şey sadece çalışan kod yazmak değildir.  
Aynı zamanda çözüm mantığını da anlaması beklenir.

---

## 7. Complexity yazım standardı

Her çözümde şu iki kavram düşünülmelidir:

- **Time Complexity**
- **Space Complexity**

Örnek:

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

**Önemli not:**  
Gerçek çalışma süresi ile Big-O aynı şey değildir.

- `O(n)` teorik analizdir.
- Runtime ölçümü ise pratik çalıştırma sonucudur.

İkisi birlikte düşünülmelidir.

---

## 8. Benchmark kullanımı

Repo içinde ortak benchmark aracı bulunmaktadır:

```text
tools/benchmark.py
```

Bu araç şu metrikleri ölçmek için kullanılabilir:

- runtime
- peak memory
- peak CPU usage

Örnek kullanım:

```python
from tools.benchmark import benchmark


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    stats = benchmark(two_sum, nums, target)

    print("Result:", stats["result"])
    print(f"Runtime: {stats['runtime_ms']:.4f} ms")
    print(f"Peak memory: {stats['peak_memory_mb']:.4f} MB")
    print(f"Peak CPU: {stats['peak_cpu_percent']:.2f}%")
```

### Benchmark hakkında önemli not

Benchmark sonucu ile complexity aynı şey değildir.

Örnek:

- Runtime: `0.01 ms`
- Time Complexity: `O(n)`

Bunlar farklı kavramlardır.

---

## 9. Commit mesajı standardı

Commit mesajları basit ve açıklayıcı olmalıdır.

**Doğru örnekler:**

```text
Solve two sum problem
Add benchmark utility
Update two sum README
Fix bug in valid parentheses solution
```

**Yanlış örnekler:**

```text
final
last version
update
new code
123
```

---

## 10. Pull Request başlığı standardı

PR başlıkları düzenli olmalıdır.

Önerilen format:

```text
[LeetCode][Topic] Problem Name
[Mock Interview][Company] Problem Name
```

Örnekler:

```text
[LeetCode][Arrays] Solve Two Sum
[LeetCode][Strings] Solve Valid Anagram
[Mock Interview][Amazon] Solve Top K Frequent Elements
```

---

## 11. Pull Request açıklaması standardı

PR açıklaması şu yapıda olabilir:

```md
## Summary
Solved the problem using a hash map approach.

## Details
- Added working solution in `solution.py`
- Used shared benchmark utility
- Verified output with sample input

## Complexity
- Time: O(n)
- Space: O(n)
```

---

## 12. Mock interview klasör yapısı

Mock interview çalışmaları şirket bazlı tutulur.

Örnek yapı:

```text
mock_interviews/
├── amazon/
│   └── coding/
├── meta/
│   └── coding/
├── google/
│   └── coding/
└── microsoft/
    └── coding/
```

Burada da aynı çalışma mantığı geçerlidir:

- öğretmen ilgili klasörü hazırlar
- öğrenci kendi branch'inde çözüm geliştirir
- PR açar

---

## 13. Sık yapılan hatalar

### Hata 1 - `main` branch üzerinde çalışmak

Bunu yapmayın. Her zaman feature branch açın.

### Hata 2 - `.idea/`, `.vscode/`, `.venv/` gibi dosyaları push etmek

Bunlar kişisel geliştirme ortamı dosyalarıdır. Repoya gönderilmemelidir.

### Hata 3 - Aynı problem için yeni yeni dosya isimleri üretmek

Mevcut `solution.py` dosyası kullanılmalıdır.

### Hata 4 - Benchmark ile complexity'yi karıştırmak

- Benchmark = pratik ölçüm
- Complexity = teorik analiz

### Hata 5 - Kodu test etmeden push etmek

Push öncesi çözüm mutlaka çalıştırılmalıdır.

---

## 14. Push öncesi kontrol listesi

Push atmadan önce şunları kontrol edin:

- Doğru branch'te miyim?
- Doğru dosyayı mı düzenledim?
- Kod çalışıyor mu?
- Gereksiz dosya ekledim mi?
- `.idea/` veya `.venv/` gibi dosyalar stage edildi mi?
- Commit mesajım açıklayıcı mı?

---

## 15. Kısa özet

Bu repo içinde doğru çalışma düzeni şudur:

1. Repo'yu clone et
2. Güncel kodu çek
3. Yeni branch aç
4. Çözümü `solution.py` içine yaz
5. Kodu test et
6. Commit at
7. Branch'i push et
8. Pull Request aç
9. Öğretmen review etsin
10. Uygun görülürse merge edilsin

---

## 16. Son not

Bu repo sadece problem çözmek için değil,  
aynı zamanda profesyonel yazılım geliştirme alışkanlığı kazanmak için kullanılmaktadır.

Bu yüzden aşağıdaki konular en az çözüm kadar önemlidir:

- düzenli klasör yapısı
- temiz commit geçmişi
- branch disiplini
- açıklayıcı PR
- kod okunabilirliği
- complexity farkındalığı