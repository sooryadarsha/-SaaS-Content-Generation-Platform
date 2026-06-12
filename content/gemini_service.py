import google.generativeai as genai

genai.configure(
    api_key="GEMINI_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_ai_content(prompt):

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return "⚠ AI limit reached. Please try again later."
    
    return response.text
'''import google.generativeai as genai

genai.configure(api_key="YOUR_KEY")

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

response = model.generate_content("hello")
print(response.text)'''