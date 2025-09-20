import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from algorithms import algorithms
from utils.file_handler import generate_random_numbers_file, read_numbers_from_file, write_numbers_to_file
from utils.performance import time_algorithm
import subprocess
import os


class SortingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sorting Algorithms Project")
        self.filepath = None

        # Frame for dataset generation options
        dataset_frame = tk.LabelFrame(self.root, text="Dataset Generator", padx=10, pady=10)
        dataset_frame.pack(fill="x", padx=5, pady=5)

        # tk.Label(dataset_frame, text="Lower Limit:").grid(row=0, column=0, sticky="w")
        # self.lower_limit = tk.IntVar(value=1000)
        # tk.Entry(dataset_frame, textvariable=self.lower_limit, width=10).grid(row=0, column=1, padx=5)

        tk.Label(dataset_frame, text="Upper Limit :").grid(row=0, column=2, sticky="w")
        self.upper_limit = tk.IntVar(value=100000)
        tk.Entry(dataset_frame, textvariable=self.upper_limit, width=10).grid(row=0, column=3, padx=5)

        tk.Button(dataset_frame, text="Generate File", command=self.generate_file).grid(row=0, column=4, padx=10)
        tk.Button(dataset_frame, text="Run Dataset Script", command=self.run_dataset_script).grid(row=0, column=5, padx=10)

        # Sorting algorithm selector
        algo_frame = tk.LabelFrame(self.root, text="Sorting Algorithm", padx=10, pady=10)
        algo_frame.pack(fill="x", padx=5, pady=5)

        tk.Label(algo_frame, text="Choose Algorithm:").pack(side="left")
        self.algo_var = tk.StringVar()
        self.algo_selector = ttk.Combobox(algo_frame, textvariable=self.algo_var, state="readonly")
        self.algo_selector['values'] = list(algorithms.keys())
        if algorithms:
            self.algo_selector.current(0)
        self.algo_selector.pack(side="left", padx=5)

        # File load and run buttons
        action_frame = tk.Frame(self.root)
        action_frame.pack(fill="x", pady=5)

        tk.Button(action_frame, text="Load File", command=self.load_file).pack(side="left", padx=5)
        tk.Button(action_frame, text="Run Sorting", command=self.run_sorting).pack(side="left", padx=5)
        tk.Button(action_frame, text="Plot Graph", command=self.plot_graph).pack(side="left", padx=5)

        self.results = {}

    def generate_file(self):
        self.filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if self.filepath:
            # lower = self.lower_limit.get()
            upper = min(self.upper_limit.get(), 100000)
            # if lower >= upper:
            #     messagebox.showerror("Error", "Lower limit must be less than upper limit")
            #     return
            size = upper  # treat upper as dataset size for now
            generate_random_numbers_file(self.filepath, size)
            messagebox.showinfo("File Generated", f"File saved at {self.filepath}")

    def run_dataset_script(self):
        script_path = os.path.join("utils", "generate_datasets.py")
        if not os.path.exists(script_path):
            messagebox.showerror("Error", "generate_datasets.py not found in utils/")
            return
        try:
            subprocess.run(["python", script_path], check=True)
            messagebox.showinfo("Success", "Datasets generated successfully in data/ directory")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run dataset script: {e}")

    def load_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            messagebox.showinfo("File Loaded", f"Loaded {self.filepath}")

    def run_sorting(self):
        if not self.filepath:
            messagebox.showerror("Error", "No file loaded")
            return
        algo_name = self.algo_var.get()
        if not algo_name:
            messagebox.showerror("Error", "No algorithm selected")
            return
        numbers = read_numbers_from_file(self.filepath)
        func = algorithms[algo_name]
        arr = numbers.copy()
        duration, sorted_arr = time_algorithm(func, arr)
        out_path = self.filepath.replace(".txt", f"_{algo_name}.txt")
        write_numbers_to_file(out_path, sorted_arr)
        self.results[algo_name] = duration
        messagebox.showinfo("Sorting Done", f"Algorithm {algo_name} executed in {duration:.4f} seconds.")

    def plot_graph(self):
        if not self.results:
            messagebox.showerror("Error", "No results to plot")
            return
        names = list(self.results.keys())
        times = list(self.results.values())
        plt.bar(names, times)
        plt.ylabel("Time (s)")
        plt.title("Sorting Algorithms Performance")
        plt.show()

    def run(self):
        self.root.mainloop()