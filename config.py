import os
from dotenv import load_dotenv

load_dotenv()

NYT_API_KEY=os.getenv("NYT_API_KEY")

if not NYT_API_KEY:
    raise ValueError("NYT_API_KEY is missing. Add it inside your .env file")

else:
    print("sucessful")