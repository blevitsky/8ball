import streamlit as st
import random
import time

# Initialize session state if needed
if 'name_submitted' not in st.session_state:
    st.session_state.name_submitted = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Custom CSS for fade effects
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    
    /* Fade-out effect */
    @keyframes fadeOut {
        from {opacity: 1;}
        to {opacity: 0;}
    }
    
    /* Fade-in effect */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    
    .fade-out {
        animation: fadeOut 1s forwards;
    }
    
    .fade-in {
        animation: fadeIn 1.5s forwards;
    }
    
    /* Additional styling for 8Ball appearance */
    .magic-ball {
        width: 200px;
        height: 200px;
        background: radial-gradient(circle at 65% 15%, white 1px, #3a3a3a 3%, black 60%, #3a3a3a 100%);
        border-radius: 50%;
        color: white;
        text-align: center;
        margin: 30px auto;
        padding-top: 80px;
        font-size: 22px;
        box-shadow: 0 0 20px 5px #a855f7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to handle name submission


def submit_name():
    st.session_state.username = st.session_state.name_input
    st.session_state.name_submitted = True


# Main app logic
if not st.session_state.name_submitted:
    # First screen - name input
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("Digital 8Ball")
    st.write("Ask away! The 8Ball will answer your question.")

    st.text_input("Your name:", key="name_input")
    st.button("Submit", on_click=submit_name)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Second screen - 8Ball answer
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title(f"Welcome, {st.session_state.username}!")

    question = st.text_input("What would you like to ask the 8Ball?")

    if st.button("Shake the 8Ball"):
        with st.spinner("The 8Ball is thinking..."):
            time.sleep(1.5)  # Create suspense

        answer = random.choice(responses)
        st.markdown(
            f'<div class="magic-ball">{answer}</div>', unsafe_allow_html=True)

    # Add reset button
    if st.button("Start Over"):
        st.session_state.name_submitted = False
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
