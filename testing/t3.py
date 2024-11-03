import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Constants
GRID_SIZE = 10
CELL_SIZE = 50
PLAYER_COLOR = "blue"
ENEMY_COLOR = "red"
ITEM_COLOR = "green"
INVINCIBILITY_DURATION = 5000  # 5 seconds
ADMIN_PASSWORD = "admin123"
MOD_PASSWORD = "mod123"
OWNER_PASSWORD = "owner"

PERMISSION_OPTIONS = ["Add/Remove Enemies", "Add/Remove Items", "Move Player", "Reset Game", "Toggle Invincibility", "Run Code"]

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple RPG Game")
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.pack()
        
        self.player_pos = [0, 0]
        self.enemies = []
        self.items = []
        self.invincible = False
        self.key_sequence = []
        
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
        self.player = self.canvas.create_oval(x * CELL_SIZE + 15, y * CELL_SIZE + 5, x * CELL_SIZE + 35, y * CELL_SIZE + 25, fill=PLAYER_COLOR)  # Head
        self.player_body = self.canvas.create_rectangle(x * CELL_SIZE + 20, y * CELL_SIZE + 25, x * CELL_SIZE + 30, y * CELL_SIZE + 45, fill=PLAYER_COLOR)  # Body
    
    def update_player_position(self):
        x, y = self.player_pos
        self.canvas.coords(self.player, x * CELL_SIZE + 15, y * CELL_SIZE + 5, x * CELL_SIZE + 35, y * CELL_SIZE + 25)
        self.canvas.coords(self.player_body, x * CELL_SIZE + 20, y * CELL_SIZE + 25, x * CELL_SIZE + 30, y * CELL_SIZE + 45)
    
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
        self.update_player_position()
        self.check_collisions()

        # Handle invincibility key sequence
        self.key_sequence.append(event.keysym)
        if len(self.key_sequence) > 2:
            self.key_sequence.pop(0)
        
        if self.key_sequence == ["a", "p"]:
            self.activate_invincibility()
        
        # Handle admin panel key sequence
        if event.keysym == "F1":
            self.open_admin_panel()
    
    def activate_invincibility(self):
        self.invincible = True
        self.canvas.itemconfig(self.player, fill="yellow")
        self.canvas.itemconfig(self.player_body, fill="yellow")
        self.root.after(INVINCIBILITY_DURATION, self.deactivate_invincibility)
    
    def deactivate_invincibility(self):
        self.invincible = False
        self.canvas.itemconfig(self.player, fill=PLAYER_COLOR)
        self.canvas.itemconfig(self.player_body, fill=PLAYER_COLOR)
    
    def check_collisions(self):
        if self.player_pos in self.enemies and not self.invincible:
            messagebox.showinfo("Game Over", "You encountered an enemy!")
            self.root.destroy()
        elif self.player_pos in self.items:
            self.items.remove(self.player_pos)
            messagebox.showinfo("Item Collected", "You collected an item!")
            if not self.items:
                messagebox.showinfo("Victory", "You collected all items!")
                self.root.destroy()
    
    def open_admin_panel(self):
        password = simpledialog.askstring("Admin Panel", "Enter password:", show='*')
        if password == ADMIN_PASSWORD:
            self.create_admin_panel()
        elif password == MOD_PASSWORD:
            self.create_mod_panel()
        elif password == OWNER_PASSWORD:
            self.create_owner_panel()
        else:
            messagebox.showerror("Error", "Incorrect password!")
    
    def create_admin_panel(self):
        self.admin_panel = tk.Toplevel(self.root)
        self.admin_panel.title("Admin Panel")
        
        # Create frames for better layout
        enemy_frame = tk.LabelFrame(self.admin_panel, text="Enemies", padx=10, pady=10)
        enemy_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        item_frame = tk.LabelFrame(self.admin_panel, text="Items", padx=10, pady=10)
        item_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        player_frame = tk.LabelFrame(self.admin_panel, text="Player", padx=10, pady=10)
        player_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        game_frame = tk.LabelFrame(self.admin_panel, text="Game Controls", padx=10, pady=10)
        game_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        # Enemy controls
        add_enemy_button = tk.Button(enemy_frame, text="Add Enemy", command=self.add_enemy)
        add_enemy_button.pack(pady=5)
        
        remove_enemy_button = tk.Button(enemy_frame, text="Remove Enemy", command=self.remove_enemy)
        remove_enemy_button.pack(pady=5)
        
        # Item controls
        add_item_button = tk.Button(item_frame, text="Add Item", command=self.add_item)
        add_item_button.pack(pady=5)
        
        remove_item_button = tk.Button(item_frame, text="Remove Item", command=self.remove_item)
        remove_item_button.pack(pady=5)
        
        # Player controls
        move_player_button = tk.Button(player_frame, text="Move Player", command=self.move_player)
        move_player_button.pack(pady=5)
        
        # Game controls
        reset_game_button = tk.Button(game_frame, text="Reset Game", command=self.reset_game)
        reset_game_button.pack(pady=5)
        
        toggle_invincibility_button = tk.Button(game_frame, text="Toggle Invincibility", command=self.toggle_invincibility)
        toggle_invincibility_button.pack(pady=5)
    
    def create_mod_panel(self):
        self.mod_panel = tk.Toplevel(self.root)
        self.mod_panel.title("Mod Panel")
        
        # Create frames for better layout
        enemy_frame = tk.LabelFrame(self.mod_panel, text="Enemies", padx=10, pady=10)
        enemy_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        item_frame = tk.LabelFrame(self.mod_panel, text="Items", padx=10, pady=10)
        item_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        # Enemy controls
        add_enemy_button = tk.Button(enemy_frame, text="Add Enemy", command=self.add_enemy)
        add_enemy_button.pack(pady=5)
        
        remove_enemy_button = tk.Button(enemy_frame, text="Remove Enemy", command=self.remove_enemy)
        remove_enemy_button.pack(pady=5)
        
        # Item controls
        add_item_button = tk.Button(item_frame, text="Add Item", command=self.add_item)
        add_item_button.pack(pady=5)
        
        remove_item_button = tk.Button(item_frame, text="Remove Item", command=self.remove_item)
        remove_item_button.pack(pady=5)
    
    def create_owner_panel(self):
        self.owner_panel = tk.Toplevel(self.root)
        self.owner_panel.title("Owner Panel")
        
        # Create frames for better layout
        password_frame = tk.LabelFrame(self.owner_panel, text="Password Management", padx=10, pady=10)
        password_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        permission_frame = tk.LabelFrame(self.owner_panel, text="Permissions Management", padx=10, pady=10)
        permission_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        code_frame = tk.LabelFrame(self.owner_panel, text="Run Code", padx=10, pady=10)
        code_frame.pack(padx=10, pady=5, fill="both", expand="yes")
        
        # Password management controls
        set_admin_password_button = tk.Button(password_frame, text="Set Admin Password", command=self.set_admin_password)
        set_admin_password_button.pack(pady=5)
        
        set_mod_password_button = tk.Button(password_frame, text="Set Mod Password", command=self.set_mod_password)
        set_mod_password_button.pack(pady=5)
        
        # Permissions management controls
        self.admin_permissions = tk.StringVar(value=PERMISSION_OPTIONS[0])
        self.mod_permissions = tk.StringVar(value=PERMISSION_OPTIONS[0])
        
        tk.Label(permission_frame, text="Admin Permissions:").pack(pady=5)
        tk.OptionMenu(permission_frame, self.admin_permissions, *PERMISSION_OPTIONS).pack(pady=5)
        
        tk.Label(permission_frame, text="Mod Permissions:").pack(pady=5)
        tk.OptionMenu(permission_frame, self.mod_permissions, *PERMISSION_OPTIONS).pack(pady=5)
        
        set_permissions_button = tk.Button(permission_frame, text="Set Permissions", command=self.set_permissions)
        set_permissions_button.pack(pady=5)
        
        # Run code controls
        self.code_entry = tk.Text(code_frame, height=10)
        self.code_entry.pack(pady=5)
        
        run_code_button = tk.Button(code_frame, text="Run Code", command=self.run_code)
        run_code_button.pack(pady=5)
    
    def set_admin_password(self):
        global ADMIN_PASSWORD
        new_password = simpledialog.askstring("Set Admin Password", "Enter new admin password:", show='*')
        if new_password:
            ADMIN_PASSWORD = new_password
            messagebox.showinfo("Success", "Admin password updated!")
    
    def set_mod_password(self):
        global MOD_PASSWORD
        new_password = simpledialog.askstring("Set Mod Password", "Enter new mod password:", show='*')
        if new_password:
            MOD_PASSWORD = new_password
            messagebox.showinfo("Success", "Mod password updated!")
    
    def set_permissions(self):
        admin_perms = self.admin_permissions.get()
        mod_perms = self.mod_permissions.get()
        messagebox.showinfo("Success", f"Permissions updated!\nAdmin: {admin_perms}\nMod: {mod_perms}")
    
    def run_code(self):
        code = self.code_entry.get("1.0", tk.END)
        try:
            exec(code, globals())
            messagebox.showinfo("Success", "Code executed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing code: {e}")
    
    def add_enemy(self):
        self.spawn_enemies(1)
    
    def remove_enemy(self):
        if self.enemies:
            enemy_pos = self.enemies.pop()
            self.canvas.create_rectangle(enemy_pos[0] * CELL_SIZE, enemy_pos[1] * CELL_SIZE, (enemy_pos[0] + 1) * CELL_SIZE, (enemy_pos[1] + 1) * CELL_SIZE, fill="white", outline="gray")
    
    def add_item(self):
        self.spawn_items(1)
    
    def remove_item(self):
        if self.items:
            item_pos = self.items.pop()
            self.canvas.create_oval(item_pos[0] * CELL_SIZE, item_pos[1] * CELL_SIZE, (item_pos[0] + 1) * CELL_SIZE, (item_pos[1] + 1) * CELL_SIZE, fill="white", outline="gray")
    
    def move_player(self):
        x = simpledialog.askinteger("Move Player", "Enter X position (0-9):", minvalue=0, maxvalue=GRID_SIZE-1)
        y = simpledialog.askinteger("Move Player", "Enter Y position (0-9):", minvalue=0, maxvalue=GRID_SIZE-1)
        if x is not None and y is not None:
            self.player_pos = [x, y]
            self.update_player_position()
    
    def reset_game(self):
        self.canvas.delete("all")
        self.enemies.clear()
        self.items.clear()
        self.player_pos = [0, 0]
        self.create_grid()
        self.create_player()
        self.spawn_enemies(5)
        self.spawn_items(5)
    
    def toggle_invincibility(self):
        if self.invincible:
            self.deactivate_invincibility()
        else:
            self.activate_invincibility()

if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()