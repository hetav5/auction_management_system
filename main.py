import tkinter as tk
from user_interface import AuctionAppUI

def main():
    root = tk.Tk()
    root.geometry('800x600')
    app = AuctionAppUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
