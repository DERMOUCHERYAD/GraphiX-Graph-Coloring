# GraphiX
GraphiX is a graph coloring application that allows you to visualize and solve the graph coloring problem using propositional logic.

You have already downloaded the `ProjetColorationINF402.zip` file and extracted it on your machine. You can now open this project in PyCharm or Visual Studio.

## Environment Setup:
1. Make sure you have Python 3 installed on your system.
   If not, you can download it from:

   ### Windows:
   - **64-bit:** [Download Python 3.12.3 64-bit](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)
   - **32-bit:** [Download Python 3.12.3 32-bit](https://www.python.org/ftp/python/3.12.3/python-3.12.3.exe)

   Follow the installer steps. Ensure that the "Add to PATH environment variable" option is checked.
   ##### Note: Python 3.12.3 cannot be used on Windows 7 or earlier versions.

   ### Linux:
   On most Linux distributions, Python is usually pre-installed.
   In a terminal:
   ```bash
   sudo apt install python3
   ```
   You can refer to this page for using Python on Unix platforms: [Python on Unix](https://docs.python.org/3/using/unix.html).

   ### MacOS:
   [Download Python 3.12.3 for MacOS](https://www.python.org/downloads/release/python-3123/)

## Usage:
2. You can use the code from this project in two ways.

   ### Non-Interactive Usage:
   In a terminal:
   - Navigate to the correct path: `./ProjetColorationINF402/ProjetColorationINF402/`
   - **For Linux:**
     ```bash
     python3 interface.py
     ```
   - **For Windows/MacOS:**
     ```bash
     python interface.py
     ```

   ### Using an IDE:
   You can work with an IDE to make it easier to manage and produce code. You can choose your preferred IDE.
   For example:
   - **Pycharm:**
     - **Windows:** [Download PyCharm for Windows](https://www.jetbrains.com/pycharm/download/?section=windows)
     - **Linux:** [Download PyCharm for Linux](https://www.jetbrains.com/pycharm/download/?section=linux)
     - **MacOS:** [Download PyCharm for MacOS](https://www.jetbrains.com/pycharm/download/?section=macos)
   
   - **Visual Studio Code:**
     - **Windows:** [Download VS Code for Windows](https://code.visualstudio.com/docs/?dv=win64user)
     - **Linux:** [Download VS Code for Linux](https://code.visualstudio.com/docs/?dv=linux64_deb)
     - **MacOS:** [Download VS Code for MacOS](https://code.visualstudio.com/docs/setup/mac)

   ### Configuration:
   To link PyCharm with Python, please watch this video:
   - [In French](https://www.youtube.com/watch?v=lMRKY3wjcrE)
   - [In English](https://www.youtube.com/watch?v=sLcLE0zJWuA)

## Execution and Compilation:
1. Launch PyCharm.
   On the welcome screen, select "Open."
   Navigate to the location where you extracted the `.zip` file of your project.
   Select the root folder of the project `ProjetColorationINF402` and click "OK."

2. Once your project is open, PyCharm will prompt you to install the necessary dependencies. Follow the instructions to install them.

3. Then, go to "File" > "Settings" > "Project: [ProjetColorationINF402]" > "Python Interpreter," and look for the libraries `tkinter`, `draw`, `PIL`, `math`, `pysat`, `python-sat`, `matplotlib`, `networkx`, and install them.
   If your Python interpreter is not already configured, click on the gear icon and select "Add" to add a new Python interpreter.
   Choose the Python interpreter that you previously downloaded and installed on your machine.

   For VS Code:
   Open the terminal to install the required libraries:
   ```bash
   pip install tkinter
   pip install math
   pip install matplotlib
   pip install networkx
   pip install pysat
   ```
   Choose "Open," then "Open Folder," and select the folder `ProjetColorationINF402`.
   For the SAT solver, we used `Glucose3` from `pysat.solvers`.

4. Open the `interface.py` file in the file explorer of PyCharm or VS Code.
5. Right-click on the `interface.py` file and select "Run," or use the associated button at the top-right to launch the application.

## Using GraphiX:
1. Click "Start" to begin the game.
2. You can create your own graph and choose the number of colors you want, or select a graph from 8 choices and the number of colors you wish to use.
3. You can always go back or completely exit the application.
