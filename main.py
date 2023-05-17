import streamlit as st

from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
import app
from barfi import __init__

def main():
    # Spawn a new Ace editor
    content = st_ace()

    # Display editor's content as you type
    content
    _RELEASE = True
    app.app()


if __name__ == "__main__":
    main()