# 🎮 Conway's Game of Life

A mesmerizing cellular automaton where simple rules create infinite complexity.

---

## ✨ What is Conway's Game of Life?

Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway. It's a **zero-player game** that evolves based on its initial state, requiring no further input. Despite incredibly simple rules, it generates fascinating and complex patterns that emerge over generations.

---

## 📋 The Rules (Elegantly Simple)

Every cell follows these four rules:

| Condition | Result |
|-----------|--------|
| 🟢 Alive cell with **2-3 neighbors** | **Survives** ✅ |
| 🟢 Alive cell with **<2 or >3 neighbors** | **Dies** ❌ |
| ⚫ Dead cell with **exactly 3 neighbors** | **Born** 🌟 |

That's it! Despite this simplicity, complex and fascinating patterns emerge over generations.

---

## 🚀 Quick Start

### Option 1: Try It Online (Easiest!)

**No installation needed!** Everything runs in your browser.

👉 **[Play Now](https://conwaygameoflife.streamlit.app/)**

Just click the link and start playing!

### Option 2: Run Locally

**Requirements:**
- Python 3.8+
- Streamlit

**Setup:**

```bash
# Clone the repository
git clone https://github.com/yourusername/conway-game-of-life.git
cd conway-game-of-life

# Install dependencies
pip install streamlit

# Run the app
streamlit run app.py

# Open in your browser
http://localhost:8501
```

---

## 📖 How to Use

### 1. Start the Application
Open the app (online or locally)

### 2. Configure Your Simulation

| Setting | Range | Default |
|---------|-------|---------|
| **Rows** | 1-50 | 5 |
| **Columns** | 1-50 | 5 |
| **Generations** | 1-100 | 10 |

### 3. Watch It Evolve!
Click **"▶ Execute Simulation"** and watch the generations unfold.

### Example Run

**Input:**
- Rows: 5
- Columns: 5
- Generations: 3

**Output:**
```
Generation 0:
# # . . #
# # # . .
. # . . #
. # . . .
# . . . .

Generation 1:
# . # . .
. . # # .
. . . . .
. # # . .
# # . . .

Generation 2:
. . # . .
# . # . .
. # . . .
. # # . .
. . . . .

Generation 3:
. . . . .
. . # . .
# . # . .
. . # . .
. . . . .
```

---

## 🎓 What You'll Learn

- **Python**: Classes, loops, list comprehension, algorithms
- **Cellular Automata**: How simple rules create complex behavior
- **Biology**: Self-organizing systems and emergence
- **Philosophy**: Complexity arising from simplicity
- **Web Development**: Build interactive web apps with Streamlit

---

## 📚 Resources

- [Conway's Game of Life on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cellular Automata Theory](https://en.wikipedia.org/wiki/Cellular_automaton)

---

## 💡 Tips for Exploration

- Start with small grids to see patterns clearly
- Try different initial configurations
- Some patterns are stable (still lifes), some oscillate (blinkers), and some travel (gliders)
- Experiment and discover emergent behavior!

---

<div align="center">

**Enjoy watching life emerge from simple rules!** 🌱✨

</div>
