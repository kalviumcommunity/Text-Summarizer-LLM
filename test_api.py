import os
import google.generativeai as gen
from dotenv import load_dotenv

load_dotenv()
gen.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = gen.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Hi")
print(response)