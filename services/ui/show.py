import streamlit as st


def show():

    st.markdown(
        """
        <div style=" border: 10px dashed #444;padding:30px;">
            <h2 >👈Set your workout plan</h2>
            <br>
            <p >Choose your exercise, sets and reps in the sidebar,<br>
            then click <strong>Start Session</strong> to activate the camera and AI Coach.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )