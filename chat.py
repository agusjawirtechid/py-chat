import requests
import os
import time
import hashlib
import urllib.parse

db = "https://python-loginsytem-default-rtdb.asia-southeast1.firebasedatabase.app/chattan.json"
db_login = "https://python-loginsytem-default-rtdb.asia-southeast1.firebasedatabase.app/login"
ai = "https://api.nekolabs.web.id/text.gen/grok/3-jailbreak/v1?text=Jawab%20SELAU%20singkat%2C%20padat%2C%20dan%20to%20the%20point.%20Jika%20diminta%20membuat%20script%2Fkode%2Fprogram%2C%20jawab%20%22GK%20boleh%2C%20kepanjangan.%22%20Jawaban%20maksimal%202%20kalimat.Promt:"


print("="*20)
print(" GRUP DARI PYTHON")
print("="*20)
print("1. login \n2. Register")
pilih = input("MASUKAN 1/2 : ")

def chat(username):
  while True:
    req = requests.get(db)
    data = req.json()
    
    os.system("clear")
    print("=========Grup=========")
    print("Ketik @ai untuk bertanya kepada ai")
    if data:
      for k, v in data.items():
        print(f"{v['user']} : {v['pesan']}")
    else:
      print("Chat kosong")
    
    pesan = input(">")
    if pesan.lower() == "exit":
      break
    
    if "@ai" in pesan:
      promt = urllib.parse.quote(pesan)
      ai_req = requests.get(f"{ai}{promt}").json()
      result_ai = ai_req["result"]
      print(result_ai)
      requests.post(db, json={
        "user": "AI",
        "pesan": result_ai
      })
      continue
      
    
    isi = {
      "user": username,
      "pesan": pesan
    }
    requests.post(db, json=isi)
    time.sleep(0.5)

def login():
  username = input("Masukan username: ")
  password = input("Masukan password: ")
  pass_kuat = hashlib.sha256(password.encode()).hexdigest()
  
  cek = requests.get(f"{db_login}/{username}.json").json()
  if not cek:
    print("Tidak ada username itu!!")
  elif pass_kuat == cek['password']:
    os.system('clear')
    print("berhasil login")
    return username
  else:
    print("password salah")

def register():
  user_reg = input("Masukan Username: ")
  pass_reg = input("Masukan Password: ")
  pass_kuat = hashlib.sha256(pass_reg.encode()).hexdigest()
  
  data = {
    "username": user_reg,
    "password": pass_kuat
  }
  cek = requests.get(f"{db_login}/{user_reg}.json").json()
  if cek:
    print("Username Udah dipake")
  else:
    requests.put(f"{db_login}/{user_reg}.json", json=data)
    print("Berhasil, Silahkan login")

if pilih == "1":
  user = login()
  if user:
    chat(user)
elif pilih == "2":
  register()