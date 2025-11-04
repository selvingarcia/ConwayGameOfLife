import streamlit as st
import time
import numpy as np
import ConwayGameOfLife  # your logic file

game = ConwayGameOfLife.ConwayGameOfLife()

# --- Sidebar input ---
st.sidebar.title("Conway's Game of Life Settings")
rows = st.sidebar.number_input("Number of rows:", min_value=5, max_value=50, value=10)
cols = st.sidebar.number_input("Number of columns:", min_value=5, max_value=50, value=10)
loops = st.sidebar.number_input("Number of loops:", min_value=1, max_value=200, value=20)

# --- Button to start ---
if st.sidebar.button("Start Simulation"):
    grid = game.create_grid(rows, cols)

    placeholder = st.empty()
    for _ in range(loops):
        placeholder.text(game.format_grid(grid))
        grid = game.update_grid(grid)
        time.sleep(0.2)
