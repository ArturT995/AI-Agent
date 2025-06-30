import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("No input detected, ask something")
        exit(1)
    
    args = sys.argv[1:]
    user_prompt = " ".join(args)
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]), ]
    

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
    )


    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count:}")

#prevents code from being executed when its being imported as a module

if __name__ == "__main__":
    main()