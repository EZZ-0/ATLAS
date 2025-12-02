# ⚡ ATLAS Financial Intelligence

**Professional-grade financial analysis and valuation platform for USA publicly traded companies.**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

---

## 🎯 Features

### **Data Extraction**
- SEC EDGAR API integration (10-K, 10-Q, S-1 filings)
- Yahoo Finance data (real-time market data)
- 350+ financial metrics extraction
- Multi-source reconciliation

### **Financial Analysis**
- **DCF Valuation:** 3-scenario modeling (Bear/Base/Bull)
- **Forensic Accounting:** Altman Z-Score, Beneish M-Score, Piotroski F-Score
- **Technical Analysis:** RSI, MACD, Moving Averages, Support/Resistance
- **Quant Analysis:** Fama-French factors, risk-adjusted returns
- **Peer Comparison:** Auto peer discovery, percentile rankings

### **Investment Intelligence**
- Automated IC-ready investment memos
- Bull/bear case generation
- Risk assessment heatmaps
- Catalyst timeline
- PDF report export

### **AI Advisory**
- Google Gemini 2.0 integration
- CFA-level financial analysis
- Real-time metric explanations

---

## 🚀 Quick Start

### **Method 1: Run Locally**

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/atlas-financial-intelligence.git
cd atlas-financial-intelligence

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.template .env
# Add your GEMINI_API_KEY

# Run app
streamlit run usa_app.py
```

### **Method 2: One-Click Launch**

Double-click `run_app.bat` (Windows)

---

## 📊 Tech Stack

- **Frontend:** Streamlit
- **Data Sources:** SEC EDGAR API, Yahoo Finance
- **Visualization:** Plotly
- **AI:** Google Gemini 2.0 Flash
- **Export:** ReportLab (PDF)

---

## 📁 Project Structure

```
atlas-financial-intelligence/
├── usa_app.py              # Main Streamlit app
├── usa_backend.py          # Data extraction engine
├── dcf_modeling.py         # DCF valuation
├── investment_summary.py   # IC memo generation
├── dashboard_tab.py        # Dashboard UI
├── analysis_tab.py         # Deep dive analysis
├── quant_tab.py           # Quantitative analysis
├── compare_tab.py         # Peer comparison
├── governance_tab.py      # Corporate governance
├── financial_ai.py        # AI advisor
├── config/                # Configuration
├── utils/                 # Security & logging
└── .streamlit/           # Streamlit config
```

---

## 🔐 Security

- Input validation (SQL injection, XSS prevention)
- API key encryption
- Centralized logging
- No data storage (stateless)

---

## 📝 License

© 2025 Atlas Financial Intelligence. All rights reserved.

---

## 🤝 Contributing

This is a professional portfolio project. For questions or collaboration:
- Open an issue on GitHub
- Contact via LinkedIn

---

## ⚙️ Environment Variables

Required in `.env` or Streamlit Secrets:

```bash
GEMINI_API_KEY=your_key_here
```

Optional:
```bash
NEWSAPI_KEY=your_key_here  # For premium news sources
```

---

## 📈 Performance

- Extraction: 3-5 seconds per company
- DCF Analysis: <1 second
- Full analysis suite: 5-10 seconds
- Supports 500+ S&P 500 companies

---

**Built with precision. Powered by data.**
