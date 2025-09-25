# 🔐 SecAudit – Linux Server Security Audit & Hardening Tool

SecAudit is a modular and professional-grade security audit tool for Linux servers. It scans, reports, and optionally hardens your system following security best practices.

## ✅ Features
- Automated security checks (SSH, users, firewall, services)
- Modular design
- CLI interface
- Markdown report generation
- Optional hardening steps

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/secaudit.git
cd secaudit
pip install -r requirements.txt
sudo python3 main.py --scan
```

## 📂 Project Structure
- `main.py` – CLI entry point
- `modules/` – Individual audit checks
- `utils/` – Logging, report generator, etc.
- `reports/` – Markdown audit reports
- `logs/` – Action logs

## 📄 License
MIT License
