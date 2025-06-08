# 🧠 Discord Logger Bot

Bot Discord ghi lại toàn bộ tin nhắn trong tất cả các kênh và gửi embed vào một kênh log (hoặc thực hiện các hành động tùy chỉnh khác).

## 📌 Tính năng

- 📝 Ghi lại toàn bộ tin nhắn trong server
- 🕒 Thêm timestamp theo múi giờ `Asia/Bangkok`
- 📋 Hiển thị embed nội dung tin nhắn, user gửi, kênh gửi
- 🔒 Tự động lọc bỏ bot messages và DMs

## ⚙️ Yêu cầu

- Python `>=3.10`
- Các thư viện sau:

```bash
pip install -r requirements.txt
````

Nội dung `requirements.txt`:

```
discord.py>=2.3.2
tzdata
```

## 🚀 Hướng dẫn chạy bot

1. Clone source về:

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
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
