import getpass
import os
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

# Store API key temporarily during runtime;
os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

# Initialize model
model = ChatGroq(model="llama-3.3-70b-versatile")

# Define schema using Pydantic
class Review(BaseModel):
    summary: str = Field(description="Short summary of the review")
    sentiment: str = Field(description="Overall sentiment")

# Enable structured output
structured_model = model.with_structured_output(Review)

# Invoke a simple review;
result = structured_model.invoke("""
The OnePlus 15 is a top-tier Android flagship offering, highlighted by exceptional battery life that exceeds many competitors,
lightning-fast performance, and a sleek design. It directly challenges Samsung and Google’s best with a balanced mix of
cutting-edge specs and AI features, all while maintaining a more competitive price point.
""")

print(result.summary)
