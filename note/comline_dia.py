import tkinter as tk
import tkinter.filedialog as fd

# no reperence tk apl window
root = tk.Tk()
root.withdraw()

# Open dialog
file = fd.askopenfilename(
    title = "Select file",
    filetypes = [("TEXT",".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

# Open the selected file
if file:
    with open(file,"r", encoding = "utf-8")as fileobj:
        text = fileobj.read()
        print(text)
