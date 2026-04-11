#Implementation of Autokey Cipher and Redefence Cipher

## Përshkrimi i Projektit

Ky projekt implementon dy algoritme klasike të kriptografisë:

* **Autokey Cipher**
* **Redefence Cipher**

Qëllimi i projektit është të demonstrojë implementimin e algoritmeve të enkriptimit dhe dekriptimit duke përdorur teknika klasike të kriptografisë.

Programi mundëson:

* Enkriptimin e një mesazhi (plaintext)
* Dekriptimin e një mesazhi të enkriptuar (ciphertext)

Projekti është implementuar në gjuhën programuese **Python** dhe ekzekutohet përmes një ndërfaqeje të thjeshtë në terminal.

---

# Algoritmet e Implementuara

## 1. Autokey Cipher

Autokey Cipher është një **cipher polialfabetik** që përdor një çelës fillestar dhe më pas e zgjeron atë duke përdorur vetë tekstin origjinal (plaintext).

### Procesi i Enkriptimit

1. Fillojmë me një çelës fillestar.
2. Çelësi zgjerohet duke shtuar tekstin origjinal.
3. Çdo shkronjë konvertohet në një numër sipas alfabetit:

A = 0, B = 1, C = 2, ..., Z = 25

4. Përdoret formula:

C = (P + K) mod 26

Ku:

* **P** = vlera e shkronjës së plaintext
* **K** = vlera e shkronjës së çelësit
* **C** = vlera e shkronjës së ciphertext

### Procesi i Dekriptimit

Formula për dekriptim është:

P = (C - K) mod 26

Pas çdo hapi të dekriptimit, shkronja e rikuperuar i shtohet çelësit për të vazhduar procesin.

---

## 2. Redefence Cipher

Redefence Cipher është një **cipher transpozimi**. Në këtë algoritëm nuk ndryshohen shkronjat, por **ndryshohet renditja e tyre** për të krijuar tekstin e enkriptuar.

### Hapat e Enkriptimit

1. Teksti origjinal shkruhet në rreshta sipas një modeli të caktuar ose një çelësi.
2. Shkronjat vendosen në një strukturë të caktuar.
3. Teksti i enkriptuar merret duke lexuar shkronjat sipas një renditjeje të përcaktuar.

### Hapat e Dekriptimit

1. Rindërtohet struktura që është përdorur gjatë enkriptimit.
2. Shkronjat e ciphertext vendosen në pozicionet përkatëse.
3. Teksti origjinal lexohet sipas renditjes fillestare.

---


# Si të Ekzekutohet Projekti

1. Klono repository nga GitHub

```
git clone https://github.com/your-username/crypto-ciphers-project.git
```

2. Hyr në folderin e projektit

```
cd crypto-ciphers-project
```

3. Ekzekuto programin

```
python src/main.py
```

---

# Shembull – Autokey Cipher

Plaintext:

```
HELLO
```

Çelësi:

```
KEY
```

Ciphertext (shembull):

```
RIJSS
```

---

# Shembull – Redefence Cipher

Plaintext:

```
HELLOWORLD
```

Çelësi (numri i rreshtave):

```
3
```

Ciphertext (shembull):

```
HOLELWRDLO
```

---


# Autori

Student: Grejona Gashi, Gerti Parduzi, Elmaze Murati, Genti Kafexhiu
---

Lënda: Siguri e të dhënave

---
