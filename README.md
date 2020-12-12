# kamus-bahasa-alay

* Dataset diambil dari beberapa kalimat alay di twitter, dan di filtering lagi menjadi sebuah OOV
* Dari OOV (kata alay) yang kita dapatkan akan digenerate sebuah kode soundex berdasarkan rule (createsoundex.py)
* Ketika OOV sudah tergenerate kemudian lanjut kita generate Soundex kode untuk Kamus KBBI
* Ketika Kata Alay (OOV) dan Kamus KBBI sudah tergenerate masing masing kode soundexnya lanjut kita proses dengan algoritma levenshtein distance.

- Createsoundex.py for generate soundex code (OOVSOUNDEX.csv)
- Main.py for generate the right word depends on OOV (OOVDUMMY.csv) and KAMUS KBBI (KAMUSDUMMY) Data.
- Write.csv is result from main.py
