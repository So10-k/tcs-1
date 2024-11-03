import tkinter as tk
import random

# Constants
GRID_SIZE = 10
CELL_SIZE = 50
PLAYER_COLOR = "blue"
ENEMY_COLOR = "red"
ITEM_COLOR = "green"

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple RPG Game")
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        
        self.player_pos = [0, 0]
        self.enemies = []
        self.items = []
        
        self.create_grid()
        self.create_player()
        self.spawn_enemies(5)
        self.spawn_items(5)
        
        self.root.bind("<KeyPress>", self.on_key_press)
    
    def create_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE, (i + 1) * CELL_SIZE, (j + 1) * CELL_SIZE, outline="gray")
    
    def create_player(self):
        x, y = self.player_pos
        self.player = self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=PLAYER_COLOR)
    
    def spawn_enemies(self, count):
        for _ in range(count):
            while True:
                x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
                if [x, y] != self.player_pos and [x, y] not in self.enemies:
                    self.enemies.append([x, y])
                    self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=ENEMY_COLOR)
                    break
    
    def spawn_items(self, count):
        for _ in range(count):
            while True:
                x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
                if [x, y] != self.player_pos and [x, y] not in self.enemies and [x, y] not in self.items:
                    self.items.append([x, y])
                    self.canvas.create_oval(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=ITEM_COLOR)
                    break
    
    def on_key_press(self, event):
        x, y = self.player_pos
        if event.keysym == "Up" and y > 0:
            y -= 1
        elif event.keysym == "Down" and y < GRID_SIZE - 1:
            y += 1
        elif event.keysym == "Left" and x > 0:
            x -= 1
        elif event.keysym == "Right" and x < GRID_SIZE - 1:
            x += 1
        
        self.player_pos = [x, y]
        self.canvas.coords(self.player, x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE)
        
        self.check_collisions()
    
    def check_collisions(self):
        if self.player_pos in self.enemies:
            messagebox.showinfo("Game Over", "You encountered an enemy!")
            self.root.destroy()
        elif self.player_pos in self.items:
            self.items.remove(self.player_pos)
            messagebox.showinfo("Item Collected", "You collected an item!")
            if not self.items:
                messagebox.showinfo("Victory", "You collected all items!")
                self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()