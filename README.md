# 🦖 PyDinoRun

A Python implementation of the classic **Chrome Dino Run** game, built with [Pygame](https://www.pygame.org/).  
This project is designed for **learning purposes** — ideal for students, hobbyists, or anyone interested in 2D game development with Python.

---

## 📸 Demo

Screenshots from gameplay:

![Demo 1](./demo/Screenshot%202025-08-16%20at%2015.57.20.png)  
![Demo 2](./demo/Screenshot%202025-08-16%20at%2015.58.33.png)  
![Demo 3](./demo/Screenshot%202025-08-16%20at%2016.00.47.png)  

---

## 🚀 Features

- Control a pixel dinosaur 🦖 that jumps or ducks to avoid obstacles.  
- Obstacles: **cacti 🌵** and **birds 🐦**.  
- Day/night cycle ☀️🌙 with smooth transitions.  
- Clouds drifting in the background.  
- Scrolling ground effect.  
- Score tracking with custom pixel-style number font.  
- Clean and modular codebase (each game object in a separate Python file).

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vantu03/PyDinoRun.git
cd PyDinoRun
````

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate the environment:

* **macOS/Linux**

  ```bash
  source venv/bin/activate
  ```
* **Windows**

  ```bash
  venv\Scripts\activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, simply install Pygame:
>
> ```bash
> pip install pygame
> ```

---

## ▶️ Run the Game

Start the game by running:

```bash
python main.py
```

---

## 🎮 Controls

* **SPACE** or **↑ (Arrow Up)** → Jump
* **↓ (Arrow Down)** → Duck
* **ESC** → Quit game

---

## 📂 Project Structure

```
PyDinoRun/
│── demo/                 # Screenshots and demo images
│── main.py               # Entry point of the game
│── game.py               # Game loop and state management
│── game_object.py        # Base class for all game objects
│── dino.py               # Player character (the dinosaur)
│── bird.py               # Bird obstacle
│── cactus_small.py       # Cactus obstacle
│── cloud.py              # Cloud objects for background
│── ground.py             # Scrolling ground surface
│── number_font.py        # Custom font for score rendering
│── ...
```

---

## 🎯 Purpose

This project was created **for educational purposes**:

* Demonstrates how to structure a Pygame project.
* Useful for **course assignments, reports, or programming practice**.
* Can serve as a foundation for more advanced 2D games.

---

## 📜 License

Released under the **MIT License**.
Free to use, modify, and distribute for **non-commercial / educational** purposes.

---

## 🙌 Acknowledgements

* Inspired by Google Chrome’s offline **Dino Run** game.
* Built using [Pygame](https://www.pygame.org/).
