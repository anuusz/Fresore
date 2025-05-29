# <span style="font-family: 'Satisfy', cursive; font-size: 1.5em;">fresore</span>  

**Solusi Digital untuk Manajemen Vendor Buah & Sayuran**  

Aplikasi ini lahir dari pengalaman langsung sebagai karyawan di startup vendor buah dan sayuran. Fresore mengotomatisasi alur kerja yang sebelumnya manual dan rentan *human error*, sehingga meningkatkan akurasi dan menjaga citra perusahaan.  

**🔐 Akses Terkontrol**:  
- Hanya **partner terdaftar** (mitra perusahaan) yang dapat mengakses.  
- Pendaftaran memerlukan persetujuan admin perusahaan.  

---

## ✨ Fitur Utama  
- **Login dengan Autentikasi Khusus**  
  - Register hanya via persetujuan perusahaan.  
- **Manajemen Produk**  
  - Tambah/edit/hapus produk (harga, stok, kategori).  
- **Pembayaran & Invoice**  
  - Generate PDF invoice otomatis.  
  - Rekapitulasi pembayaran transfer bulanan.  

---

## 🛠️ Teknologi  
| **Frontend**       | **Backend**         | **Database** |  
|--------------------|---------------------|--------------|  
| Vue 3 (Composition API) | Django 5.2         | PostgreSQL   |  
| Pinia (State Management) | Django REST Framework |             |  
| Axios (HTTP Client)     | JWT Authentication |              |  

---

### Prasyarat  
- PostgreSQL (untuk database).  
- Python 3.10+ dan Node.js 18+, bun 1.2.

## ⚙️ Instalasi
### 2. Frontend (Django) 
```bash
cd ff  
npm install  
npm run dev  
```  

### 2. Backend (Django)  
```bash
cd bf  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  

# Install dependencies  
pip install -r requirements.txt  

# Setup database (Pastikan PostgreSQL sudah berjalan)  
python manage.py migrate  
python manage.py createsuperuser  # Untuk akun admin  
python manage.py runserver
```
