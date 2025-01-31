# 🕹️ Tic-Tac-Toe GUI (Python + Docker)

A simple **Tic-Tac-Toe** game with a **Tkinter GUI**, built using Python and Docker. The game allows two players to play against each other.

## ✨ Features
- ✅ Interactive **Tkinter GUI**  
- ✅ **Sound effects** using `pygame`  
- ✅ Fully **Dockerized** with **CI/CD pipeline** using GitHub Actions  
- ✅ Automated **unit tests** with `unittest`  

---

## 🖥️ Run Natively (Without Docker)
Make sure you have **Python 3.9+** installed.

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/pariaighanian/RAP_Final_Project.git
cd RAP_Final_Project
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the game:
```bash
python main.py
```

📌 **For Windows users:** If using **WSL2**, ensure you have **VcXsrv/Xming** running to display the GUI.

---

## 🐳 Run with Docker
You can also run the game inside a **Docker container**.

### 1️⃣ Pull the Docker image:
```bash
docker pull pariaighanian/tictactoe_gui:latest
```

### 2️⃣ Run the container:
```bash
docker run -it --rm -e DISPLAY=$DISPLAY --network="host" --name gui_container pariaighanian/tictactoe_gui
```

🚀 The **GUI will appear** on your screen.

---

## ✅ Run Tests
To run the unit tests:
```bash
python -m unittest discover tests
```

