import math
import re
import tkinter as tk
from tkinter import messagebox
import io

def return_TL(F0, RA):
    FA = F0/ (2 * math.pi * (RA/100))
    TL = 10 * math.log10(1 + (3000 / FA) ** 2)
    TL = round(TL,1)
    return str(TL)

def return_SQ(RK):
    rk = RK/100
    rk = round((1/rk)*100,0)
    return str(rk)

def return_OQ(RK,RG):
    rk = RK/100
    rg = RG/100
    top = 1+rk
    bottom = 2*rg
    OQ = round((top/bottom)*100,1)
    return str(OQ) 

def return_AV(EE):
   AV = round(20 * math.log10(EE), 1)
   return str(AV) 
    
def populate_Finished_File(fileName,F0,AV,TL,SQ,OQ):
    final_file = fileName + ".txt"
    file_path = final_file
    with io.open(file_path, 'w', encoding='utf-8') as file:
        # Write header row
        file.write("F0 (Hz)\tAV (dB)\tTL (dB)\tSQ (%)\tOQ (%)\n")
        # Write data row
        file.write(f"{F0}\t{AV}\t{TL}\t{SQ}\t{OQ}\n")
    
    print(f"File '{file_path}' created successfully.")

# Function to get input values and display results
def calculate_results():
    try:
        # Get inputs from the UI
        F0 = float(entry_F0.get())
        RA = float(entry_RA.get())
        RK = float(entry_RK.get())
        RG = float(entry_RG.get())
        EE = float(entry_EE.get())
        file_name = str(entry_file_name.get())

        # Validate file name: only numbers and Latin letters allowed
        if not re.match(r'^[A-Za-z0-9]+$', file_name):
            messagebox.showerror("Invalid File Name", "File name must contain only numbers and Latin letters.")


        # Calculate results
        av_result = return_AV(EE)
        tl_result = return_TL(F0, RA)
        sq_result = return_SQ(RK)
        oq_result = return_OQ(RK, RG)
        populate_Finished_File(file_name,F0,av_result,tl_result,sq_result,oq_result)

    except ValueError:
        messagebox.showerror("Input Error","Error: Please enter valid numbers in all fields.")

    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Create the main window
root = tk.Tk()
root.title("Parameter Calculator")

# Input labels and fields
tk.Label(root, text="F0 (Hz):").grid(row=0, column=0, padx=5, pady=5)
entry_F0 = tk.Entry(root)
entry_F0.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="EE:").grid(row=1, column=0, padx=5, pady=5)
entry_EE = tk.Entry(root)
entry_EE.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="RA (%):").grid(row=2, column=0, padx=5, pady=5)
entry_RA = tk.Entry(root)
entry_RA.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="RK (%):").grid(row=3, column=0, padx=5, pady=5)
entry_RK = tk.Entry(root)
entry_RK.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="RG (%):").grid(row=4, column=0, padx=5, pady=5)
entry_RG = tk.Entry(root)
entry_RG.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="FileName:").grid(row=5, column=0, padx=5, pady=5)
entry_file_name = tk.Entry(root)
entry_file_name.grid(row=5, column=1, padx=5, pady=5)

# Button to calculate results
btn_calculate = tk.Button(root, text="Calculate", command=calculate_results)
btn_calculate.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()