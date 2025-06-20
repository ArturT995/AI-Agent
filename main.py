import os
from google import genai
from dotenv import load_dotenv
import sys



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("No input detected, ask something")
        exit(1)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents = sys.argv[1]
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count:}")

#prevents code from being executed when its being imported as a module

if __name__ == "__main__":
    main()