import streamlit as st
import random

# Title and description
st.title("12 Times Table Challenge 🏆")
st.write("Test your multiplication skills with the 12 times table!")

# Initialize session state variables
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.replays = 5  # Default value
    st.session_state.difficulty = 1  # Default difficulty
    st.session_state.multiplier = None
    st.session_state.correct_answer = None
    st.session_state.show_next_question = False

# Start quiz setup
if not st.session_state.quiz_started:
    # User input for number of questions
    st.session_state.replays = st.number_input("How many times do you want to play?", min_value=1, max_value=100, step=1)

    # Difficulty selection
    difficulty = st.radio(
        "Select Difficulty Level:",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Easy (1-5)", 2: "Medium (5-10)", 3: "Hard (11-20)"}[x]
    )
    st.session_state.difficulty = difficulty
    difficulty_ranges = {1: (1, 5), 2: (5, 10), 3: (11, 20)}
    st.session_state.min_val, st.session_state.max_val = difficulty_ranges[difficulty]

    # Start button
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.multiplier = random.randint(st.session_state.min_val, st.session_state.max_val)
        st.session_state.correct_answer = 12 * st.session_state.multiplier
        st.session_state.show_next_question = False
        st.rerun()

# Quiz in progress
if st.session_state.quiz_started:
    if st.session_state.question_index < st.session_state.replays:
        st.subheader(f"Question {st.session_state.question_index + 1} of {st.session_state.replays}")
        st.write(f"What is **12 × {st.session_state.multiplier}?**")

        # User input for answer
        user_answer = st.number_input("Your answer:", min_value=0, step=1, key=st.session_state.question_index)

        # Submit button
        if st.button("Submit Answer"):
            if user_answer == st.session_state.correct_answer:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. The correct answer was {st.session_state.correct_answer}.")

            # Move to next question
            st.session_state.question_index += 1

            # Generate next question if quiz is not finished
            if st.session_state.question_index < st.session_state.replays:
                st.session_state.multiplier = random.randint(st.session_state.min_val, st.session_state.max_val)
                st.session_state.correct_answer = 12 * st.session_state.multiplier

            # Show "Next Question" button
            st.session_state.show_next_question = True

    # Show final score at the end
    if st.session_state.question_index >= st.session_state.replays:
        st.subheader(f"🎉 Quiz Completed! You scored **{st.session_state.score}** out of **{st.session_state.replays}**.")
        st.session_state.quiz_started = False  # Reset quiz after completion

# "Next Question" button to manually continue
if st.session_state.show_next_question and st.button("Next Question"):
    st.session_state.show_next_question = False