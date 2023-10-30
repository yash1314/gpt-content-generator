import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content(notes):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a paragraph based on the below information.\n\n{notes}\n\nDescription:",
            temperature=0.7,
            max_tokens=256
        )
        print(response)
        description = response['choices'][0]['text']
        return description
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title('Content Generator')
    notes = st.text_area('Enter your message here.')

    if st.button("Generate Content") and notes:
        with st.spinner('Processing...'):
            description = generate_content(notes)
            if description:
                st.write(description)

if __name__ == '__main__':
    main()
