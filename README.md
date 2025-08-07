# 🤖 Agentic AI Engineering

This repository is dedicated to exploring and developing agentic AI systems that exhibit autonomous decision-making capabilities. Here, you will find resources including algorithms, frameworks, and example projects aimed at fostering the development of intelligent agents capable of adapting and functioning in dynamic environments.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [AutoGen Studio Setup](#autogen-studio-setup)
- [Gemini Model Configuration](#gemini-model-configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini models
- Git

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/agentic-ai-engineering.git
cd agentic-ai-engineering
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 AutoGen Studio Setup

### Version Information
- **AutoGen Studio Version**: `v0.4.2.2`

### Starting AutoGen Studio
Run the following command to start AutoGen Studio on a custom port:

```bash
autogenstudio ui --port 8081 --appdir ./dir
```

This will:
- Launch AutoGen Studio on port `8081`
- Use `./dir` as the application directory for storing configurations and data

## ⚙️ Gemini Model Configuration

To use Google's Gemini models with AutoGen Studio, create a model configuration with the following JSON:

### Configuration File
Create a file named `gemini_model_config.json`:

```json
{
  "provider": "autogen_ext.models.openai.OpenAIChatCompletionClient",
  "component_type": "model",
  "version": 1,
  "component_version": 1,
  "description": "Gemini model for AutoGen",
  "label": "Gemini Model",
  "config": {
    "model": "gemini-1.5-flash",
    "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
    "api_key": "YOUR_FULL_API_KEY_HERE",
    "temperature": 0.7,
    "max_tokens": 8192,
    "model_info": {
      "vision": "True",
      "function_calling": "True",
      "json_output": "True",
      "family": "gemini",
      "structured_output": "True"
    }
  }
}
```

### Configuration Steps

1. **Obtain Google API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Generate an API key
   - Replace `YOUR_FULL_API_KEY_HERE` with your actual API key

2. **Import Configuration**:
   - Open AutoGen Studio UI
   - Navigate to Gallery → Models
   - Click "Edit Component" or "New Model"
   - Paste the JSON configuration
   - Save changes

3. **Available Models**:
   - `gemini-1.5-flash` - Faster, cost-effective model
   - `gemini-1.5-pro` - More capable, advanced model

## 📚 Dependencies

### Core Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| `autogenstudio` | 0.4.2 | AutoGen Studio for multi-agent orchestration |
| `autogen-agentchat` | ~0.2 | Agent chat capabilities with LLM support |
| `autogen-core` | Latest | Core AutoGen framework |
| `autogen-ext` | Latest | AutoGen extensions |
| `ag2[gemini]` | Latest | AG2 with Gemini support |

### AI/ML Frameworks

| Package | Description |
|---------|-------------|
| `langgraph` | Graph-based agent workflows |
| `langchain` | Framework for LLM applications |
| `langchain_openai` | OpenAI integration for LangChain |
| `langchain_google_genai` | Google Generative AI integration |
| `google-generativeai` | Google's Generative AI Python SDK |

### Additional Tools

| Package | Description |
|---------|-------------|
| `streamlit` | Web app framework for ML projects |
| `arxiv` | Access to arXiv papers |
| `ollama` | Local LLM support |
| `openai` | OpenAI API client |
| `tiktoken` | Token counting for OpenAI models |
| `ipykernel` | Jupyter kernel support |
| `python-dotenv` | Environment variable management |

### Full Requirements File

```txt
langgraph
langchain
langchain_openai
python-dotenv
ipykernel
langchain_google_genai
autogen-agentchat
autogen-core
autogen-ext
asyncio
openai
tiktoken
autogenstudio==0.4.2
streamlit
arxiv
autogen-agentchat[llm,gemini]~=0.2
google-generativeai
ollama
autogen-ext[ollama]
autogen
ag2[gemini]
```

## 🛠️ Troubleshooting

### Common Issues

1. **Model Configuration Error**: "model_info is required when model name is not a valid OpenAI model"
   - **Solution**: Ensure the `model_info` fields are correctly set in the configuration JSON

2. **API Key Issues**
   - **Solution**: Verify your Google API key is valid and has the necessary permissions

3. **Port Already in Use**
   - **Solution**: Change the port number in the startup command or kill the process using the port

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions and support, please open an issue in the GitHub repository.

---

**Note**: Remember to never commit your API keys to version control. Use environment variables or `.env` files (added to `.gitignore`) for sensitive information.