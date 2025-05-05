import tkinter as tk
from tkinter import messagebox, ttk
from db import Database
from datetime import datetime
from PIL import Image, ImageTk  # Add this import at the top


class AuctionAppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auction Management System")

        # Set initial size
        self.root.geometry("1000x720")  # Set initial size
        self.root.minsize(1000, 720)  # Set minimum size
        self.root.resizable(True, True)  # Allow window resizing

        # Add styling configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configure colors and fonts
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'accent': '#3498db',
            'success': '#2ecc71',
            'warning': '#f1c40f',
            'error': '#e74c3c',
            'white': '#ffffff',
            'light_gray': '#f5f6fa',  # Use a very light gray for the login container
        }

        self.fonts = {
            'header': ('Helvetica', 24, 'bold'),
            'subheader': ('Helvetica', 18, 'bold'),
            'body': ('Helvetica', 12),
            'button': ('Helvetica', 12, 'bold')
        }

        # Load only background image
        try:
            bg_img = Image.open(r'F:\auction\images\reg_bg.png')
            self.bg_image = ImageTk.PhotoImage(bg_img)
        except Exception as e:
            print(f"Warning: Unable to load background image. Error: {e}")
            self.bg_image = None

        # Configure custom button style with rounded corners
        self.style.configure('Rounded.TButton',
                             font=self.fonts['button'],
                             background=self.colors['accent'],
                             foreground=self.colors['white'],
                             borderwidth=0,
                             relief='flat',
                             padding=(20, 10))

        self.style.map('Rounded.TButton',
                       background=[('active', self.colors['secondary'])],
                       foreground=[('active', self.colors['white'])])

        # Update button styling
        self.style.configure('Login.TButton',
                             font=self.fonts['button'],
                             background=self.colors['accent'],
                             foreground=self.colors['white'],
                             padding=(20, 10))

        self.style.map('Login.TButton',
                       background=[('active', self.colors['secondary'])],
                       foreground=[('active', self.colors['white'])])

        # Configure ttk styles
        self.style.configure('Header.TLabel',
                             font=self.fonts['header'],
                             background=self.colors['primary'],
                             foreground=self.colors['white'])

        self.style.configure('Custom.TButton',
                             font=self.fonts['button'],
                             background=self.colors['accent'],
                             foreground=self.colors['white'])

        self.style.configure('Custom.TEntry',
                             fieldbackground=self.colors['light_gray'],
                             borderwidth=2)

        self.style.configure('Custom.Treeview',
                             background=self.colors['white'],
                             fieldbackground=self.colors['white'],
                             font=self.fonts['body'])

        self.style.configure('Custom.Treeview.Heading',
                             font=self.fonts['subheader'])

        self.style.map('Custom.TButton',
                       background=[('active', self.colors['secondary'])],
                       foreground=[('active', self.colors['white'])]
                       )

        # Add these style configurations
        self.style.configure('UserManagement.TFrame',
                             background=self.colors['white'])
        self.style.configure(
            'Controls.TFrame', background=self.colors['white'])

        # For ttk.Frame backgrounds
        self.style.configure('TFrame', background=self.colors['white'])

        # Add these new style configurations
        self.style.configure('Custom.TFrame',
                             background=self.colors['white'])

        self.style.configure('Custom.TLabel',
                             background=self.colors['white'],
                             foreground=self.colors['primary'])

        self.style.configure('Info.TLabel',
                             background=self.colors['white'],
                             foreground=self.colors['secondary'],
                             font=self.fonts['body'])

        self.style.configure('Header.TLabel',
                             background=self.colors['primary'],
                             foreground=self.colors['white'],
                             font=self.fonts['header'])

        self.style.configure('Title.TLabel',
                             background=self.colors['white'],
                             foreground=self.colors['primary'],
                             font=self.fonts['subheader'])

        # Style for Buttons
        self.style.configure('Action.TButton',
                             font=self.fonts['button'],
                             background=self.colors['accent'],
                             foreground=self.colors['white'])

        self.style.map('Action.TButton',
                       background=[('active', self.colors['secondary'])],
                       foreground=[('active', self.colors['white'])])

        # Style for Tabs
        self.style.configure('Custom.TNotebook',
                             background=self.colors['white'],
                             borderwidth=0)

        self.style.configure('Custom.TNotebook.Tab',
                             background=self.colors['light_gray'],
                             padding=(10, 5),
                             font=self.fonts['body'])

        # Configure main window
        self.root.configure(bg=self.colors['primary'])

        self.db = Database()

        self.current_user_id = None
        self.current_admin_id = None
        self.is_admin = False

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        self.show_login_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Configure main frame with plain background
        self.main_frame.configure(
            bg=self.colors['white'],
            padx=20,
            pady=20
        )

    def show_login_screen(self):
        self.clear_frame()

        # Create a container for background
        bg_container = tk.Frame(self.main_frame)
        bg_container.place(relx=0.5, rely=0.5,
                           anchor='center', width=800, height=600)

        # Set background image if available
        if self.bg_image:
            # Resize background image to fit container
            try:
                bg_img = Image.open('f:/auction/images/background.jpg')
                bg_img = bg_img.resize((800, 600), Image.Resampling.LANCZOS)
                self.bg_image = ImageTk.PhotoImage(bg_img)
                bg_label = tk.Label(bg_container, image=self.bg_image)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            except Exception as e:
                print(
                    f"Warning: Unable to resize background image. Error: {e}")

        # Create login container with light background
        login_container = tk.Frame(
            bg_container,
            # Use light gray instead of semi-transparent
            bg=self.colors['light_gray'],
            padx=40,
            pady=20,
            relief='solid',
            borderwidth=1
        )
        login_container.place(relx=0.5, rely=0.5, anchor='center')

        # Update the color for elements inside login container
        login_bg = self.colors['light_gray']  # Use this for consistency

        # Title frame
        title_frame = tk.Frame(login_container, bg=login_bg)
        title_frame.pack(pady=(0, 30))

        # Shadow effect for title
        shadow_label = tk.Label(
            title_frame,
            text="Auction System",
            font=self.fonts['header'],
            bg=login_bg,
            fg='gray'
        )
        shadow_label.place(x=2, y=2)

        # Main title
        tk.Label(
            title_frame,
            text="Auction System",
            font=self.fonts['header'],
            bg=login_bg,
            fg=self.colors['primary']
        ).pack()

        # Update all frame backgrounds in the login container
        username_frame = tk.Frame(login_container, bg=login_bg)
        username_frame.pack(fill='x', pady=10)

        tk.Label(
            username_frame,
            text="Username",
            font=self.fonts['body'],
            bg=login_bg,
            fg=self.colors['primary']
        ).pack(anchor='w')

        self.login_username_entry = ttk.Entry(
            username_frame,
            style='Custom.TEntry',
            width=30,
            font=self.fonts['body']
        )
        self.login_username_entry.pack(fill='x', pady=(5, 0))

        # Password field with custom style
        password_frame = tk.Frame(login_container, bg=login_bg)
        password_frame.pack(fill='x', pady=10)

        tk.Label(
            password_frame,
            text="Password",
            font=self.fonts['body'],
            bg=login_bg,
            fg=self.colors['primary']
        ).pack(anchor='w')

        self.login_password_entry = ttk.Entry(
            password_frame,
            style='Custom.TEntry',
            show="•",
            width=30,
            font=self.fonts['body']
        )
        self.login_password_entry.pack(fill='x', pady=(5, 0))

        # Buttons frame
        button_frame = tk.Frame(login_container, bg=login_bg)
        button_frame.pack(pady=20)

        # Regular styled buttons
        ttk.Button(
            button_frame,
            text="Login as User",
            style='Login.TButton',
            command=self.login_user,
            width=25  # Make buttons wider
        ).pack(pady=5)

        ttk.Button(
            button_frame,
            text="Login as Admin",
            style='Login.TButton',
            command=self.login_admin,
            width=25
        ).pack(pady=5)

        ttk.Button(
            button_frame,
            text="Register",
            style='Login.TButton',
            command=self.show_register_screen,
            width=25
        ).pack(pady=5)

    def show_register_screen(self):
        self.clear_frame()

        # Create a container for the background
        bg_container = tk.Frame(self.main_frame)
        bg_container.place(relx=0.5, rely=0.5,
                           anchor='center', width=800, height=600)

        # Set background image if available
        try:
            bg_img = Image.open(r'f:/auction/images/reg_bg.png')
            bg_img = bg_img.resize((800, 600), Image.Resampling.LANCZOS)
            self.register_bg_image = ImageTk.PhotoImage(bg_img)
            bg_label = tk.Label(bg_container, image=self.register_bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Warning: Unable to load background image. Error: {e}")
            # Use a plain background color as a fallback
            bg_container.configure(bg=self.colors['light_gray'])

        # Create a container for the registration form
        form_container = tk.Frame(
            bg_container,
            # Use a light gray background for the form
            bg=self.colors['light_gray'],
            padx=40,
            pady=20,
            relief='solid',
            borderwidth=1
        )
        form_container.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        tk.Label(
            form_container,
            text="Register User",
            font=self.fonts['header'],
            bg=self.colors['light_gray'],
            fg=self.colors['primary']
        ).pack(pady=10)

        # Form fields
        fields = [
            ("Username", "reg_username_entry"),
            ("Password", "reg_password_entry"),
            ("Email", "reg_email_entry"),
            ("First Name", "reg_first_name_entry"),
            ("Last Name", "reg_last_name_entry"),
            ("Phone Number", "reg_phone_entry"),
            ("Address", "reg_address_entry")
        ]

        for label_text, field_name in fields:
            tk.Label(
                form_container,
                text=label_text,
                font=self.fonts['body'],
                bg=self.colors['light_gray'],
                fg=self.colors['primary']
            ).pack(anchor='w', pady=(5, 0))

            setattr(self, field_name, tk.Entry(form_container))
            getattr(self, field_name).pack(fill='x', pady=(0, 10))

        # Register button
        tk.Button(
            form_container,
            text="Register",
            font=self.fonts['button'],
            bg=self.colors['accent'],
            fg=self.colors['white'],
            command=self.register_user
        ).pack(pady=10)

        # Back to Login button
        tk.Button(
            form_container,
            text="Back to Login",
            font=self.fonts['button'],
            bg=self.colors['secondary'],
            fg=self.colors['white'],
            command=self.show_login_screen
        ).pack()

    # Login as user
    def login_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        user_id = self.db.verify_user(username, password)
        if user_id:
            self.current_user_id = user_id
            self.is_admin = False
            messagebox.showinfo("Success", f"User '{username}' logged in.")
            self.show_user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # Login as admin
    def login_admin(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        admin_id = self.db.verify_admin(username, password)
        if admin_id:
            self.current_admin_id = admin_id
            self.is_admin = True
            messagebox.showinfo("Success", f"Admin '{username}' logged in.")
            self.show_admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid admin username or password")

    def register_user(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        email = self.reg_email_entry.get()
        first_name = self.reg_first_name_entry.get()
        last_name = self.reg_last_name_entry.get()
        phone = self.reg_phone_entry.get()
        address = self.reg_address_entry.get()

        if not (username and password and email):
            messagebox.showerror(
                "Error", "Username, password, and email are required.")
            return

        success = self.db.add_user(
            username, password, email, first_name, last_name, phone, address)
        if success:
            messagebox.showinfo(
                "Success", "Registration successful. Please login.")
            self.show_login_screen()
        else:
            messagebox.showerror(
                "Error", "Failed to register user. Username or email may already exist.")

    def logout(self):
        self.current_user_id = None
        self.current_admin_id = None
        self.is_admin = False
        self.show_login_screen()

    # --- Admin Dashboard ---

    def show_admin_dashboard(self):
        self.clear_frame()

        # Header with styling
        header_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        tk.Label(
            header_frame,
            text="Admin Dashboard",
            font=self.fonts['header'],
            bg=self.colors['primary'],
            fg=self.colors['white']
        ).pack(pady=10)

        # Tab control with styling
        tab_control = ttk.Notebook(self.main_frame)

        # Style the tabs
        self.style.configure(
            "TNotebook",
            background=self.colors['white'],
            borderwidth=0
        )
        self.style.configure(
            "TNotebook.Tab",
            background=self.colors['light_gray'],
            padding=[10, 5],
            font=self.fonts['body']
        )

        # User Management tab
        user_tab = ttk.Frame(tab_control)
        tab_control.add(user_tab, text='User Management')
        self.populate_user_management(user_tab)

        # Auction Management tab
        auction_tab = ttk.Frame(tab_control)
        tab_control.add(auction_tab, text='Auction Management')
        self.populate_auction_management(auction_tab)

        # Item Management tab
        item_tab = ttk.Frame(tab_control)
        tab_control.add(item_tab, text='Item Management')
        self.populate_item_management(item_tab)

        # Bids Management tab
        bids_tab = ttk.Frame(tab_control)
        tab_control.add(bids_tab, text='Bids Management')
        self.populate_bids_management(bids_tab)

        # Auction History tab
        history_tab = ttk.Frame(tab_control)
        tab_control.add(history_tab, text='Auction History')
        self.populate_auction_history(history_tab)

        # Auctioneer Management tab
        auctioneer_tab = ttk.Frame(tab_control)
        tab_control.add(auctioneer_tab, text='Auctioneer Management')
        self.populate_auctioneer_management(auctioneer_tab)

        # Payment Management tab
        payment_tab = ttk.Frame(tab_control)
        tab_control.add(payment_tab, text='Payment Management')
        self.populate_payment_management(payment_tab)

        tab_control.pack(expand=1, fill='both')

        # Styled logout button
        ttk.Button(
            self.main_frame,
            text="Logout",
            style='Custom.TButton',
            command=self.logout
        ).pack(pady=20)

        # Dark Mode Toggle Button
        ttk.Button(
            self.main_frame,
            text="Toggle Dark Mode",
            style='Custom.TButton',
            command=self.toggle_dark_mode
        ).pack(pady=10)

    def populate_user_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="User Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.user_tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Username", "Email", "First Name",
                     "Last Name", "Phone", "Address"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "ID": 50,
            "Username": 100,
            "Email": 150,
            "First Name": 100,
            "Last Name": 100,
            "Phone": 100,
            "Address": 200
        }

        for col in self.user_tree["columns"]:
            self.user_tree.heading(col, text=col)
            self.user_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.user_tree.yview)
        self.user_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.user_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Control buttons frame
        controls = ttk.Frame(
            content_frame, style='Custom.TFrame', padding=(20, 0))
        controls.pack(side='right', fill='y')

        # Add buttons with consistent styling
        buttons = [
            ("Add User", self.admin_add_user_window),
            ("Edit User", self.admin_edit_user_window),
            ("Delete User", self.admin_delete_user)
        ]

        for text, command in buttons:
            ttk.Button(
                controls,
                text=text,
                style='Action.TButton',
                command=command
            ).pack(pady=5)

        self.refresh_user_list()

    def refresh_user_list(self):
        for i in self.user_tree.get_children():
            self.user_tree.delete(i)
        users = self.db.get_all_users()
        for user in users:
            self.user_tree.insert('', 'end', values=(
                user['user_id'],
                user['username'],
                user['email'],
                user['first_name'],
                user['last_name'],
                user['phone_number'],
                user['address']
            ))

    def admin_add_user_window(self):
        win = tk.Toplevel(self.root)
        win.title("Add User")

        fields = ["Username", "Password", "Email", "First Name",
                  "Last Name", "Phone Number", "Address"]
        entries = {}

        for field in fields:
            tk.Label(win, text=field).pack()
            entry = tk.Entry(win)
            entry.pack()
            entries[field] = entry

        def on_add():
            vals = {field: ent.get() for field, ent in entries.items()}
            if not (vals["Username"] and vals["Password"] and vals["Email"]):
                messagebox.showerror(
                    "Error", "Username, Password and Email required")
                return
            success = self.db.add_user(vals["Username"], vals["Password"], vals["Email"],
                                       vals["First Name"], vals["Last Name"], vals["Phone Number"], vals["Address"])
            if success:
                messagebox.showinfo("Success", "User added")
                self.refresh_user_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add user")

        tk.Button(win, text="Add", command=on_add).pack()

    def admin_edit_user_window(self):
        selected = self.user_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a user to edit")
            return

        user_vals = self.user_tree.item(selected[0])['values']
        user_id = user_vals[0]

        # Create window with specific size
        win = tk.Toplevel(self.root)
        win.title("Edit User")
        win.geometry("400x600")  # Set window size
        win.minsize(400, 600)    # Set minimum size

        # Create main container with padding
        container = ttk.Frame(win, padding="20")
        container.pack(fill='both', expand=True)

        # Header
        tk.Label(
            container,
            text="Edit User",
            font=self.fonts['header'],
            fg=self.colors['primary']
        ).pack(pady=(0, 20))

        fields = ["Username", "Password", "Email", "First Name",
                  "Last Name", "Phone Number", "Address"]
        entries = {}

        # Create fields with better styling
        for i, field in enumerate(fields):
            field_frame = ttk.Frame(container)
            field_frame.pack(fill='x', pady=5)

            tk.Label(
                field_frame,
                text=field + ":",
                font=self.fonts['body'],
                fg=self.colors['primary']
            ).pack(anchor='w')

            entry = ttk.Entry(field_frame, style='Custom.TEntry', width=40)
            if field != "Password":  # Don't fill in password
                try:
                    entry.insert(0, user_vals[i] if i == 0 else user_vals[i+1])
                except IndexError:
                    # Insert empty string if no value exists
                    entry.insert(0, "")
            entry.pack(fill='x', pady=(0, 5))
            entries[field] = entry

        def on_update():
            vals = {field: ent.get() for field, ent in entries.items()}
            if not vals["Password"]:
                old_password = self.get_user_password(user_id)
                vals["Password"] = old_password if old_password else ""

            success = self.db.update_user(
                user_id,
                vals["Username"],
                vals["Password"],
                vals["Email"],
                vals["First Name"],
                vals["Last Name"],
                vals["Phone Number"],
                vals["Address"]
            )

            if success:
                messagebox.showinfo("Success", "User updated successfully")
                self.refresh_user_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update user")

        # Button frame
        button_frame = ttk.Frame(container)
        button_frame.pack(pady=20)

        # Update button with styling
        ttk.Button(
            button_frame,
            text="Update",
            style='Custom.TButton',
            command=on_update
        ).pack(side='left', padx=5)

        # Cancel button
        ttk.Button(
            button_frame,
            text="Cancel",
            style='Custom.TButton',
            command=win.destroy
        ).pack(side='left', padx=5)

        # Center the window
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry(f'+{x}+{y}')

    def get_user_password(self, user_id):
        if not self.db.connection or not self.db.connection.is_connected():
            self.db.connect()
        cursor = self.db.connection.cursor()
        try:
            query = "SELECT password FROM USER WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching password: {e}")
            return None
        finally:
            cursor.close()

    def admin_delete_user(self):
        selected = self.user_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a user to delete")
            return
        user_vals = self.user_tree.item(selected[0])['values']
        user_id = user_vals[0]

        confirm = messagebox.askyesno(
            "Confirm Delete", f"Delete user '{user_vals[1]}'?")
        if confirm:
            success = self.db.delete_user(user_id)
            if success:
                messagebox.showinfo("Success", "User deleted")
                self.refresh_user_list()
            else:
                messagebox.showerror("Error", "Failed to delete user")

    def populate_auction_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Auction Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.auction_tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Title", "Description", "Start Date", "End Date",
                     "Reserve Price", "Current Bid", "Auctioneer ID", "Status"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "ID": 50,
            "Title": 150,
            "Description": 200,
            "Start Date": 100,
            "End Date": 100,
            "Reserve Price": 100,
            "Current Bid": 100,
            "Auctioneer ID": 100,
            "Status": 100
        }

        for col in self.auction_tree["columns"]:
            self.auction_tree.heading(col, text=col)
            self.auction_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.auction_tree.yview)
        self.auction_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.auction_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Control buttons frame
        controls = ttk.Frame(
            content_frame, style='Custom.TFrame', padding=(20, 0))
        controls.pack(side='right', fill='y')

        # Add buttons with consistent styling
        buttons = [
            ("Add Auction", self.admin_add_auction_window),
            ("Edit Auction", self.admin_edit_auction_window),
            ("Delete Auction", self.admin_delete_auction)
        ]

        for text, command in buttons:
            ttk.Button(
                controls,
                text=text,
                style='Action.TButton',
                command=command
            ).pack(pady=5)

        # Display latest bidder details
        latest_bid = self.db.get_latest_bid()
        if latest_bid:
            ttk.Label(
                controls,
                text=f"Latest Bidder: {latest_bid['bidder_name']}",
                style='Info.TLabel'
            ).pack(pady=(20, 5))
            ttk.Label(
                controls,
                text=f"Bid Amount: ₹{latest_bid['bid_amount']}",
                style='Info.TLabel'
            ).pack(pady=5)
            ttk.Label(
                controls,
                text=f"Auction ID: {latest_bid['auction_id']}",
                style='Info.TLabel'
            ).pack(pady=5)

        self.refresh_auction_list()

    def refresh_auction_list(self):
        for i in self.auction_tree.get_children():
            self.auction_tree.delete(i)
        auctions = self.db.get_all_auctions()
        for auction in auctions:
            self.auction_tree.insert('', 'end', values=(
                auction['auction_id'],
                auction['title'],
                auction['description'],
                auction['start_date'],
                auction['end_date'],
                auction['reserve_price'],
                auction['current_bid'],
                auction['auctioneer_id'],
                auction['status']
            ))

    def admin_add_auction_window(self):
        win = tk.Toplevel(self.root)
        win.title("Add Auction")

        fields = ["Title", "Description",
                  "Start Date (YYYY-MM-DD)", "End Date (YYYY-MM-DD)", "Reserve Price", "Auctioneer ID", "Status"]
        entries = {}

        for field in fields:
            tk.Label(win, text=field).pack()
            entry = tk.Entry(win)
            entry.pack()
            entries[field] = entry

        def on_add():
            vals = {field: ent.get() for field, ent in entries.items()}
            if not (vals["Title"] and vals["Start Date (YYYY-MM-DD)"] and vals["End Date (YYYY-MM-DD)"] and vals["Reserve Price"] and vals["Auctioneer ID"]):
                messagebox.showerror(
                    "Error", "Please fill in all required fields")
                return
            try:
                datetime.strptime(vals["Start Date (YYYY-MM-DD)"], "%Y-%m-%d")
                datetime.strptime(vals["End Date (YYYY-MM-DD)"], "%Y-%m-%d")
                reserve_price = float(vals["Reserve Price"])
                auctioneer_id = int(vals["Auctioneer ID"])
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                return
            status = vals.get("Status", "active") or "active"

            success = self.db.add_auction(vals["Title"], vals["Description"], vals["Start Date (YYYY-MM-DD)"],
                                          vals["End Date (YYYY-MM-DD)"], reserve_price, auctioneer_id, status)
            if success:
                messagebox.showinfo("Success", "Auction added")
                self.refresh_auction_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add auction")

        tk.Button(win, text="Add", command=on_add).pack()

    def admin_edit_auction_window(self):
        selected = self.auction_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an auction to edit")
            return
        vals = self.auction_tree.item(selected[0])['values']
        auction_id = vals[0]

        win = tk.Toplevel(self.root)
        win.title("Edit Auction")

        fields = ["Title", "Description", "Start Date (YYYY-MM-DD)", "End Date (YYYY-MM-DD)",
                  "Reserve Price", "Current Bid", "Auctioneer ID", "Status"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(win, text=field).pack()
            entry = tk.Entry(win)
            entry.insert(0, vals[i+1])
            entry.pack()
            entries[field] = entry

        def on_update():
            vals2 = {field: ent.get() for field, ent in entries.items()}
            try:
                datetime.strptime(vals2["Start Date (YYYY-MM-DD)"], "%Y-%m-%d")
                datetime.strptime(vals2["End Date (YYYY-MM-DD)"], "%Y-%m-%d")
                reserve_price = float(vals2["Reserve Price"])
                current_bid = float(vals2["Current Bid"])
                auctioneer_id = int(vals2["Auctioneer ID"])
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                return
            status = vals2.get("Status", "active") or "active"

            success = self.db.update_auction(auction_id, vals2["Title"], vals2["Description"], vals2["Start Date (YYYY-MM-DD)"],
                                             vals2["End Date (YYYY-MM-DD)"], reserve_price, current_bid, auctioneer_id, status)
            if success:
                messagebox.showinfo("Success", "Auction updated")
                self.refresh_uction_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update auction")

        tk.Button(win, text="Update", command=on_update).pack()

    def admin_delete_auction(self):
        selected = self.auction_tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an auction to delete")
            return
        vals = self.auction_tree.item(selected[0])['values']
        auction_id = vals[0]

        confirm = messagebox.askyesno(
            "Confirm Delete", f"Delete auction '{vals[1]}'?")
        if confirm:
            success = self.db.delete_auction(auction_id)
            if success:
                messagebox.showinfo("Success", "Auction deleted")
                self.refresh_auction_list()
            else:
                messagebox.showerror("Error", "Failed to delete auction")

    def populate_bids_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Bids Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.bids_tree = ttk.Treeview(
            tree_frame,
            columns=("Bid ID", "Auction ID", "Bidder Name",
                     "Bid Amount", "Bid Time"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "Bid ID": 50,
            "Auction ID": 100,
            "Bidder Name": 150,
            "Bid Amount": 100,
            "Bid Time": 150
        }

        for col in self.bids_tree["columns"]:
            self.bids_tree.heading(col, text=col)
            self.bids_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.bids_tree.yview)
        self.bids_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.bids_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Refresh the bids list
        self.refresh_bids_list()

    def refresh_bids_list(self):
        for i in self.bids_tree.get_children():
            self.bids_tree.delete(i)
        bids = self.db.get_all_bids()
        for bid in bids:
            self.bids_tree.insert('', 'end', values=(
                bid['bid_id'],
                bid['auction_id'],
                bid['bidder_name'],
                bid['bid_amount'],
                bid['bid_time']
            ))

    def populate_auction_history(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Auction History",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.history_tree = ttk.Treeview(
            tree_frame,
            columns=("History ID", "Auction ID", "Winner ID",
                     "Final Bid Amount", "End Time"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "History ID": 50,
            "Auction ID": 100,
            "Winner ID": 100,
            "Final Bid Amount": 150,
            "End Time": 150
        }

        for col in self.history_tree["columns"]:
            self.history_tree.heading(col, text=col)
            self.history_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.history_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Refresh the auction history list
        self.refresh_auction_history()

    def refresh_auction_history(self):
        for i in self.history_tree.get_children():
            self.history_tree.delete(i)
        history = self.db.get_auction_history()
        for record in history:
            self.history_tree.insert('', 'end', values=(
                record['history_id'],
                record['auction_id'],
                record['winner_id'],
                record['final_bid_amount'],
                record['end_time']
            ))

    def populate_auctioneer_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Auctioneer Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.auctioneer_tree = ttk.Treeview(
            tree_frame,
            columns=("Auctioneer ID", "Name", "Contact Info"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "Auctioneer ID": 100,
            "Name": 150,
            "Contact Info": 200
        }

        for col in self.auctioneer_tree["columns"]:
            self.auctioneer_tree.heading(col, text=col)
            self.auctioneer_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.auctioneer_tree.yview)
        self.auctioneer_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.auctioneer_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Refresh the auctioneer list
        self.refresh_auctioneer_list()

    def refresh_auctioneer_list(self):
        for i in self.auctioneer_tree.get_children():
            self.auctioneer_tree.delete(i)
        auctioneers = self.db.get_all_auctioneers()
        for auctioneer in auctioneers:
            self.auctioneer_tree.insert('', 'end', values=(
                auctioneer['auctioneer_id'],
                auctioneer['name'],
                auctioneer['contact_info']
            ))

    def populate_feedback_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Feedback Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.feedback_tree = ttk.Treeview(
            tree_frame,
            columns=("Feedback ID", "User ID",
                     "Auction ID", "Rating", "Comment"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "Feedback ID": 100,
            "User ID": 100,
            "Auction ID": 100,
            "Rating": 100,
            "Comment": 300
        }

        for col in self.feedback_tree["columns"]:
            self.feedback_tree.heading(col, text=col)
            self.feedback_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.feedback_tree.yview)
        self.feedback_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.feedback_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Refresh the feedback list
        self.refresh_feedback_list()

    def refresh_feedback_list(self):
        for i in self.feedback_tree.get_children():
            self.feedback_tree.delete(i)
        feedbacks = self.db.get_all_feedbacks()
        for feedback in feedbacks:
            self.feedback_tree.insert('', 'end', values=(
                feedback['feedback_id'],
                feedback['user_id'],
                feedback['auction_id'],
                feedback['rating'],
                feedback['comment']
            ))

    def populate_payment_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Payment Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.payment_tree = ttk.Treeview(
            tree_frame,
            columns=("Payment ID", "Bidder ID", "Auction ID",
                     "Amount", "Payment Date", "Payment Method"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "Payment ID": 100,
            "Bidder ID": 100,
            "Auction ID": 100,
            "Amount": 100,
            "Payment Date": 150,
            "Payment Method": 150
        }

        for col in self.payment_tree["columns"]:
            self.payment_tree.heading(col, text=col)
            self.payment_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.payment_tree.yview)
        self.payment_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.payment_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Refresh the payment list
        self.refresh_payment_list()

    def refresh_payment_list(self):
        for i in self.payment_tree.get_children():
            self.payment_tree.delete(i)
        payments = self.db.get_all_payments()
        for payment in payments:
            self.payment_tree.insert('', 'end', values=(
                payment['payment_id'],
                payment['bidder_id'],
                payment['auction_id'],
                payment['amount'],
                payment['payment_date'],
                payment['payment_method']
            ))

    def populate_item_management(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Item Management",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Main content container
        content_frame = ttk.Frame(frame, style='Custom.TFrame')
        content_frame.pack(fill='both', expand=True)

        # Create TreeView with styling
        tree_frame = ttk.Frame(content_frame)
        tree_frame.pack(side='left', fill='both', expand=True)

        self.item_tree = ttk.Treeview(
            tree_frame,
            columns=("Item ID", "Name", "Description",
                     "Category ID", "Starting Price", "Auction ID"),
            show='headings',
            style='Custom.Treeview'
        )

        # Configure columns with better widths
        column_widths = {
            "Item ID": 100,
            "Name": 150,
            "Description": 200,
            "Category ID": 100,
            "Starting Price": 100,
            "Auction ID": 100
        }

        for col in self.item_tree["columns"]:
            self.item_tree.heading(col, text=col)
            self.item_tree.column(
                col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.item_tree.yview)
        self.item_tree.configure(yscrollcommand=scrollbar.set)

        # Pack tree and scrollbar
        self.item_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Control buttons frame
        controls = ttk.Frame(
            content_frame, style='Custom.TFrame', padding=(20, 0))
        controls.pack(side='right', fill='y')

        # Add buttons with consistent styling
        buttons = [
            ("Add Item", self.admin_add_item_window),
            ("Edit Item", self.admin_edit_item_window),
            ("Delete Item", self.admin_delete_item)
        ]

        for text, command in buttons:
            ttk.Button(
                controls,
                text=text,
                style='Action.TButton',
                command=command
            ).pack(pady=5)

        # Refresh the item list
        self.refresh_item_list()

    def refresh_item_list(self):
        for i in self.item_tree.get_children():
            self.item_tree.delete(i)
        items = self.db.get_all_items()
        for item in items:
            self.item_tree.insert('', 'end', values=(
                item['item_id'],
                item['name'],
                item['description'],
                item['category_id'],
                item['starting_price'],
                item['auction_id']
            ))

    def admin_add_item_window(self):
        # Create a new window for adding an item
        win = tk.Toplevel(self.root)
        win.title("Add Item")
        win.geometry("400x400")

        # Form fields
        fields = [
            ("Name", "name"),
            ("Description", "description"),
            ("Category ID", "category_id"),
            ("Starting Price", "starting_price"),
            ("Auction ID", "auction_id")
        ]

        entries = {}
        for i, (label, field) in enumerate(fields):
            ttk.Label(win, text=label, style='Custom.TLabel').grid(
                row=i, column=0, padx=10, pady=10, sticky='w')
            entry = ttk.Entry(win, style='Custom.TEntry', width=30)
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[field] = entry

        # Submit button
        def on_submit():
            data = {field: entry.get() for field, entry in entries.items()}
            success = self.db.add_item(
                data['name'], data['description'], data['category_id'], data['starting_price'], data['auction_id'])
            if success:
                messagebox.showinfo("Success", "Item added successfully.")
                self.refresh_item_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add item.")

        ttk.Button(win, text="Submit", style='Action.TButton', command=on_submit).grid(
            row=len(fields), column=0, columnspan=2, pady=20)

    def admin_edit_item_window(self):
        # Get the selected item
        selected_item = self.item_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected.")
            return

        # Get the item details
        item_values = self.item_tree.item(selected_item, 'values')
        item_id = item_values[0]

        # Create a new window for editing the item
        win = tk.Toplevel(self.root)
        win.title("Edit Item")
        win.geometry("400x400")

        # Form fields
        fields = [
            ("Name", "name", item_values[1]),
            ("Description", "description", item_values[2]),
            ("Category ID", "category_id", item_values[3]),
            ("Starting Price", "starting_price", item_values[4]),
            ("Auction ID", "auction_id", item_values[5])
        ]

        entries = {}
        for i, (label, field, value) in enumerate(fields):
            ttk.Label(win, text=label, style='Custom.TLabel').grid(
                row=i, column=0, padx=10, pady=10, sticky='w')
            entry = ttk.Entry(win, style='Custom.TEntry', width=30)
            entry.insert(0, value)  # Pre-fill the entry with the current value
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[field] = entry

        # Submit button
        def on_submit():
            data = {field: entry.get() for field, entry in entries.items()}
            success = self.db.update_item(
                item_id, data['name'], data['description'], data['category_id'], data['starting_price'], data['auction_id'])
            if success:
                messagebox.showinfo("Success", "Item updated successfully.")
                self.refresh_item_list()
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update item.")

        ttk.Button(win, text="Submit", style='Action.TButton', command=on_submit).grid(
            row=len(fields), column=0, columnspan=2, pady=20)

    def admin_delete_item(self):
        selected_item = self.item_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No item selected.")
            return

        item_id = self.item_tree.item(selected_item, 'values')[0]
        success = self.db.delete_item(item_id)
        if success:
            messagebox.showinfo("Success", "Item deleted successfully.")
            self.refresh_item_list()
        else:
            messagebox.showerror("Error", "Failed to delete item.")

    # --- User Dashboard ---
    def show_user_dashboard(self):
        self.clear_frame()

        # Fetch user data
        user_data = self.db.get_user_by_id(self.current_user_id)
        if not user_data:
            messagebox.showerror("Error", "Could not fetch user data")
            return

        # Header with styling
        header_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        tk.Label(
            header_frame,
            text="User Dashboard",
            font=self.fonts['header'],
            bg=self.colors['primary'],
            fg=self.colors['white']
        ).pack(pady=10)

        tk.Label(
            header_frame,
            text=f"Welcome, {user_data['username']}!",
            font=self.fonts['header'],
            bg=self.colors['primary'],
            fg=self.colors['accent']
        ).pack(pady=10)

        # Tab control with styling
        tab_control = ttk.Notebook(self.main_frame)

        # Style the tabs
        self.style.configure(
            "TNotebook",
            background=self.colors['white'],
            borderwidth=0
        )
        self.style.configure(
            "TNotebook.Tab",
            background=self.colors['light_gray'],
            padding=[10, 5],
            font=self.fonts['body']
        )

        # User Profile tab
        profile_tab = ttk.Frame(tab_control)
        tab_control.add(profile_tab, text='My Profile')
        self.populate_user_profile(profile_tab)

        # Active Auctions tab
        active_auction_tab = ttk.Frame(tab_control)  # Define the tab here
        tab_control.add(active_auction_tab, text='Active Auctions')
        self.populate_active_auctions(active_auction_tab)  # Now this will work

        # Feedback tab
        feedback_tab = ttk.Frame(tab_control)
        tab_control.add(feedback_tab, text='Feedback')
        self.populate_feedback(feedback_tab)

        # Payment tab
        payment_tab = ttk.Frame(tab_control)
        tab_control.add(payment_tab, text='Payments')
        self.populate_payment_section(payment_tab)

        # Auction Rules tab
        rules_tab = ttk.Frame(tab_control)
        tab_control.add(rules_tab, text='Auction Rules')
        self.populate_auction_rules(rules_tab)

        tab_control.pack(expand=1, fill='both')

        # Styled logout button
        ttk.Button(
            self.main_frame,
            text="Logout",
            style='Custom.TButton',
            command=self.logout
        ).pack(pady=20)

    def on_enter(self, e):
        e.widget['background'] = self.colors['secondary']

    def on_leave(self, e):
        e.widget['background'] = self.colors['primary']

    def populate_user_profile(self, frame):
        # First fetch user data
        user_data = self.db.get_user_by_id(self.current_user_id)
        if not user_data:
            messagebox.showerror("Error", "Could not fetch user data")
            return

        # Use padding instead of padx/pady for ttk.Frame
        frame.configure(padding=(20, 20))

        # User info container with custom style
        info_frame = ttk.Frame(frame, style='Custom.TFrame')
        info_frame.pack(fill='x', pady=10)

        # Username and email (read-only)
        readonly_frame = ttk.Frame(info_frame, style='Custom.TFrame')
        readonly_frame.pack(fill='x', pady=10)

        ttk.Label(
            readonly_frame,
            text="Username:",
            font=self.fonts['subheader'],
            style='Custom.TLabel'
        ).pack(anchor='w')

        ttk.Label(
            readonly_frame,
            text=f"{user_data['username']}",
            font=self.fonts['body'],
            style='Info.TLabel'
        ).pack(fill='x')

        # Rest of your existing code, but replace 'user' with 'user_data'
        fields = [
            ("First Name:", 'user_first_name_edit'),
            ("Last Name:", 'user_last_name_edit'),
            ("Phone Number:", 'user_phone_edit'),
            ("Address:", 'user_address_edit')
        ]

        for label_text, field_name in fields:
            field_frame = tk.Frame(info_frame, bg=self.colors['white'])
            field_frame.pack(fill='x', pady=5)

            tk.Label(
                field_frame,
                text=label_text,
                font=self.fonts['body'],
                bg=self.colors['white'],
                fg=self.colors['primary']
            ).pack(anchor='w')

            setattr(self, field_name, ttk.Entry(
                field_frame,
                style='Custom.TEntry',
                width=40
            ))
            getattr(self, field_name).pack(fill='x', pady=(0, 5))
            field_value = user_data.get(field_name.split('_')[1], '') or ''
            getattr(self, field_name).insert(0, field_value)

        # Buttons frame
        button_frame = tk.Frame(frame, bg=self.colors['white'])
        button_frame.pack(pady=20)

        ttk.Button(
            button_frame,
            text="Update Profile",
            style='Custom.TButton',
            command=self.user_update_self
        ).pack(side='left', padx=5)

        ttk.Button(
            button_frame,
            text="Delete Account",
            style='Custom.TButton',
            command=self.user_delete_self
        ).pack(side='left', padx=5)

    def user_update_self(self):
        first_name = self.user_first_name_edit.get()
        last_name = self.user_last_name_edit.get()
        phone = self.user_phone_edit.get()
        address = self.user_address_edit.get()

        success = self.db.update_user_self(
            self.current_user_id, first_name, last_name, phone, address)
        if success:
            messagebox.showinfo("Success", "Profile updated")
        else:
            messagebox.showerror("Error", "Failed to update profile")

    def user_delete_self(self):
        confirm = messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete your account?")
        if confirm:
            success = self.db.delete_user_self(self.current_user_id)
            if success:
                messagebox.showinfo("Success", "Your account was deleted")
                self.logout()
            else:
                messagebox.showerror("Error", "Failed to delete account")

    def populate_active_auctions(self, frame):
        self.active_auction_tree = ttk.Treeview(frame, columns=(
            "ID", "Title", "Description", "Start Date", "End Date", "Reserve Price", "Current Bid", "Status"), show='headings')
        columns = ("ID", "Title", "Description", "Start Date",
                   "End Date", "Reserve Price", "Current Bid", "Status")
        for col in columns:
            self.active_auction_tree.heading(col, text=col)
            self.active_auction_tree.column(col, width=100)
        self.active_auction_tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=self.active_auction_tree.yview)
        scrollbar.pack(side='left', fill='y')
        self.active_auction_tree.configure(yscrollcommand=scrollbar.set)

        control_frame = tk.Frame(frame)
        control_frame.pack(side='right', fill='y', padx=10)

        tk.Button(control_frame, text="Refresh",
                  command=self.refresh_active_auction_list).pack(pady=5)
        tk.Button(control_frame, text="Place Bid",
                  command=self.place_bid_window).pack(pady=5)
        # The "View Auction Rules" button has been removed as requested

        self.refresh_active_auction_list()

    def refresh_active_auction_list(self):
        for i in self.active_auction_tree.get_children():
            self.active_auction_tree.delete(i)
        auctions = self.db.get_active_auctions()
        for auction in auctions:
            self.active_auction_tree.insert('', 'end', values=(
                auction['auction_id'],
                auction['title'],
                auction['description'],
                auction['start_date'],
                auction['end_date'],
                auction['reserve_price'],
                auction['current_bid'],
                auction['status']
            ))

    def place_bid_window(self, auction_id=None):
        if not auction_id:
            selected = self.active_auction_tree.selection()
            if not selected:
                messagebox.showerror(
                    "Error", "Select an auction to place a bid")
                return
            auction_vals = self.active_auction_tree.item(selected[0])['values']
            auction_id = auction_vals[0]
            try:
                # Convert to float to prevent TypeError
                current_bid = float(auction_vals[6])
            except ValueError:
                messagebox.showerror("Error", "Invalid current bid value.")
                return
        else:
            # Fetch auction details from the database if auction_id is passed
            auction = next((a for a in self.db.get_active_auctions()
                           if a['auction_id'] == auction_id), None)
            if not auction:
                messagebox.showerror("Error", "Auction not found.")
                return
            current_bid = auction['current_bid']

        win = tk.Toplevel(self.root)
        win.title(f"Place Bid for Auction: {auction_id}")

        tk.Label(win, text=f"Current Bid: {current_bid}").pack(pady=5)

        tk.Label(win, text="Enter your bid:").pack()
        bid_entry = tk.Entry(win)
        bid_entry.pack()

        def on_place_bid():
            try:
                bid_amount = float(bid_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number for bid.")
                return
            if bid_amount <= current_bid:
                messagebox.showerror(
                    "Error", "Bid must be higher than the current bid.")
                return
            success = self.db.place_bid(
                self.current_user_id, auction_id, bid_amount)
            if success:
                messagebox.showinfo("Success", "Bid placed successfully")
                win.destroy()
                self.refresh_active_auction_list()
            else:
                messagebox.showerror("Error", "Failed to place bid")

        tk.Button(win, text="Place Bid", command=on_place_bid).pack(pady=10)

        auction_frame = tk.Frame(self.main_frame, bg=self.colors['white'])
        auction_frame.pack(fill='both', expand=True)

        for auction in self.db.get_active_auctions():
            card = tk.Frame(
                auction_frame, bg=self.colors['light_gray'], padx=10, pady=10, relief='solid', borderwidth=1)
            card.pack(fill='x', pady=5)

            tk.Label(
                card,
                text=auction['title'],
                font=self.fonts['subheader'],
                bg=self.colors['light_gray'],
                fg=self.colors['primary']
            ).pack(anchor='w')

            tk.Label(
                card,
                text=f"Current Bid: ₹{auction['current_bid']}",
                font=self.fonts['body'],
                bg=self.colors['light_gray'],
                fg=self.colors['secondary']
            ).pack(anchor='w')

            tk.Button(
                card,
                text="Place Bid",
                font=self.fonts['button'],
                bg=self.colors['accent'],
                fg=self.colors['white'],
                command=lambda a=auction['auction_id']: self.place_bid_window(
                    a)
            ).pack(anchor='e', pady=5)

    def populate_auction_rules(self, frame):
        frame.configure(padding=(20, 20))

        # Header with styled container
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Auction Rules",
            style='Header.TLabel'
        ).pack(pady=10)

        # Rules container
        rules_container = ttk.Frame(frame, style='Custom.TFrame')
        rules_container.pack(fill='both', expand=True)

        # Create canvas with scrollbar
        canvas = tk.Canvas(
            rules_container,
            bg=self.colors['white'],  # Use tk.Canvas for background color
            highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(
            rules_container,
            orient="vertical",
            command=canvas.yview
        )

        # Rules frame inside canvas
        rules_frame = tk.Frame(canvas, bg=self.colors['white'])

        # Rules list
        rules = [
            "All bids are final.",
            "Payment must be made within 24 hours.",
            "No returns on art pieces.",
            "Jewelry authenticity certificate provided.",
            "Books are sold as-is.",
            "Car must be picked up within 7 days.",
            "Stamp collection is sold as a set.",
            "Home appliances have a 30-day warranty.",
            "Designer clothing must be dry cleaned.",
            "Sports memorabilia comes with a certificate of authenticity.",
            "Real estate property is sold with clear title.",
            "Antique furniture is sold with minor wear and tear.",
            "Musical instruments are tuned before sale.",
            "Toys and games are suitable for ages 3+.",
            "Gardening tools are sold without plants.",
            "Kitchenware is dishwasher safe.",
            "Office supplies are sold in bulk.",
            "Pet supplies are non-refundable.",
            "Travel gear is sold with a 1-year warranty."
        ]

        # Add rules with alternating backgrounds
        for i, rule in enumerate(rules, 1):
            rule_frame = tk.Frame(
                rules_frame,
                bg=self.colors['white'] if i % 2 == 0 else self.colors['light_gray']
            )
            rule_frame.pack(fill='x', pady=1)

            # Rule number
            tk.Label(
                rule_frame,
                text=f"{i}.",
                font=self.fonts['body'],
                width=3,
                bg=rule_frame['bg'],
                fg=self.colors['accent']
            ).pack(side='left', padx=(10, 0))

            # Rule text
            tk.Label(
                rule_frame,
                text=rule,
                font=self.fonts['body'],
                bg=rule_frame['bg'],
                fg=self.colors['secondary'],
                anchor='w',
                justify='left'
            ).pack(side='left', fill='x', padx=(5, 10), pady=8)

        # Configure canvas and scrollbar
        canvas.create_window((0, 0), window=rules_frame, anchor='nw')
        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)

        # Configure canvas scrolling
        rules_frame.bind('<Configure>',
                         lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.configure(yscrollcommand=scrollbar.set)

        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        canvas.bind_all('<MouseWheel>', _on_mousewheel)

    def get_latest_bid(self):
        """Fetch the latest bid details from the BID table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT b.bid_id, b.bid_amount, b.auction_id, u.username AS bidder_name
                FROM BID b
                JOIN BIDDER br ON b.bidder_id = br.bidder_id
                JOIN USER u ON br.user_id = u.user_id
                ORDER BY b.bid_time DESC
                LIMIT 1
            """
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching latest bid: {e}")
            return None
        finally:
            cursor.close()

    def place_bid(self, user_id, auction_id, bid_amount):
        """Place a bid for a user on an auction."""
        cursor = self.connection.cursor()
        try:
            # Get the bidder_id for the user
            cursor.execute(
                "SELECT bidder_id FROM BIDDER WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            if not result:
                print("Bidder not found for the given user.")
                return False
            bidder_id = result[0]

            # Insert the bid into the BID table
            cursor.execute(
                "INSERT INTO BID (bidder_id, auction_id, bid_amount) VALUES (%s, %s, %s)",
                (bidder_id, auction_id, bid_amount)
            )

            # Update the current bid in the AUCTION table
            cursor.execute(
                "UPDATE AUCTION SET current_bid = %s WHERE auction_id = %s",
                (bid_amount, auction_id)
            )

            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error placing bid: {e}")
            return False
        finally:
            cursor.close()

    def get_user_name(self, user_id):
        """Fetch the username of a user by their user_id."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor()
        try:
            query = "SELECT username FROM USER WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching username: {e}")
            return None
        finally:
            cursor.close()

    def populate_feedback(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Submit Feedback",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Feedback form container
        form_frame = ttk.Frame(frame, style='Custom.TFrame')
        form_frame.pack(fill='x', pady=10)

        # Auction ID field
        ttk.Label(
            form_frame,
            text="Auction ID:",
            style='Custom.TLabel'
        ).grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.feedback_auction_id_entry = ttk.Entry(
            form_frame, style='Custom.TEntry', width=30)
        self.feedback_auction_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Rating field
        ttk.Label(
            form_frame,
            text="Rating (1-5):",
            style='Custom.TLabel'
        ).grid(row=1, column=0, sticky='w', padx=5, pady=5)

        self.feedback_rating_entry = ttk.Entry(
            form_frame, style='Custom.TEntry', width=30)
        self.feedback_rating_entry.grid(row=1, column=1, padx=5, pady=5)

        # Comment field
        ttk.Label(
            form_frame,
            text="Comment:",
            style='Custom.TLabel'
        ).grid(row=2, column=0, sticky='w', padx=5, pady=5)

        self.feedback_comment_entry = tk.Text(
            form_frame, height=5, width=40, wrap='word')
        self.feedback_comment_entry.grid(row=2, column=1, padx=5, pady=5)

        # Submit button
        ttk.Button(
            frame,
            text="Submit Feedback",
            style='Action.TButton',
            command=self.submit_feedback
        ).pack(pady=20)

    def submit_feedback(self):
        auction_id = self.feedback_auction_id_entry.get()
        rating = self.feedback_rating_entry.get()
        comment = self.feedback_comment_entry.get("1.0", tk.END).strip()

        # Validate inputs
        if not auction_id or not rating:
            messagebox.showerror(
                "Error", "Auction ID and Rating are required.")
            return

        try:
            auction_id = int(auction_id)
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return

        # Submit feedback to the database
        success = self.db.add_feedback(
            self.current_user_id, auction_id, rating, comment)
        if success:
            messagebox.showinfo("Success", "Feedback submitted successfully.")
            self.feedback_auction_id_entry.delete(0, tk.END)
            self.feedback_rating_entry.delete(0, tk.END)
            self.feedback_comment_entry.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Failed to submit feedback.")

    def populate_payment_section(self, frame):
        frame.configure(padding=(20, 20))

        # Create header
        header_frame = ttk.Frame(frame, style='Custom.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))

        ttk.Label(
            header_frame,
            text="Make Payment",
            style='Title.TLabel'
        ).pack(anchor='w')

        # Payment form container
        form_frame = ttk.Frame(frame, style='Custom.TFrame')
        form_frame.pack(fill='x', pady=10)

        # Auction ID field
        ttk.Label(
            form_frame,
            text="Auction ID:",
            style='Custom.TLabel'
        ).grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.payment_auction_id_entry = ttk.Entry(
            form_frame, style='Custom.TEntry', width=30)
        self.payment_auction_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Amount field
        ttk.Label(
            form_frame,
            text="Amount:",
            style='Custom.TLabel'
        ).grid(row=1, column=0, sticky='w', padx=5, pady=5)

        self.payment_amount_entry = ttk.Entry(
            form_frame, style='Custom.TEntry', width=30)
        self.payment_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Payment Method field
        ttk.Label(
            form_frame,
            text="Payment Method:",
            style='Custom.TLabel'
        ).grid(row=2, column=0, sticky='w', padx=5, pady=5)

        self.payment_method_combobox = ttk.Combobox(
            form_frame,
            values=["credit_card", "paypal", "bank_transfer"],
            state="readonly",
            style='Custom.TCombobox'
        )
        self.payment_method_combobox.grid(row=2, column=1, padx=5, pady=5)

        # Submit button
        ttk.Button(
            frame,
            text="Submit Payment",
            style='Action.TButton',
            command=self.submit_payment
        ).pack(pady=20)

    def submit_payment(self):
        auction_id = self.payment_auction_id_entry.get()
        amount = self.payment_amount_entry.get()
        payment_method = self.payment_method_combobox.get()

        # Validate inputs
        if not auction_id or not amount or not payment_method:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            auction_id = int(auction_id)
            amount = float(amount)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return

        # Submit payment to the database
        success = self.db.add_payment(
            self.current_user_id, auction_id, amount, payment_method)
        if success:
            messagebox.showinfo("Success", "Payment submitted successfully.")
            self.payment_auction_id_entry.delete(0, tk.END)
            self.payment_amount_entry.delete(0, tk.END)
            self.payment_method_combobox.set("")
        else:
            messagebox.showerror("Error", "Failed to submit payment.")

    def toggle_dark_mode(self):
        if self.colors['primary'] == '#2c3e50':  # Light mode
            self.colors['primary'] = '#1e1e1e'
            self.colors['secondary'] = '#2e2e2e'
            self.colors['white'] = '#121212'
            self.colors['accent'] = '#bb86fc'
        else:  # Dark mode
            self.colors['primary'] = '#2c3e50'
            self.colors['secondary'] = '#34495e'
            self.colors['white'] = '#ffffff'
            self.colors['accent'] = '#3498db'
        self.show_user_dashboard() if not self.is_admin else self.show_admin_dashboard()
