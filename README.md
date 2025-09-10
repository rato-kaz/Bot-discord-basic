🤖 My Discord Bot

Một bot Discord đa chức năng được viết bằng Python + discord.py, có thể:

Quản lý server (moderation)

Phát nhạc từ YouTube

Chào mừng thành viên mới

Tích hợp Stable Diffusion để tạo ảnh từ prompt

(Sắp tới) Tích hợp AI Chatbot (GPT, Hugging Face, …)

📂 Cấu trúc dự án
my-discord-bot/
├── bot.py               # Entry point chính
├── cogs/                # Các module lệnh (command handler)
│   ├── moderation.py
│   ├── music.py
│   ├── welcome.py
│   └── stable_diffusion.py
├── events/              # Event listener
│   ├── on_ready.py
│   ├── on_member_join.py
│   └── on_message.py
├── utils/               # Helper functions, DB, checks
│   ├── database.py
│   ├── checks.py
│   └── helpers.py
├── data/                # Logs, cache
│   ├── logs/
│   └── cache.json
├── config.json          # Config chung (prefix, settings)
├── .env                 # Chứa token/API key (không push lên git!)
├── requirements.txt     # Các thư viện cần cài
└── README.md

🚀 Cài đặt
1. Clone repo
git clone https://github.com/rato-kaz/Bot-discord-basic.git
cd my-discord-bot

2. Tạo virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

3. Cài dependencies
pip install -r requirements.txt

🔑 Cấu hình

Tạo file .env (không push lên git):

BOT_TOKEN=your_discord_bot_token
HF_API_KEY=your_huggingface_api_token


File config.json ví dụ:

{
  "prefix": "!",
  "default_volume": 50,
  "welcome_channel": 123456789012345678
}

▶️ Chạy bot
python bot.py

⚙️ Các tính năng
1. Moderation

!kick @user – kick user

!ban @user – ban user

2. Music

!play <youtube_url> – phát nhạc từ YouTube

!stop – dừng phát

3. Welcome

Tự động gửi lời chào khi có người mới vào server

4. Stable Diffusion (AI Image)

!imagine <prompt> – tạo ảnh từ văn bản

🌐 Triển khai

Bạn có thể deploy bot bằng:

Heroku (dễ dàng, miễn phí giới hạn)

Railway.app

Docker

VPS riêng

🛡️ Lưu ý bảo mật

Không bao giờ push .env hoặc token lên GitHub

Dùng GitHub Secrets nếu deploy qua CI/CD

📜 License

MIT License