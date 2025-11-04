# ConwayGameOfLife

What is Conway's Game of Life?
Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway. It's a zero-player game that evolves based on its initial state, requiring no further input.
The Rules (Extremely Simple)

Alive cell with 2-3 neighbors → Survives ✅
Alive cell with <2 or >3 neighbors → Dies ❌
Dead cell with exactly 3 neighbors → Born 🌟

That's it! Despite these simple rules, complex and fascinating patterns emerge over generations.

🌐 Try It Online
Run it now in the cloud (no installation needed):
https://conwaygameoflife.streamlit.app/
Just click the link and start playing! The simulation runs entirely in your browser.

🎯 What You Learn

Python: Classes, loops, list comprehension, algorithms
Cellular Automata: How simple rules create complex behavior
Biology: Self-organizing systems and emergence
Philosophy: Complexity from simplicity
Streamlit: Build interactive web apps with pure Python

 Installation
Option 1: Run Online (Easiest!)
Visit: https://conwaygameoflife.streamlit.app/
No installation required! Everything runs in your browser.

Option 2: Run Locally
Requirements

Python 3.8+
Streamlit
No other dependencies!

Setup

Clone the repository

bashgit clone https://github.com/yourusername/conway-game-of-life.git
cd conway-game-of-life

Install dependencies

bashpip install streamlit

Run the app

bashstreamlit run app.py

Open in browser

http://localhost:8501

📝 Usage
Using the Web App

Open the app (online or locally)
Enter grid size:

Rows: 1-50 (default: 5)
Columns: 1-50 (default: 5)


Enter number of generations: 1-100 (default: 10)
Click "▶ Execute Simulation"
Watch the generations evolve!

Example
Input:
- Rows: 5
- Columns: 5
- Generations: 3

Output:
Generación 0
# # . . #
# # # . .
. # . . #
. # . . .
# . . . .

Generación 1
# . # . .
. . # # .
. . . . .
. # # . .
# # . . .
