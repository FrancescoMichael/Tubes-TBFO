# Tubes-TBFO

## Problem Description
Dalam pembuatan suatu bahasa pemogramman, tentunya diperlukan suatu pemeriksaan sintaks untuk memastikan kode sumber yang diberikan sudah sesuai bahasa dan dapat dieksekusi oleh mesin dengan baik. Parser yang kami buat bertujuan untuk memeriksa sintaks suatu kode sumber HTML, atau Hypertext Markup Language. HTML umumnya digunakan untuk membuat struktur dan tampilan seluruh konten yang ada di suatu website, sehingga perlu dipastikan bahwa halaman web dapat diinterpretasikan dan ditampilkan dengan benar oleh browser. Implementasi harus dapat mendeteksi kesalahan sintaks yang umum, seperti tag yang tidak ditutup dengan benar, tag yang tertumpuk dengan tidak sesuai, atau atribut yang tidak valid. Oleh karena itu, kami memutuskan untuk mengimplementasikan model komputasi abstrak yang dapat digunakan untuk mengenali bahasa kontekstual, yaitu Push Down Automata. Pushdown automata (PDA) adalah perluasan dari mesin berstatus terbatas (finite state machine) dengan tambahan tumpukan (stack), yang memberikan PDA kemampuan untuk "mengingat" informasi sepanjang jalannya dalam membaca masukan. Pada Tugas Besar ini, kami menggunakan bahasa Python untuk menciptakan PDA yang sesuai, juga struktur data Trie untuk membantu proses tokenizing

## Members and Responsibilities
| NIM  | NAME |
| ------------- | ------------- |
| 13522024  | Kristo Anugrah  | Membuat laporan, README. Membuat PDA, Membuat Rules, membuat run.py
| 13522037  | Farhan Nafis Rayhan  | Membuat laporan, README. Membuat proses tokenisasi, membuat program membaca file, membuat main.py, dan membuat struktur data Trie
| 13522038  | Francesco Michael Kusuma  | Membuat laporan, README. menggambar diagram PDA, membuat PDA

## How To Run
1. Masukkan [filePDA].py pada res/PDA/
2. Masukkan [fileHTML].py pada res/test/
3. pindah ke directory src/ dengan 'cd/src'
4. pada Command Line Input, jalankan 'python main.py [filePDA].py "[fileHTML].py"'

## Struktur Program
TUBES-TBFO
|-- res
|   |-- PDA
|       |-- pda.txt
|-- test
|   |-- accept1.html
|   |-- accept2.html
|   |-- accept3.html
|   |-- accept4.html
|   |-- accept5.html
|   |-- accept6.html
|   |-- inputAcc.html
|   |-- inputReject.html
|   |-- reject1.html
|   |-- reject2.html
|   |-- reject3.html
|   |-- reject4.html
|   |-- reject5.html
|   |-- reject6.html
|-- src
|   |-- Rules.py
|   |-- Token.py
|   |-- Trie.py
|   |-- TrieNode.py
|   |-- main.py
|   |-- run.py
|-- .gitignore
|-- README.md
