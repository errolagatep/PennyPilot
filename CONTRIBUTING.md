# Contributing to AI-Powered Budget Tracker

Thank you for your interest in contributing to the AI-Powered Budget Tracker! 🎉

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/ai-budget-tracker.git
   cd ai-budget-tracker
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 💡 How to Contribute

### 🐛 Bug Reports
- Check if the bug has already been reported in [Issues](https://github.com/yourusername/ai-budget-tracker/issues)
- Create a new issue with:
  - Clear, descriptive title
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots if applicable
  - Your environment (OS, Python version, etc.)

### ✨ Feature Requests
- Check existing feature requests in [Issues](https://github.com/yourusername/ai-budget-tracker/issues)
- Open a new issue with:
  - Clear description of the feature
  - Use case/motivation
  - Possible implementation approach

### 🔧 Code Contributions

#### Areas for Contribution
- **New Chart Types**: Additional visualization options
- **Export Formats**: Support for more file formats
- **AI Enhancements**: Better categorization, more analysis types
- **UI/UX Improvements**: Better mobile experience, accessibility
- **Performance**: Optimizations for large datasets
- **Testing**: Unit tests, integration tests
- **Documentation**: Code comments, user guides

#### Development Guidelines

1. **Code Style**:
   - Follow PEP 8 for Python code
   - Use meaningful variable names
   - Add docstrings for functions and classes
   - Keep functions focused and concise

2. **File Structure**:
   - `streamlit_app.py`: Main UI and page logic
   - `budget_tracker_web.py`: Core business logic
   - `create_base_database.py`: Database initialization
   - `sample_data.py`: Test data generation

3. **Testing**:
   - Test your changes thoroughly
   - Ensure the app runs without errors
   - Test both with and without OpenAI API key
   - Test data import/export functionality

4. **Commit Messages**:
   ```
   feat: add new chart type for expense trends
   fix: resolve date formatting issue in exports
   docs: update README with new installation steps
   style: improve mobile responsive design
   ```

## 📝 Pull Request Process

1. **Before submitting**:
   - Ensure your code follows the style guidelines
   - Test your changes thoroughly
   - Update documentation if needed
   - Make sure all existing functionality still works

2. **Pull Request**:
   - Create a clear, descriptive title
   - Provide a detailed description of changes
   - Reference any related issues
   - Include screenshots for UI changes

3. **Review Process**:
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Once approved, your PR will be merged

## 🏗️ Development Setup

### Prerequisites
- Python 3.7+
- Git
- Code editor (VS Code recommended)

### Optional Setup
- **OpenAI API Key**: For testing AI features
- **Excel**: For testing data compatibility

### Running Tests
```bash
# Run the application
streamlit run streamlit_app.py

# Generate test data
python sample_data.py

# Create fresh database
python create_base_database.py
```

## 🎯 Project Goals

Our project aims to:
- **Accessibility**: Make personal finance tracking accessible to everyone
- **Intelligence**: Leverage AI to provide meaningful insights
- **Simplicity**: Keep the interface clean and intuitive
- **Privacy**: Ensure user data stays local and secure
- **Flexibility**: Support various workflows and preferences

## 📚 Resources

### Learn About the Tech Stack
- **Streamlit**: [Documentation](https://docs.streamlit.io/)
- **Plotly**: [Python Guide](https://plotly.com/python/)
- **Pandas**: [User Guide](https://pandas.pydata.org/docs/user_guide/)
- **OpenAI API**: [Documentation](https://platform.openai.com/docs)

### Design Guidelines
- **Material Design**: For UI consistency
- **Accessibility**: WCAG 2.1 guidelines
- **Mobile-First**: Responsive design principles

## 🤝 Community

- **Discussions**: Use GitHub Discussions for questions and ideas
- **Issues**: Report bugs and request features
- **Pull Requests**: Contribute code improvements

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be:
- Added to the project's contributors list
- Mentioned in release notes for significant contributions
- Credited in the app's about section

---

**Thank you for contributing to make personal finance management better for everyone!** 🎉