import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 1. Pengaturan Akun & Server
pengirim = "pastibisa7913@gmail.com"
kata_sandi = "bosq ntim sfqa rlzx"  # Gunakan App Password, bukan kata sandi akun biasa
penerima = "hgsh682@gmail.com"

# 2. Membuat Struktur Email
pesan = MIMEMultipart()
pesan["From"] = pengirim
pesan["To"] = penerima
pesan["Subject"] = "Uji Coba Pengiriman Email Python"

isi_email = "Halo, ini adalah email uji coba yang dikirim menggunakan skrip Python!"
pesan.attach(MIMEText(isi_email, "plain"))

# 3. Menghubungkan ke Server SMTP dan Mengirim Email
try:
    # Menggunakan server SMTP Gmail (port 587 untuk TLS)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Mengamankan koneksi dengan TLS
    server.login(pengirim, kata_sandi)

    # Mengirim email
    teks = pesan.as_string()
    server.sendmail(pengirim, penerima, teks)
    print("Email berhasil dikirim!")

except Exception as e:
    print(f"Gagal mengirim email: {e}")

finally:
    server.quit()
