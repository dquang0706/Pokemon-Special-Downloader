# Pokemon-Special-Downloader

Công cụ download truyện tranh **Pokémon Đặc Biệt** từ Archive.org với giao diện web dễ sử dụng. Hỗ trợ tải đa luồng để tối ưu tốc độ.

## 📋 Tính năng

- ✅ Tải 81 tập Pokémon Đặc Biệt từ Archive.org
- ✅ Giao diện web trực quan với thanh tiến trình
- ✅ Tải đa luồng song song (tùy chỉnh 1-10 luồng)
- ✅ Tự động bỏ qua file đã tải
- ✅ Logs chi tiết từng tập
- ✅ Hỗ trợ dừng quá trình tải

## 🛠 Yêu cầu

- **Python 3.6+**
- Kết nối internet ổn định
- Port 8080 khả dụng (hoặc sửa `PORT = 8080` trong script)

## 📥 Cài đặt

```bash
# Clone repo
git clone https://github.com/dquang0706/Pokemon-Special-Downloader.git
cd Pokemon-Special-Downloader

# Không cần cài đặt thêm thư viện (dùng built-in Python)
```

## 🚀 Cách sử dụng

### Chạy server

```bash
python pokemon_downloader.py
```

Output:
```
Pokemon Dac Biet Downloader
Mo trinh duyet: http://localhost:8080
Thu muc luu   : D:\TruyenPokemon\downloads
Nhan Ctrl+C de dung server
```

### Mở giao diện web

1. Mở trình duyệt: **http://localhost:8080**
2. Nhập số luồng song song (mặc định: 4)
3. Bấm **"Bắt đầu tải"**
4. Theo dõi tiến trình trong logs

### Folder lưu trữ

File sẽ được lưu vào thư mục `downloads` trong cùng thư mục với script:
```
Pokemon-Special-Downloader/
├── pokemon_downloader.py
├── downloads/
│   ├── Pokémon Đặc Biệt_Tập 01_Red Blue Green.pdf
│   ├── Pokémon Đặc Biệt_Tập 02_Red Blue Green.pdf
│   └── ... (81 tập)
└── README.md
```

## 📚 Nguồn dữ liệu

- **Kho lưu trữ**: [archive.org/download/pokemon-dac-biet](https://archive.org/download/pokemon-dac-biet)
- **Định dạng**: PDF
- **Tổng số**: 81 tập
- **Kích thước**: ~1-2GB tùy thuộc độ phân giải PDF

## 🔧 Tùy chỉnh

### Thay đổi port

```python
PORT = 8080  # Sửa thành port khác nếu cần
```

### Thay đổi nguồn download

```python
BASE_URL = "https://archive.org/download/pokemon-dac-biet"  # Thay đổi URL tại đây
```

### Thay đổi số luồng mặc định

Trong giao diện web, nhập số luồng trước khi bấm "Bắt đầu tải" (1-10 luồng).

## ⚠️ Lưu ý

- Lần đầu tải tất cả 81 tập sẽ mất **30 phút - 2 giờ** tùy tốc độ internet
- Script sẽ **tự động bỏ qua** file đã tải trước đó
- Nếu bị ngắt quá trình, chạy lại script sẽ tiếp tục từ file chưa tải
- Cần **1.5-2GB dung lượng** để lưu trữ toàn bộ truyện

## 🐛 Troubleshooting

### SSL Certificate Error
Nếu gặp lỗi `ssl:certificate_verify_failed`, script đã được sửa để bỏ qua kiểm tra SSL (chỉ cho mục đích tải từ archive.org).

### Port 8080 đang sử dụng
```bash
# Sửa PORT = 8080 thành số port khác (ví dụ: 9090)
```

### File tải không đầy đủ
Xóa file `.tmp` trong folder `downloads` và chạy lại script.

## 📝 License

Free to use for personal purposes. Nguồn dữ liệu từ Archive.org.

## 👨‍💻 Phát triển

Nếu bạn muốn cải tiến:
1. Fork repo này
2. Tạo branch mới (`git checkout -b feature/xyz`)
3. Commit thay đổi (`git commit -am 'Add xyz'`)
4. Push lên (`git push origin feature/xyz`)
5. Tạo Pull Request

---

**Tháng 6/2026** - Phiên bản 1.0