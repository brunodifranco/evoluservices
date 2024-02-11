import streamlit as st
import tkinter as tk
from tkinter import filedialog

def select_folder():
   root = tk.Tk()
   root.withdraw()
   folder_path = filedialog.askdirectory(master=root)
   root.destroy()
   return folder_path
