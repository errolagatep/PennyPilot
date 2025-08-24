# 💰 AI-Powered Budget Tracker

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-orange.svg)](https://openai.com/)

A comprehensive web-based budget tracking application built with Streamlit, featuring Excel data integration and AI-powered financial insights. Perfect for personal finance management with intelligent categorization and analysis.

## 🚀 Live Demo

![Budget Tracker Demo](docs/demo-screenshot.png)

*Note: Add your own OpenAI API key to enable AI features*

## ✨ Features

### 🎯 Core Functionality
- **💻 Interactive Web Dashboard**: Modern, responsive web interface
- **📊 Excel Integration**: Store and manage data in Excel files (works like a database)
- **📈 Real-time Charts**: Interactive visualizations with Plotly
- **🤖 AI-Powered Analysis**: Intelligent spending insights using OpenAI GPT
- **📁 Data Management**: Upload/download Excel files, filter and view data
- **🏷️ Expense Categorization**: Automatic AI categorization of expenses
- **🎯 Financial Goal Setting**: Track progress toward financial objectives

### 🆕 New Features
- **👤 First-Time User Setup**: Guided onboarding with financial profile creation
- **📅 Multiple Data Views**: View data by All Time, Current Month, or Current Year
- **🎨 Improved Navigation**: Clean, vertical list navigation in sidebar
- **💾 User Profile Storage**: Personal financial goals and preferences in Excel
- **📱 Mobile-Friendly**: Responsive design that works on all devices  

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-budget-tracker.git
cd ai-budget-tracker
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key (Optional)
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```

Then edit `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

> **Note:** The app works without an API key, but AI features (categorization, analysis) will be disabled.

### 5. Generate Sample Data (Optional)
```bash
python sample_data.py
```

> **Tip:** You can also generate sample data from within the app during first-time setup!

### 6. Run the Application

**Option A: Using batch file (Windows)**
```bash
run_app.bat
```

**Option B: Direct command**
```bash
streamlit run streamlit_app.py
```

**Option C: Using Python**
```bash
python -m streamlit run streamlit_app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## Application Structure

### Pages

1. **📊 Dashboard**
   - Key financial metrics (Balance, Income, Expenses)
   - Interactive charts (Pie chart, Bar chart, Trend analysis)
   - Recent transactions view
   - Visual analytics overview

2. **➕ Add Transaction**
   - Add income or expense transactions
   - AI-powered expense categorization
   - Date and amount input
   - Real-time data updates

3. **🤖 AI Analysis**
   - AI-powered spending analysis
   - Personalized budget recommendations
   - Financial pattern insights
   - Smart recommendations based on spending habits

4. **📁 Data Management**
   - View all transactions with filters
   - Upload Excel files
   - Download data as Excel or CSV
   - Data import/export functionality

### Key Features

#### Excel Integration
- **📊 Database-like Storage**: Excel files with data integrity and validation
- **📥 Smart Import**: Upload existing Excel files with automatic format detection  
- **📤 Flexible Export**: Download data in Excel or CSV with period-specific naming
- **🔄 External Compatibility**: Standard Excel format for editing in Microsoft Excel, Google Sheets, etc.

#### Interactive Charts
- **Expense Pie Chart**: Visual breakdown of spending by category
- **Monthly Trends**: Income vs expenses over time
- **Running Balance**: Balance progression over time
- **Category Analysis**: Horizontal bar chart of spending categories

#### 🤖 AI Features (Optional - requires OpenAI API key)
- **🏷️ Smart Categorization**: Automatic expense categorization using GPT-3.5-turbo
- **📈 Spending Analysis**: AI-generated insights about spending patterns and trends
- **💡 Budget Recommendations**: Personalized budget advice using 50/30/20 rule
- **🎯 Financial Coaching**: Intelligent suggestions for financial improvement and goal achievement

## 📂 Project Structure

```
ai-budget-tracker/
├── 📄 streamlit_app.py           # Main Streamlit application
├── 📄 budget_tracker_web.py      # Core budget tracking logic
├── 📄 create_base_database.py    # Database initialization script
├── 📄 sample_data.py             # Generate sample data for testing
├── 📄 run_app.bat                # Windows batch file to run the app
├── 📄 requirements.txt           # Python dependencies
├── 📄 .env.example              # Environment variables template
├── 📄 .gitignore                # Git ignore file
├── 📄 LICENSE                   # MIT License
├── 📄 README.md                 # This file
├── 📁 docs/                     # Documentation and screenshots
└── 📊 *.xlsx                    # Excel data files (auto-generated, git-ignored)
```

## 💡 Usage Tips

### First-Time Users
1. **Complete Setup**: The app will guide you through initial setup on first launch
2. **Add Sample Data**: Use the "Add Sample Data" button to explore features
3. **Set Financial Goals**: Input your income, savings goals, and expense limits

### Power Users
1. **Time Period Views**: Switch between All Time, Current Month, and Current Year views
2. **Data Export**: Download your data in Excel or CSV format with period-specific filenames
3. **AI Features**: Set your OpenAI API key for intelligent expense categorization and analysis
4. **Data Import**: Upload existing Excel files with columns: type, amount, description, category, date

### Mobile Users
- **Responsive Design**: Works seamlessly on phones and tablets
- **Touch-Friendly**: All buttons and interactions optimized for mobile

## Data Format

When importing Excel files, ensure the following columns:
- `type`: "income" or "expense"
- `amount`: Numerical value
- `description`: Text description of the transaction
- `category`: Category name
- `date`: Date in YYYY-MM-DD format

## 🐛 Troubleshooting

<details>
<summary><strong>Common Issues & Solutions</strong></summary>

### Installation Issues
- **Module Import Errors**: Ensure virtual environment is activated and dependencies installed
- **Python Version**: Requires Python 3.7 or higher
- **Streamlit Issues**: Try `pip install --upgrade streamlit`

### AI Features
- **AI Not Working**: Verify OPENAI_API_KEY is set in `.env` file
- **Categories Show "Other"**: API key may be invalid or OpenAI service unavailable

### Data Issues
- **Excel Import Fails**: Ensure columns are named: type, amount, description, category, date
- **Date Format Issues**: Use YYYY-MM-DD format or Excel date format
- **Large Files**: App handles thousands of transactions efficiently

### Performance
- **Slow Loading**: First load creates database files automatically
- **Port Issues**: Streamlit auto-finds available ports (usually 8501-8510)

</details>

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Quick Start for Contributors
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit: `git commit -am 'Add new feature'`
5. Push: `git push origin feature-name`
6. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web app framework
- **Plotly** - For beautiful, interactive charts
- **OpenAI** - For AI-powered financial insights
- **Pandas & Openpyxl** - For robust Excel data handling

## 🌟 Advanced Features

<details>
<summary><strong>Technical Features</strong></summary>

### Performance Optimizations
- **🚀 Fast Loading**: Streamlit caching for instant data access
- **📊 Efficient Charts**: Optimized Plotly rendering
- **💾 Smart Storage**: Excel files work like a database with integrity checks
- **🔄 Real-time Updates**: Changes reflect immediately across all pages

### Data Management
- **✅ Data Validation**: Automatic validation and correction of imported data
- **🔒 Data Integrity**: ID uniqueness and proper sequencing maintained
- **📤 Export Options**: Multiple formats (Excel, CSV) with smart naming
- **🔍 Advanced Filtering**: Dynamic filtering by date, category, and type

### User Experience
- **📱 Mobile-First**: Responsive design for all devices
- **🎨 Modern UI**: Clean, intuitive interface with proper spacing
- **♿ Accessibility**: Screen reader friendly with proper labels
- **🌐 Cross-Platform**: Works on Windows, macOS, and Linux

</details>

---

<div align="center">

**🛠️ Built with:** Streamlit • Plotly • Pandas • OpenAI API • Openpyxl  
**🖥️ Compatible with:** Windows • macOS • Linux  
**🐍 Python Version:** 3.7+

**⭐ If this project helps you, please give it a star! ⭐**

</div>