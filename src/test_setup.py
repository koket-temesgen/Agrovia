from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")

print("✅ Setup successful!")

if groq_key:
    print("✅ GROQ API key loaded")
else:
    print("❌ GROQ API key missing")

if pinecone_key:
    print("✅ Pinecone API key loaded")
else:
    print("❌ Pinecone API key missing")

print("Environment ready for Agrovia AI 🌱")