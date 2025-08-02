# 🍎 Fruit Catcher Game 🍎


## 🎮 **About the Game**

A **fun and addictive** Pygame-based game where players catch falling fruits while avoiding bombs. Features multiple levels with increasing difficulty, score tracking, and high score saving.

---

## ✨ **Features**

### 🍓 **Gameplay Elements**
- **Two challenging levels** with different mechanics
- **Level 1**: Catch specific fruits for bonus points
- **Level 2**: Faster gameplay with more dangerous bombs
- **Real-time score tracking** and timer
- **Persistent high score** saving

### 🎨 **Visual & Audio**
- Colorful graphics and animations
- Sound effects for different actions
- Interactive start and end screens

---

## ⚙️ **Requirements**

- Python 3.6+
- Pygame library

```bash
pip install pygame# Fruit-Catcher-Game
```



### 🕹️ **Controls**

| **Action**               | **Keyboard**       | **Mouse**          |
|--------------------------|--------------------|--------------------|
| Move Basket Left         | ← (Left Arrow) / A | -                  |
| Move Basket Right        | → (Right Arrow) / D| -                  |
| Start Game               | -                  | Click START button |
| Proceed to Next Level    | ENTER              | -                  |
| Quit Game                | ESC                | Click QUIT button  |

### 🍎 **Game Rules**

#### **Level 1: Target Practice**

+ Catch ONLY the highlighted fruit for 10 points
! Other fruits give 5 points
- Bombs deduct 5 points
⏱️ 60-second timer or reach 100 points to advance

#### **Level 2: Survival Mode**
+ All fruits give 10 points
- Bombs now deduct 10 points
⚡ Faster falling objects!
⏱️ 60-second timer or reach 150 points to win


## 🎮 Game Flow Steps

1. **START**  
   🚀 Click Start to begin and enter LEVEL 1.

2. **LEVEL 1**  
   🕹️ Play and earn points.  
   ➡️ Proceed if **Score ≥ 100** or **Time ≤ 0**.

3. **INTERLEVEL**  
   ✨ "Level 1 complete!"  
   ⏎ Press Enter to continue.

4. **LEVEL 2**  
   🎮 Play to reach **Score ≥ 150** or **Time ≤ 0**.

5. **END SCREEN**  
   👑 Show final score.  
   🔄 Restart or ❌ Quit options.



### 🎉 What's Implemented
✔️ Complete two-level gameplay with escalating difficulty  
✔️ Persistent high score system  
✔️ Responsive controls (keyboard + mouse)  
✔️ Visual and audio feedback system  
✔️ Proper state management and transitions  

### 🚧 Known Limitations
- Screen resolution fixed at 1000×650px
- Limited to 3 fruit types + bombs
- No pause functionality during gameplay

### 🔮 Future Enhancements
- "Power-ups (slow motion, score multipliers)"
- "Mobile touch controls"
- "Dynamic difficulty adjustment"
- "Online leaderboards"
- "Custom fruit skins"


## 🙏 Credits & Acknowledgements

**Development Team:**
- Pankaj Singh
- Aniruth Devaraj  
- V K James
- Shree Krishna

**Special Thanks To:**
- Pygame Community
- OpenGameArt.org contributors
- FreeSound.org artists
- SSN College of Engineering

<div align="center">
  <em>Made with ❤️ by Team Fruit Catcher</em>
</div>
