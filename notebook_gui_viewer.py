import json
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Load the Jupyter Notebook as JSON
notebook_path = "example.ipynb"  # Place your .ipynb file in the same directory
with open(notebook_path, "r", encoding="utf-8") as f:
    nb_data = json.load(f)

# Extract code cells and outputs
cell_outputs = []
for cell in nb_data.get("cells", []):
    if cell.get("cell_type") == "code":
        source = "".join(cell.get("source", []))
        outputs = cell.get("outputs", [])
        output_texts = []
        for output in outputs:
            if output.get("output_type") == "stream":
                output_texts.append(output.get("text", ""))
            elif output.get("output_type") == "execute_result":
                data = output.get("data", {})
                output_texts.append(data.get("text/plain", ""))
            elif output.get("output_type") == "error":
                output_texts.append("\n".join(output.get("traceback", [])))
        cell_outputs.append((source, "\n".join(output_texts)))

# Tkinter GUI to display it nicely
def show_gui():
    root = tk.Tk()
    root.title("Fancy Jupyter Notebook Viewer")
    root.geometry("1000x600")

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for idx, (code, output) in enumerate(cell_outputs):
        code_label = ttk.Label(scrollable_frame, text=f"Cell [{idx+1}] Code:", font=("Helvetica", 12, "bold"))
        code_label.pack(anchor="w", pady=(10, 0))

        code_box = ScrolledText(scrollable_frame, height=6, font=("Courier", 10), bg="#f0f0f0")
        code_box.insert(tk.END, code)
        code_box.configure(state="disabled")
        code_box.pack(fill=tk.X)

        output_label = ttk.Label(scrollable_frame, text="Output:", font=("Helvetica", 12, "bold"))
        output_label.pack(anchor="w")

        output_box = ScrolledText(scrollable_frame, height=6, font=("Courier", 10), bg="#e8f5e9")
        output_box.insert(tk.END, output)
        output_box.configure(state="disabled")
        output_box.pack(fill=tk.X, pady=(0, 10))

    root.mainloop()

show_gui()
