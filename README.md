Project Capstone Asah Dicoding
Team:
1. Mizana amaliya (React & Backend)
2. Ganesha tania Pramesti (React & Backend)
3. Richy Julianto (React & Backend)
4. Farah aulia Hadi (Machine Lerning) 
5. Iklima Fatma (Machine Lerning)

AI Learning Insight
AI Learning Insight adalah fitur dashboard untuk website Studi Independent yang dirancang untuk membantu mahasiswa memahami pola belajar mereka. Terinspirasi dari Strava, sistem ini menganalisis aktivitas belajar pengguna dan memberikan insight yang actionable untuk meningkatkan efektivitas belajar.

About The Project
Sistem ini menganalisis aktivitas belajar pengguna dan menghasilkan tiga informasi utama. Pertama, Most Active Time yang menunjukkan kapan pengguna paling fokus belajar seperti pagi, siang, atau malam, sehingga pengguna dapat memanfaatkan waktu tersebut untuk materi yang lebih sulit. Kedua, Consistency Score yang memberikan skor tingkat konsistensi belajar dari hari ke hari dengan insight seperti "Kamu belajar 4 dari 7 hari minggu ini, tingkat konsistenmu tinggi". Ketiga, Learning Pattern yang mengelompokkan siswa berdasarkan pola aktivitas menjadi Consistent Learner, Fast Learner, atau Reflective Learner.

Tech Stack
Backend menggunakan Node.js dengan Express untuk API server, MongoDB sebagai database, dan Python untuk machine learning model. Frontend dibangun dengan React untuk user interface. Machine learning menggunakan Python dengan library scikit-learn, pandas, dan numpy untuk analisis pola belajar.

Getting Started
Backend setup memerlukan Node.js dan MongoDB. Install dependencies dengan npm install di folder backend, buat file .env dengan konfigurasi database dan port, lalu jalankan server dengan npm run dev.
Machine learning setup memerlukan Python 3.11 atau lebih tinggi. Buat virtual environment dengan python -m venv .venv, aktifkan dengan .venv\Scripts\activate di Windows atau source .venv/bin/activate di Mac/Linux, install dependencies dengan pip install -r backend/model_dev/requirements.txt, dan test dengan python test_python.py.
Frontend setup memerlukan install dependencies dengan npm install di folder frontend dan jalankan development server dengan npm start.