This project started as a command-line password manager and is being developed into a fully functional desktop application.

The application uses password-based key derivation and encryption to protect stored credentials. The long-term goal is to provide a simple, secure, and practical password-management solution.

✨ Current Features
🔐 Password encryption using Fernet
🔑 Password-based key derivation using PBKDF2-HMAC
➕ Add account credentials
👁️ View and decrypt saved passwords
💾 Local password storage
🖥️ GUI development using CustomTkinter
🚀 Planned Features
🔒 Master password login
📊 Modern dashboard
➕ Add, edit, and delete credentials
🔎 Search saved accounts
👁️ Show/hide passwords
📋 Copy passwords to clipboard
🎲 Secure password generator
💪 Password-strength indicator
⏱️ Automatic session locking
🗄️ SQLite database storage
⚙️ Application settings
📦 Windows executable build
🔐 Improved security architecture
🛠️ Technologies Used
Python
CustomTkinter — Graphical user interface
Cryptography — Encryption and key derivation
SQLite — Planned database storage
Git & GitHub — Version control
📂 Project Structure
Password-Manager/
│
├── app.py
├── password_manager.py
├── password.txt
├── requirements.txt
└── README.md

The project structure may change as new features are added.

🔐 Security

The project currently uses:

Fernet symmetric encryption
PBKDF2-HMAC with SHA-256
100,000 PBKDF2 iterations

The current implementation is intended primarily for learning and development. It should not be considered production-grade password-management software yet.

Security improvements will be made as the project develops.

⚙️ Installation
1. Clone the repository
git clone https://github.com/singhbrarharmandeep0-hue/Password-Manager.git
2. Open the project
cd Password-Manager
3. Install dependencies
pip install cryptography customtkinter

Or, once requirements.txt is available:

pip install -r requirements.txt
4. Run the application
python app.py