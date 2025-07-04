# 🧠 Discord Logger Bot

Bot Discord này được thiết kế để ghi lại **toàn bộ các hoạt động tin nhắn và cập nhật kênh quan trọng** trong server của bạn. Bot sẽ gửi các thông báo chi tiết dưới dạng embed vào một kênh log chuyên dụng trên Discord, đồng thời lưu trữ các log này vào **các tệp `.txt` riêng biệt theo ngày** trên máy chủ của bạn.

---

## 📌 Tính năng

- 💬 **Ghi log Tin nhắn mới**: Ghi lại nội dung tin nhắn, tác giả và kênh cho mọi tin nhắn mới.
- 🗑️ **Ghi log Tin nhắn bị xóa**: Theo dõi và ghi lại nội dung, tác giả và kênh của tin nhắn đã bị xóa.
- ✏️ **Ghi log Tin nhắn đã chỉnh sửa**: Ghi lại nội dung trước và sau khi chỉnh sửa, tác giả và kênh.
- 📁 **Ghi log Cập nhật Kênh**: Ghi lại các thay đổi về tên của các kênh văn bản trong server.
- 🕒 **Dấu thời gian chính xác**: Tất cả các log đều bao gồm dấu thời gian theo múi giờ `Asia/Bangkok`.
- 📋 **Hiển thị Embed trực quan**: Gửi các thông báo log dưới dạng embed đẹp mắt và dễ đọc vào kênh Discord được chỉ định.
- 💾 **Lưu trữ Log cục bộ**: Tự động lưu các log chi tiết vào các tệp `.txt` riêng biệt cho từng ngày trong thư mục `logs/`.
- 🔒 **Tự động lọc**: Bỏ qua các tin nhắn và hoạt động từ chính bot hoặc các bot khác để tránh log lặp.

---

## ⚙️ Yêu cầu

- **Python `>=3.10`**
- Các thư viện Python sau:

```bash
pip install -r requirements.txt
```
## 🚀 Hướng dẫn chạy bot

1. Clone source về:

   ```bash
   git clone https://github.com/jennienguyn/botdiscordlog.git
   cd botdiscordlog
   ```

2. Tạo file `.env` hoặc đặt token trong biến môi trường:

   **Cách 1 – Dùng `.env`:**

   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

   **Cách 2 – Sửa trực tiếp trong `bot.py`:**

   ```python
   TOKEN = "your_bot_token_here"
   ```

3. Chạy bot:

   ```bash
   python bot.py
   ```

## 🛡️ Phân quyền cần thiết

Bot cần quyền sau:

* `Read Messages`
* `Read Message History`
* `Send Messages`
* `Embed Links`

Khuyến nghị **tạo riêng role cho bot** và cấp cho nó quyền truy cập các kênh cần ghi log.

## 🧪 Dev Mode

* Timestamp sử dụng `ZoneInfo("Asia/Bangkok")` → yêu cầu `tzdata`
* Có thể chỉnh lại `create_embed()` theo ý bạn

## 📂 Cấu trúc thư mục

```
├── bot.py              # File chính chạy bot
├── requirements.txt    # Thư viện cần thiết
└── README.md           # Hướng dẫn sử dụng
```

## 👨‍💻 Đóng góp

Repo này chỉ dành cho team dev nội bộ. Nếu bạn muốn đóng góp, hãy liên hệ quản trị viên để được thêm quyền truy cập.

## 📄 License

🔒 Private – Internal use only.
