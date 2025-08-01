# OpenAI Chat Completion Client

A simple guide to using the `OpenAIChatCompletionClient` from AutoGen for OpenAI and compatible models.

## Installation

```bash
pip install "autogen-ext[openai]" python-dotenv
```

## Quick Start

```python
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Basic usage
client = OpenAIChatCompletionClient(model="gpt-4o")
messages = [UserMessage(content="Hello!", source="user")]
result = await client.create(messages)
print(result.content)
```

## Configuration Examples

### OpenAI Models

```python
from dotenv import load_dotenv
import os

load_dotenv()

# Basic configuration
client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")  # Loaded from .env file
)

# Advanced configuration
client = OpenAIChatCompletionClient(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=1000,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    seed=42,
    timeout=30.0,
    max_retries=3
)
```

### Google Gemini

```python
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

model_client = OpenAIChatCompletionClient(
    model="gemini-2.0-flash-exp",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=google_api_key,
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": "unknown",
        "structured_output": False
    }
)
```

### Ollama (Local)

```python
# For non-OpenAI models (e.g., using with Ollama)
client = OpenAIChatCompletionClient(
    model="llama2",
    base_url="http://localhost:11434/v1",
    api_key="placeholder",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "family": "unknown",
        "structured_output": False
    }
)
```

## Key Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | str | Model name (required) |
| `api_key` | str | API key (uses env var if not provided) |
| `base_url` | str | Custom endpoint URL |
| `temperature` | float | Randomness (0.0-2.0) |
| `max_tokens` | int | Maximum tokens to generate |
| `model_info` | dict | Model capabilities (required for non-OpenAI) |
| `timeout` | float | Request timeout in seconds |
| `max_retries` | int | Number of retry attempts |

## Advanced Usage

### Streaming

```python
stream = client.create_stream(messages=messages)
async for chunk in stream:
    if isinstance(chunk, str):
        print(chunk, end="", flush=True)
```

### Structured Output

```python
from pydantic import BaseModel

class Response(BaseModel):
    answer: str
    confidence: float

result = await client.create(messages, json_output=Response)
```

### With Tools

```python
from autogen_core.tools import FunctionTool

def get_weather(city: str) -> str:
    return f"Weather in {city}: sunny, 72°F"

tool = FunctionTool(get_weather)
result = await client.create(messages, tools=[tool])
```

## Provider Setup

Create a `.env` file in your project root:

```env
# .env file
OPENAI_API_KEY=sk-your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
```

Then load it in your Python code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
```

### Ollama
Start Ollama server locally:
```bash
ollama serve
```

## Error Handling

```python
try:
    result = await client.create(messages)
    print(result.content)
except Exception as e:
    print(f"Error: {e}")
finally:
    await client.close()
```

## Documentation

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [GitHub Repository](https://github.com/microsoft/autogen)