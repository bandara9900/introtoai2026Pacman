# Pacman AI Search Project

Welcome to the **Pacman Search Project** for Ascencia University, by Professor Fajouri.

This project is based on the fundamentals of AI search algorithms like:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

## 🚀 Objective
Students must implement these algorithms in `search.py`, and test them using `searchAgents.py` within different maze layouts like `tinyMaze` or `mediumMaze`.

##  Folder Structure
- `search.py` — Where you implement your search algorithms.
- `searchAgents.py` — Agents that use your algorithms.
- `layouts/` — Mazes for Pacman to solve.
- `pacman.py` — Main driver to launch the game.
- `test_cases/q1/` — Sample tests for early-stage evaluation.

## 📝 Instructions
1. Clone this repository.
2. Implement each search strategy in `search.py`.
3. Run: `python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs` (replace `bfs` with other methods)
4. Submit your GitHub link with working implementation.

## 🔥 Notes
- Designed exclusively for academic use at Ascencia University.

Enjoy coding and good luck!

— Professor Fajouri

---

## 🧪 Student Implementation & Testing

**Student Name:** Akash Bandara  
 

**Successfully Implemented Algorithms:**
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search (A-Star)

### How to Test the Algorithms:
Open your terminal, navigate to the project directory, and run the following commands:

**Depth-First Search (DFS):**
`python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs`

**Breadth-First Search (BFS):**
`python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

**Uniform Cost Search (UCS):**
`python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`

**A* Search (A-Star):**
`python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`