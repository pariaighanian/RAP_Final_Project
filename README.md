# 🕹️ Tic-Tac-Toe GUI (Python + Docker)

A simple **Tic-Tac-Toe** game with a **Tkinter GUI**, built using Python and Docker. The game allows two players to play against each other.

## ✨ Features
- ✅ Interactive **Tkinter GUI**  
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

### 2️⃣ Run the game:
```bash
python main.py
```

## 🐳 Run with Docker
You can also run the game inside a **Docker container**.
### 🔹 **For Linux Users**
```bash
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network=host \
    --name gui_container \
    pariaighanian/tictactoe_gui
```

### 📌 Explanation:
- Ensure you have an X server running (e.g., Xorg).
- Run ``` echo $DISPLAY ``` to confirm your DISPLAY variable is set.
- If running on WSL2, use **VcXsrv** or **Xming.**

### 🔹 **For Windows Users (Using WSL2)**
Windows users need to install **VcXsrv** or **Xming** to display the GUI.

#### **Step 1: Install and Configure VcXsrv**
1. Download and install **[VcXsrv](https://sourceforge.net/projects/vcxsrv/)**.
2. Run `XLaunch` and configure it as follows:
   - **Multiple Windows**
   - **Start no client**
   - **Disable Access Control**
   - Click **Finish**.
3. Set the **DISPLAY** variable in WSL:
```bash
export DISPLAY=$(grep nameserver /etc/resolv.conf | awk '{print $2}'):0.0
```

**Step 2: Run the Docker Container**
```bash
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --network=host \
    --name gui_container \
    pariaighanian/tictactoe_gui
```


🚀 The **GUI will appear** on your screen.

---

## ✅ Run Tests
To run the unit tests:
```bash
python -m unittest discover tests
```

