# Import necessary modules
import streamlit as st
import openai

# Set up Streamlit layout
def main():
    st.title("Find Indoor Tennis Courts Near Me")

    user_input = st.text_input("Enter your OpenAI API key:") 
    user_location = st.text_input("Enter your location:")

    if st.button("Find Tennis Courts"):

        # Setup openai API with user key
        openai.api_key = user_input

        # Structure message to API
        message = [{'role': 'system', 'content': 'You are a helpful assistant.'}, 
                   {'role': 'user', 'content': 'Find indoor tennis courts near {0}'.format(user_location)}]

        # Send message to API
        response = openai.chat.completions.create(model='gpt-4', messages=message)

        # Get Response
        message_content = response.choices[0].message.content.strip()

        # Print Response
        st.write(message_content)

if __name__ == "__main__":
    main()