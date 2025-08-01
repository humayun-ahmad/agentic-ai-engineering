import google.generativeai as genai
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure the API key
genai.configure(api_key=google_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# Define the weather function
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is: "

# Simple assistant function
async def assistant_chat(task: str):
    # Check if the task is about weather
    if "weather" in task.lower():
        # Extract city (simple parsing)
        if "new york" in task.lower():
            weather_info = await get_weather("New York")
            response = model.generate_content(
                f"The user asked: {task}\n"
                f"Weather information: {weather_info}\n"
                f"Please provide a helpful response in details."
            )
            print(response.text)
    else:
        response = model.generate_content(task)
        print(response.text)

# Run the assistant
async def main():
    await assistant_chat("What is the weather in New York?")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())