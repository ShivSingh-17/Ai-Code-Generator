# AI Code Generator 🤖💻

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red.svg)
![Gemini API](https://img.shields.io/badge/Gemini-AI-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> An intelligent AI-powered code generation tool built with Google's Gemini API and Streamlit that transforms natural language descriptions into production-ready code across multiple programming languages.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-app-name.streamlit.app)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Live Demo](#live-demo)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [API Integration](#api-integration)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

**AI Code Generator** is an intelligent web application that leverages Google's Gemini AI to automatically generate high-quality code from natural language descriptions. Simply describe what you want to build in plain English, and the AI will generate complete, functional code with explanations and best practices.

### Why This Project?

- **Accelerate Development**: Generate boilerplate code instantly, saving hours of repetitive coding
- **Learn by Example**: See how experienced developers would solve problems through AI-generated code
- **Multi-Language Support**: Generate code in Python, JavaScript, Java, C++, and more
- **Iterative Refinement**: Refine and improve generated code through conversational prompts
- **Educational Tool**: Perfect for students learning programming concepts through examples

### Key Capabilities

1. **Natural Language to Code**: Describe functionality in plain English and get working code
2. **Code Explanation**: Get detailed explanations of generated code logic and structure
3. **Multiple Programming Languages**: Support for 10+ popular programming languages
4. **Code Optimization**: Request optimized versions of code for better performance
5. **Bug Fixing**: Describe errors and get corrected code with explanations
6. **Code Refactoring**: Transform existing code to follow best practices
7. **Algorithm Implementation**: Generate implementations of common algorithms and data structures

---

## ✨ Features

### Core Functionality
- 🤖 **AI-Powered Generation**: Leverages Google Gemini 2.5 Flash for fast, accurate code generation
- 🌐 **Multi-Language Support**: Python, JavaScript, TypeScript, Java, C++, C#, Go, Ruby, PHP, Swift
- 💬 **Interactive Chat Interface**: Conversational UI for iterative code refinement
- 📝 **Syntax Highlighting**: Beautiful code display with language-specific syntax highlighting
- 📋 **One-Click Copy**: Copy generated code to clipboard instantly
- 💾 **Download Support**: Download generated code as files with proper extensions
- 🔄 **Conversation History**: Maintain context across multiple code generation requests
- 🎨 **Modern UI/UX**: Clean, intuitive Streamlit interface with responsive design

### Advanced Features
- 🔍 **Code Analysis**: Analyze existing code for improvements and potential bugs
- 📊 **Complexity Estimation**: Get time and space complexity analysis
- 🧪 **Test Case Generation**: Automatically generate unit tests for your code
- 📚 **Documentation Generation**: Create comprehensive docstrings and comments
- 🔧 **Debugging Assistant**: Help identify and fix errors in existing code
- 🚀 **Performance Optimization**: Suggestions for improving code efficiency
- 🎓 **Learning Mode**: Step-by-step explanations for educational purposes

---

## 🌐 Live Demo

**Try the live application**: [https://ai-code-generator-shiv.streamlit.app](https://ai-code-generator-shiv.streamlit.app)

> **Note**: If the above link shows "app is sleeping", click the button to wake it up. Free tier apps on Streamlit Cloud sleep after inactivity.

### Demo Video
[Watch Demo Video](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) *(Add your demo video link)*

### Screenshots

#### Main Interface
![Main Interface](images/main-interface.png)
*The clean, intuitive chat interface for code generation*

#### Code Output Example
![Code Output](images/code-output.png)
*Generated code with syntax highlighting and explanations*

---

## 🛠️ Technology Stack

### Frontend
- **Streamlit 1.31+**: Modern Python web framework for building the interactive UI
- **HTML/CSS**: Custom styling for enhanced user experience
- **Streamlit Components**: Enhanced widgets and interactive elements

### Backend & AI
- **Python 3.9+**: Core programming language
- **Google Gemini API 2.5 Flash**: State-of-the-art LLM for code generation
- **google-generativeai Library**: Official Python SDK for Gemini API

### Code Processing
- **Pygments**: Syntax highlighting for multiple programming languages
- **Regular Expressions**: Code parsing and extraction
- **Markdown**: Formatted code display with proper indentation

### Deployment
- **Streamlit Cloud**: Free cloud hosting platform
- **GitHub Actions**: CI/CD pipeline for automated deployment
- **Environment Variables**: Secure API key management

---

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- Google Gemini API key (free tier available)
- Git (for cloning the repository)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ShivSingh-17/Ai-Code-Generator.git
cd Ai-Code-Generator
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### Step 5: Configure API Key

#### Method 1: Environment Variable (Recommended)
```bash
# On Windows
set GEMINI_API_KEY=your_api_key_here

# On macOS/Linux
export GEMINI_API_KEY=your_api_key_here
```

#### Method 2: Streamlit Secrets (For Deployment)
Create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

#### Method 3: Direct Input in App
The app also supports entering API key directly in the sidebar.

### Step 6: Run the Application
```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

---

## 💻 Usage

### Basic Code Generation

1. **Enter Your Prompt**: In the chat input, describe what code you want to generate
   ```
   Example: "Create a Python function to calculate fibonacci numbers"
   ```

2. **Select Programming Language** (Optional): Use the sidebar to specify your preferred language
   - Default: Python
   - Available: Python, JavaScript, Java, C++, Go, etc.

3. **Submit**: Press Enter or click the send button

4. **Review Generated Code**: The AI will generate code with:
   - Complete implementation
   - Comments and documentation
   - Usage examples
   - Complexity analysis

5. **Copy or Download**: Use the copy button or download the code as a file

### Advanced Usage

#### Code Explanation
```
Prompt: "Explain how binary search works and implement it in Python"
```

#### Code Optimization
```
Prompt: "Optimize this bubble sort function for better performance: [paste your code]"
```

#### Bug Fixing
```
Prompt: "Fix the bug in this code: [paste your code with error description]"
```

#### Test Generation
```
Prompt: "Generate unit tests for this function: [paste your function]"
```

#### Refactoring
```
Prompt: "Refactor this code following SOLID principles: [paste your code]"
```

### Example Prompts

**Web Development:**
```
- "Create a REST API endpoint using Flask for user authentication"
- "Generate a React component for a product card with image, title, and price"
- "Write Express.js middleware for request logging"
```

**Data Science:**
```
- "Implement a decision tree classifier from scratch in Python"
- "Create a function to perform k-means clustering on a dataset"
- "Generate code to visualize a correlation matrix using matplotlib"
```

**Algorithms:**
```
- "Implement Dijkstra's shortest path algorithm in Python"
- "Create a function to solve the N-Queens problem using backtracking"
- "Write code for merge sort with detailed comments"
```

**Database Operations:**
```
- "Generate SQLAlchemy models for a blog database with posts and comments"
- "Create MongoDB queries for aggregating user statistics"
- "Write Python code to perform ETL from CSV to PostgreSQL"
```

---

## 📁 Project Structure

```
Ai-Code-Generator/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── .gitignore                      # Git ignore file
│
├── .streamlit/
│   ├── config.toml                 # Streamlit configuration
│   └── secrets.toml                # API keys (not committed)
│
├── src/
│   ├── __init__.py
│   ├── code_generator.py           # Core code generation logic
│   ├── gemini_client.py            # Gemini API wrapper
│   ├── code_processor.py           # Code parsing and formatting
│   ├── language_config.py          # Programming language configurations
│   └── utils.py                    # Utility functions
│
├── components/
│   ├── __init__.py
│   ├── chat_interface.py           # Chat UI components
│   ├── code_display.py             # Code display with syntax highlighting
│   └── sidebar.py                  # Sidebar configuration
│
├── styles/
│   ├── main.css                    # Custom CSS styling
│   └── code_theme.css              # Code block themes
│
├── assets/
│   ├── logo.png                    # Application logo
│   └── favicon.ico                 # Browser favicon
│
├── tests/
│   ├── test_code_generator.py      # Unit tests
│   ├── test_gemini_client.py
│   └── test_utils.py
│
├── notebooks/
│   └── api_testing.ipynb           # Jupyter notebook for testing
│
├── docs/
│   ├── API_DOCUMENTATION.md        # API integration guide
│   ├── DEPLOYMENT.md               # Deployment instructions
│   └── EXAMPLES.md                 # Code generation examples
│
└── images/
    ├── main-interface.png          # Screenshots for README
    └── code-output.png
```

---

## 🔧 How It Works

### Architecture Overview

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│                 │      │                  │      │                 │
│  User Interface │─────▶│  Streamlit App   │─────▶│  Gemini API     │
│   (Browser)     │      │   (Python)       │      │   (Google)      │
│                 │      │                  │      │                 │
└─────────────────┘      └──────────────────┘      └─────────────────┘
         │                        │                         │
         │                        ▼                         │
         │               ┌──────────────────┐              │
         │               │                  │              │
         └──────────────▶│  Code Processor  │◀─────────────┘
                         │  & Formatter     │
                         │                  │
                         └──────────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │                  │
                         │  Syntax          │
                         │  Highlighting    │
                         │                  │
                         └──────────────────┘
```

### Workflow

1. **User Input**: User enters a natural language prompt describing desired code
2. **Prompt Engineering**: The app constructs an optimized prompt for Gemini API
3. **API Request**: Sends request to Google Gemini 2.5 Flash with conversation history
4. **Response Processing**: Receives generated code and extracts relevant sections
5. **Syntax Highlighting**: Applies language-specific formatting using Pygments
6. **Display**: Renders formatted code in Streamlit with interactive features
7. **User Actions**: User can copy, download, or request modifications

### Gemini API Integration

```python
import google.generativeai as genai
import streamlit as st

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate code
response = model.generate_content(
    prompt,
    generation_config={
        'temperature': 0.7,
        'top_p': 0.95,
        'top_k': 40,
        'max_output_tokens': 2048,
    }
)

# Extract code
code = response.text
```

### Prompt Engineering Strategy

The app uses sophisticated prompt engineering to get optimal results:

```python
system_prompt = f"""
You are an expert programmer specializing in {language}.
Generate clean, efficient, and well-documented code.

Requirements:
1. Include comprehensive comments
2. Follow best practices and design patterns
3. Add error handling where appropriate
4. Provide usage examples
5. Explain time and space complexity

User Request: {user_prompt}
"""
```

---

## 📚 Examples

### Example 1: Data Structure Implementation

**Prompt:**
```
Create a binary search tree class in Python with insert, search, and delete methods
```

**Generated Code:**
```python
class TreeNode:
    """Node class for Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Binary Search Tree implementation.
    
    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    """
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search."""
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Usage Example
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
print(bst.search(30))  # Returns TreeNode with value 30
```

### Example 2: API Development

**Prompt:**
```
Create a Flask REST API with CRUD operations for a Todo application
```

**Generated Code:**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    """Todo model for database."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

# CREATE
@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo item."""
    data = request.get_json()
    new_todo = Todo(
        title=data['title'],
        description=data.get('description', '')
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# READ (All)
@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todo items."""
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

# READ (Single)
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo item."""
    todo = Todo.query.get_or_404(todo_id)
    return jsonify(todo.to_dict())

# UPDATE
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo item."""
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)
    
    db.session.commit()
    return jsonify(todo.to_dict())

# DELETE
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo item."""
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

## 🔐 API Integration

### Gemini API Setup

#### Get API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with Google account
3. Navigate to "Get API Key"
4. Create new API key or use existing one

#### API Configuration

```python
import google.generativeai as genai

# Configure API key
genai.configure(api_key='YOUR_API_KEY_HERE')

# Initialize model
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    generation_config={
        'temperature': 0.7,        # Creativity level (0-1)
        'top_p': 0.95,            # Nucleus sampling
        'top_k': 40,              # Top-k sampling
        'max_output_tokens': 2048, # Maximum response length
    }
)

# Generate content
response = model.generate_content('Your prompt here')
print(response.text)
```

### API Limits (Free Tier)

| Feature | Limit |
|---------|-------|
| **Requests per minute** | 60 RPM |
| **Requests per day** | 1,500 RPD |
| **Tokens per minute** | 1,000,000 TPM |
| **Max output tokens** | 8,192 tokens |

### Error Handling

```python
import google.generativeai as genai
from google.api_core import exceptions

try:
    response = model.generate_content(prompt)
    code = response.text
except exceptions.ResourceExhausted:
    st.error("API quota exceeded. Please try again later.")
except exceptions.InvalidArgument:
    st.error("Invalid request. Please check your prompt.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
```

---

## 🚢 Deployment

### Deploy to Streamlit Cloud (Recommended)

#### Step 1: Prepare Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Ready for deployment"
git push origin main
```

#### Step 2: Streamlit Cloud Setup

1. Visit [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Choose branch: `main`
6. Main file path: `app.py`
7. Click "Deploy"

#### Step 3: Configure Secrets

In Streamlit Cloud dashboard:
1. Go to app settings (⚙️)
2. Click "Secrets"
3. Add your secrets:
```toml
GEMINI_API_KEY = "your_api_key_here"
```
4. Save and restart app

### Alternative Deployment Options

#### Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port $PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

#### AWS EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install dependencies
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# Run app
streamlit run app.py --server.port 80
```

---

## 🔮 Future Enhancements

### Short-term Goals
- [ ] Add support for more programming languages (Rust, Kotlin, Scala)
- [ ] Implement code versioning and history
- [ ] Add collaborative features (share generated code)
- [ ] Integrate code execution environment (sandbox)
- [ ] Add dark/light theme toggle
- [ ] Implement user authentication and saved sessions
- [ ] Add export to GitHub Gist functionality

### Long-term Vision
- [ ] Multi-file project generation (complete applications)
- [ ] Integration with popular IDEs (VS Code extension)
- [ ] Code review and improvement suggestions
- [ ] Repository analysis and documentation generation
- [ ] Real-time collaboration features
- [ ] Custom model fine-tuning for specific domains
- [ ] Mobile application (iOS/Android)
- [ ] API endpoint for programmatic access
- [ ] Enterprise features (team workspaces, analytics)

### Model Improvements
- [ ] Support for Claude, GPT-4, and other LLMs
- [ ] Model comparison feature
- [ ] Custom prompt templates
- [ ] Fine-tuned models for specific languages/frameworks

---

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork the Project**
   ```bash
   # Click 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Ai-Code-Generator.git
   cd Ai-Code-Generator
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

4. **Make Changes**
   - Add your features or bug fixes
   - Follow code style guidelines
   - Add comments and documentation
   - Write tests if applicable

5. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add: Amazing new feature description"
   ```

6. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open Pull Request**
   - Go to original repository on GitHub
   - Click "New Pull Request"
   - Describe your changes in detail
   - Wait for review and feedback

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear, descriptive commit messages
- Add docstrings to all functions and classes
- Update README.md for new features
- Test your changes thoroughly
- Be respectful and constructive in discussions

### Areas for Contribution

- 🐛 **Bug Fixes**: Help identify and fix issues
- ✨ **New Features**: Implement requested features
- 📝 **Documentation**: Improve README and code docs
- 🎨 **UI/UX**: Enhance interface design
- ⚡ **Performance**: Optimize code efficiency
- 🧪 **Testing**: Add unit and integration tests
- 🌐 **Localization**: Add multi-language support

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ⚠️ No liability
- ⚠️ No warranty

---

## 📞 Contact

**Shiv Singh**

- 💼 GitHub: [@ShivSingh-17](https://github.com/ShivSingh-17)
- 📧 Email: [Add your email]
- 💼 LinkedIn: [https://www.linkedin.com/in/shiv-prakash-singh-624091267/]
- 🌐 Portfolio: []

**Project Links:**
- Repository: [https://github.com/ShivSingh-17/Ai-Code-Generator](https://github.com/ShivSingh-17/Ai-Code-Generator)
- Live Demo: [https://ai-code-generator-shiv.streamlit.app](https://ai-code-generator-shiv.streamlit.app)
- Issues: [Report Bug or Request Feature](https://github.com/ShivSingh-17/Ai-Code-Generator/issues)

---

## 🙏 Acknowledgments

- **Google Gemini Team**: For providing powerful AI capabilities through Gemini API
- **Streamlit**: For the amazing framework that makes building ML apps easy
- **Open Source Community**: For continuous inspiration and support
- **Contributors**: Everyone who has contributed to making this project better

### References & Resources
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Best Practices](https://peps.python.org/pep-0008/)
- [Code Generation with LLMs Research](https://arxiv.org/abs/2406.19544)

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/ShivSingh-17/Ai-Code-Generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/ShivSingh-17/Ai-Code-Generator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/ShivSingh-17/Ai-Code-Generator?style=social)
![GitHub issues](https://img.shields.io/github/issues/ShivSingh-17/Ai-Code-Generator)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ShivSingh-17/Ai-Code-Generator)

---

## 🌟 Star This Repository

If you found this project helpful or interesting, please consider giving it a ⭐ on GitHub! It helps others discover the project and motivates continued development.

---

<div align="center">

**Made with ❤️ and AI**

*Transforming ideas into code, one prompt at a time* 💻✨

**[⬆ Back to Top](#ai-code-generator-)**

</div>

---

## 📝 Citation

If you use this project in your research, work, or blog posts, please cite:

```bibtex
@misc{ai_code_generator,
  author = {Shiv Singh},
  title = {AI Code Generator: Natural Language to Code with Gemini AI},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/ShivSingh-17/Ai-Code-Generator}
}
```

---

## 🔗 Related Projects

- [GitHub Copilot](https://github.com/features/copilot) - AI pair programmer
- [TabNine](https://www.tabnine.com/) - AI code completion
- [Cursor AI](https://cursor.sh/) - AI-powered code editor
- [Replit Ghostwriter](https://replit.com/ai) - AI coding assistant
- [Qodo](https://www.qodo.ai/) - AI code intelligence

---

## 📚 Additional Resources

### Tutorials
- [Building AI Apps with Streamlit](https://docs.streamlit.io/knowledge-base/tutorials)
- [Google Gemini API Guide](https://ai.google.dev/tutorials)
- [LLM Prompt Engineering](https://www.promptingguide.ai/)

### Datasets & Models
- [HumanEval Benchmark](https://github.com/openai/human-eval)
- [CodeParrot Dataset](https://huggingface.co/codeparrot)
- [The Stack Dataset](https://huggingface.co/datasets/bigcode/the-stack)

### Community
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [r/StreamlitOfficial](https://www.reddit.com/r/StreamlitOfficial/)
- [AI Code Generation Discord](https://discord.gg/ai-code-gen)

---

*Last Updated: October 2025*

**Version: 1.0.0**
