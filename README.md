# Rocket-Target-Challenge-with-pygame
 
### Description:  
In *Rocket Target Challenge*, you take control of a spaceship on the left side of the screen. Your goal is to shoot and hit a moving rectangle that shifts up and down on the right side. With each successful hit, the rectangle moves faster, increasing the challenge. If you miss and the bullet doesn’t hit the target, the game restarts. It’s a test of precision, control, and reflexes that becomes more difficult with every hit.  

---

### Game Structure:  

#### **1. Gameplay**:
- **Objective**:  
  Control the spaceship to fire bullets at the moving rectangle. Each hit increases the rectangle’s speed.  

- **Restart Conditions**:  
  If a bullet misses the rectangle, the game restarts.  

- **Controls**:  
  - **Move Up/Down**: Use the arrow keys.  
  - **Shoot**: Press the space bar to fire bullets from the spaceship.  

---

#### **2. Technical Structure of the Project**:

1. **`settings3.py`**:  
   - Contains the game’s general settings, such as screen size, colors, initial speeds for the rectangle and spaceship, and bullet speed.  

2. **`rocket3.py`**:  
   - Defines the spaceship: its initial position, how it moves up and down, and how it fires bullets.  

3. **`bullets3.py`**:  
   - Manages the bullets fired by the spaceship, including their creation, movement, and collision detection with the moving rectangle.  

4. **`clases.py`**:  
   - Implements the game’s main classes, such as the moving rectangle and other core logic.  

5. **`funciones3.py`**:  
   - Contains utility functions such as:
     - Handling keyboard events.  
     - Checking for collisions between bullets and the rectangle.  
     - Restarting the game when a bullet misses.  

6. **`stats.py`**:  
   - Tracks statistics like the number of successful hits and the rectangle’s current speed.  

7. **`boton.py`** (optional):  
   - If the game includes buttons (e.g., a main menu or manual restart), this file defines their appearance and functionality.  

8. **`ejecutable3.py`**:  
   - The main file that runs the game and organizes interactions between the modules.  

---

### Game Flow:  

1. **Start**:  
   The spaceship starts on the left side of the screen, while the moving rectangle shifts up and down on the right.  

2. **Gameplay**:  
   - The player controls the spaceship to align it vertically with the rectangle.  
   - Fires a bullet attempting to hit the moving rectangle.  

3. **Successful Hit**:  
   - If the bullet hits the rectangle, the rectangle increases its speed, becoming harder to hit.  

4. **Miss**:  
   - If the bullet misses the rectangle, the game restarts, and the rectangle returns to its initial speed.  

5. **Infinite Progression**:  
   - The goal is to see how many consecutive hits the player can achieve before missing.  

---

### Ideas for Future Improvements:
- **Score System**: Display a counter on the screen for consecutive hits.  
- **Progressive Difficulty**: Also increase the spaceship’s speed or add obstacles as the rectangle speeds up.  
- **Sound Effects**: Add sounds for shooting, hitting, or missing.  
- **Lives System**: Give the player 3 lives before fully restarting.  

---
**Installation Guide**  

1. **Clone the Repository**  
   Open your terminal and run the following command to clone the repository:  
   ```bash
   git clone https://github.com/SebasKHE/Rocket-League-based-2d-game-with-Pygame.git
   ```

2. **Navigate to the Project Directory**  
   Move into the project folder:  
   ```bash
   cd Rocket-League-based-2d-game-with-Pygame
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**  
   Create and activate a virtual environment to manage dependencies:  
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Linux/Mac
   venv\Scripts\activate          # On Windows
   ```

4. **Install Dependencies**  
   Install the required Python packages listed in `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` does not exist, manually install Pygame:  
   ```bash
   pip install pygame
   ```

5. **Run the Game**  
   Execute the main file to start the game. Depending on the project, run the executable script:  
   ```bash
   python ejecutable3.py
   ```

6. **Enjoy the Game!**  
   Use the spaceship controls to aim, shoot, and hit the moving target.  

If you encounter any issues, ensure Python and Pygame are correctly installed and that you are using Python 3.7 or higher.
