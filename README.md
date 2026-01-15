# 💬 Python Firebase Chat + Login System

Aplikasi **chat grup berbasis terminal (CLI)** menggunakan **Python + Firebase Realtime Database**.  
Dilengkapi dengan:
- 🔐 Login & Register (password di-hash)
- 💬 Chat grup realtime (refresh loop)
- 🤖 AI responder dengan trigger `@ai`
- ☁️ Backend Firebase (REST API)
- 📱 Cocok dijalankan di **Termux / Linux / Windows**

---

## 🚀 Fitur
- Register & Login user
- Password aman menggunakan **SHA256**
- Chat grup berbasis Firebase
- Deteksi chat kosong
- Auto-handle data Firebase yang rusak
- AI bot dengan trigger `@ai`
- Encode input otomatis (`URL Encoding`)

---

## 📦 PIP / Library yang Dibutuhkan

Install dulu semua dependency:

```bash
pip install requests
