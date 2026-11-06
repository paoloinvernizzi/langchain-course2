from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()

def main():
    print(os.getenv("OPENAI_API_KEY"))
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

if __name__ == "__main__":
    main()