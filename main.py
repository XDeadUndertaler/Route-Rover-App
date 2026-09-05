import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import bcrypt


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    # Verify a password against the hashed value
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Replace with your MySQL username
        password="1234",     # Replace with your MySQL password
        database="RouteRover"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Function to hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Insert a sample user (if needed)
sample_username = 'test'
sample_password = '123'

# Check if user already exists
cursor.execute("SELECT * FROM users WHERE username = %s", (sample_username,))
if not cursor.fetchone():
    hashed = hash_password(sample_password).decode('utf-8')
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (sample_username, hashed))
    conn.commit()
    print("Sample user created.")
else:
    print("Sample user already exists.")

cursor.close()
conn.close()



# Database connection parameters
DB_HOST = "localhost"
DB_USER = "root"        # Replace with your MySQL username
DB_PASSWORD = "1234"    # Replace with your MySQL password
DB_NAME = "RouteRover"

# Function to hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Function to verify password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Connect to the MySQL database
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="RouteRover"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error connecting to database: {err}")
        return None

# Fetch cities from the database
def fetch_cities(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT city FROM tourist_locations ORDER BY city")
        cities = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return cities
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching cities: {err}")
        return []

# Fetch trip locations based on start and end cities
def get_trip_locations(conn, start_city, end_city):
    try:
        cursor = conn.cursor()
        query = """
            SELECT * FROM tourist_locations
            WHERE city IN (%s, %s)
            ORDER BY FIELD(city, %s, %s)
        """
        cursor.execute(query, (start_city, end_city, start_city, end_city))
        trip_locations = cursor.fetchall()
        cursor.close()
        return trip_locations
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching trip locations: {err}")
        return []

# Main Application Class
class RouteRoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RouteRover - Your Road Trip Planner")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#f0f0f0")  # Light grey background

        # Initialize frames
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.register_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")

        # Show login frame initially
        self.show_login()

    # Function to show login frame
    def show_login(self):
        self.register_frame.pack_forget()
        self.main_frame.pack_forget()
        self.login_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        # Clear previous widgets
        for widget in self.login_frame.winfo_children():
            widget.destroy()

        # Title
        title_label = tk.Label(self.login_frame, text="RouteRover - Login", font=("Helvetica", 32, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Username
        username_label = tk.Label(self.login_frame, text="Username:", font=("Helvetica", 18), bg="#f0f0f0")
        username_label.pack(pady=10)
        self.login_username_var = tk.StringVar()
        username_entry = tk.Entry(self.login_frame, textvariable=self.login_username_var, font=("Helvetica", 16))
        username_entry.pack(pady=5)

        # Password
        password_label = tk.Label(self.login_frame, text="Password:", font=("Helvetica", 18), bg="#f0f0f0")
        password_label.pack(pady=10)
        self.login_password_var = tk.StringVar()
        password_entry = tk.Entry(self.login_frame, textvariable=self.login_password_var, font=("Helvetica", 16), show="*")
        password_entry.pack(pady=5)

        # Login Button
        login_button = tk.Button(self.login_frame, text="Login", font=("Helvetica", 18), bg="#4CAF50", fg="white", command=self.login)
        login_button.pack(pady=20)

        # Register Button
        register_button = tk.Button(self.login_frame, text="Register", font=("Helvetica", 14), bg="#2196F3", fg="white", command=self.show_register)
        register_button.pack(pady=10)

    # Function to show registration frame
    def show_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        # Clear previous widgets
        for widget in self.register_frame.winfo_children():
            widget.destroy()

        # Title
        title_label = tk.Label(self.register_frame, text="RouteRover - Register", font=("Helvetica", 32, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Username
        username_label = tk.Label(self.register_frame, text="Username:", font=("Helvetica", 18), bg="#f0f0f0")
        username_label.pack(pady=10)
        self.register_username_var = tk.StringVar()
        username_entry = tk.Entry(self.register_frame, textvariable=self.register_username_var, font=("Helvetica", 16))
        username_entry.pack(pady=5)

        # Password
        password_label = tk.Label(self.register_frame, text="Password:", font=("Helvetica", 18), bg="#f0f0f0")
        password_label.pack(pady=10)
        self.register_password_var = tk.StringVar()
        password_entry = tk.Entry(self.register_frame, textvariable=self.register_password_var, font=("Helvetica", 16), show="*")
        password_entry.pack(pady=5)

        # Confirm Password
        confirm_label = tk.Label(self.register_frame, text="Confirm Password:", font=("Helvetica", 18), bg="#f0f0f0")
        confirm_label.pack(pady=10)
        self.register_confirm_var = tk.StringVar()
        confirm_entry = tk.Entry(self.register_frame, textvariable=self.register_confirm_var, font=("Helvetica", 16), show="*")
        confirm_entry.pack(pady=5)

        # Register Button
        register_button = tk.Button(self.register_frame, text="Register", font=("Helvetica", 18), bg="#4CAF50", fg="white", command=self.register)
        register_button.pack(pady=20)

        # Back to Login Button
        back_button = tk.Button(self.register_frame, text="Back to Login", font=("Helvetica", 14), bg="#2196F3", fg="white", command=self.show_login)
        back_button.pack(pady=10)

    # Function to show main trip planner frame
    def show_main(self, username):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        
        # Clear previous widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Welcome Label
        welcome_label = tk.Label(self.main_frame, text=f"Welcome, {username}!", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Starting City
        start_city_label = tk.Label(self.main_frame, text="Starting City:", font=("Helvetica", 18), bg="#f0f0f0")
        start_city_label.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)

        self.start_city_var = tk.StringVar()
        start_city_dropdown = ttk.Combobox(self.main_frame, textvariable=self.start_city_var, state="readonly", font=("Helvetica", 16))
        start_city_dropdown['values'] = fetch_cities(self.conn)
        start_city_dropdown.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        # Ending City
        end_city_label = tk.Label(self.main_frame, text="Ending City:", font=("Helvetica", 18), bg="#f0f0f0")
        end_city_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        self.end_city_var = tk.StringVar()
        end_city_dropdown = ttk.Combobox(self.main_frame, textvariable=self.end_city_var, state="readonly", font=("Helvetica", 16))
        end_city_dropdown['values'] = fetch_cities(self.conn)
        end_city_dropdown.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        # Number of Days
        num_days_label = tk.Label(self.main_frame, text="Number of Days:", font=("Helvetica", 18), bg="#f0f0f0")
        num_days_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        self.num_days_var = tk.StringVar()
        num_days_entry = tk.Entry(self.main_frame, textvariable=self.num_days_var, font=("Helvetica", 16))
        num_days_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        # Plan Trip Button
        plan_button = tk.Button(self.main_frame, text="Plan Trip", font=("Helvetica", 18), bg="#4CAF50", fg="white", command=self.plan_trip)
        plan_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Itinerary Output
        itinerary_label = tk.Label(self.main_frame, text="Itinerary:", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        itinerary_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.itinerary_text = tk.Text(self.main_frame, wrap=tk.WORD, font=("Helvetica", 16), bg="#ffffff", height=20)
        self.itinerary_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        # Make the text widget expandable
        self.main_frame.grid_rowconfigure(6, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Logout Button
        logout_button = tk.Button(self.main_frame, text="Logout", font=("Helvetica", 14), bg="#f44336", fg="white", command=self.logout)
        logout_button.grid(row=7, column=0, columnspan=2, pady=10)

    # Login Function
    def login(self):
        username = self.login_username_var.get().strip()
        password = self.login_password_var.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        conn = get_db_connection()
        if not conn:
            return

        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            stored_hash = result[0]
            if verify_password(password, stored_hash):
                self.conn = get_db_connection()
                self.show_main(username)
            else:
                messagebox.showerror("Login Failed", "Incorrect password.")
        else:
            messagebox.showerror("Login Failed", "Username not found.")

    # Register Function
    def register(self):
        username = self.register_username_var.get().strip()
        password = self.register_password_var.get().strip()
        confirm_password = self.register_confirm_var.get().strip()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            messagebox.showwarning("Input Error", "Passwords do not match.")
            return

        conn = get_db_connection()
        if not conn:
            return

        cursor = conn.cursor()
        try:
            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Registration Failed", "Username already exists.")
                cursor.close()
                conn.close()
                return

            # Hash the password
            hashed = hash_password(password).decode('utf-8')

            # Insert the new user
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed))
            conn.commit()
            messagebox.showinfo("Registration Successful", "You have successfully registered.")
            self.show_login()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error during registration: {err}")
        finally:
            cursor.close()
            conn.close()

    # Function to plan the trip
    def plan_trip(self):
        start_city = self.start_city_var.get()
        end_city = self.end_city_var.get()
        num_days = self.num_days_var.get()

        if not start_city or not end_city or not num_days:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            num_days = int(num_days)
            if num_days <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Number of days must be a positive integer.")
            return

        if start_city == end_city:
            messagebox.showwarning("Input Error", "Starting and ending cities must be different.")
            return

        trip_locations = get_trip_locations(self.conn, start_city, end_city)

        if not trip_locations:
            self.itinerary_text.delete(1.0, tk.END)
            self.itinerary_text.insert(tk.END, f"No tourist locations found between {start_city} and {end_city}.")
            return

        days_per_location = max(1, num_days // len(trip_locations))
        itinerary = "Trip Itinerary:\n\n"

        for index, location in enumerate(trip_locations):
            day_start = index * days_per_location + 1
            day_end = (index + 1) * days_per_location
            itinerary += f"Day {day_start} to Day {day_end}:\n"
            itinerary += f"Location: {location[1]} ({location[3]}, {location[2]})\n"
            itinerary += f"Description: {location[4]}\n"
            itinerary += f"Coordinates: {location[5]}, {location[6]}\n\n"

        self.itinerary_text.delete(1.0, tk.END)
        self.itinerary_text.insert(tk.END, itinerary)

    # Logout Function
    def logout(self):
        self.main_frame.pack_forget()
        self.conn.close()
        self.show_login()

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = RouteRoverApp(root)
    root.mainloop()