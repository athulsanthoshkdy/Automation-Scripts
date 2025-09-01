import h5py
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def explore_hdf5_structure(hdf5_file):
    """Explore the structure of the HDF5 file and list all datasets."""
    with h5py.File(hdf5_file, 'r') as hdf:
        # List all top-level groups and datasets
        def recursive_list(name, obj):
            if isinstance(obj, h5py.Group):
                print(f"Group: {name}")
                for subgroup in obj.values():
                    recursive_list(name + '/' + subgroup.name, subgroup)
            elif isinstance(obj, h5py.Dataset):
                print(f"Dataset: {name}")
        
        print("Exploring HDF5 Structure...")
        recursive_list("", hdf)

def load_dataset_names(hdf5_file):
    """Return a list of datasets in the HDF5 file for selection."""
    dataset_names = []
    with h5py.File(hdf5_file, 'r') as hdf:
        # Explore and collect all datasets in the file
        def recursive_list(name, obj):
            if isinstance(obj, h5py.Group):
                for subgroup in obj.values():
                    recursive_list(name + '/' + subgroup.name, subgroup)
            elif isinstance(obj, h5py.Dataset):
                dataset_names.append(name)
        
        recursive_list("", hdf)
    return dataset_names

def hdf5_to_csv(hdf5_file, dataset_name, csv_file):
    """Convert HDF5 dataset to CSV."""
    try:
        with h5py.File(hdf5_file, 'r') as hdf:
            # Read the dataset
            data = hdf[dataset_name][:]
            
            # Convert data to pandas DataFrame and save as CSV
            df = pd.DataFrame(data)
            df.to_csv(csv_file, index=False)
            print(f"Data successfully saved to {csv_file}")
            messagebox.showinfo("Success", f"Data successfully saved to {csv_file}")
    except KeyError as e:
        messagebox.showerror("Error", f"Failed to access the dataset '{dataset_name}': {str(e)}")

def select_file_and_save():
    """Select HDF5 file, choose dataset, and save as CSV."""
    # Create the root Tkinter window (it won't be shown)
    root = tk.Tk()
    root.withdraw()

    # Ask user to select the HDF5 file
    hdf5_file = filedialog.askopenfilename(
        title="Select HDF5 file", 
        filetypes=[("HDF5 Files", "*.h5;*.hdf5"), ("All Files", "*.*")]
    )
    if not hdf5_file:
        print("No file selected. Exiting.")
        return

    # Explore the HDF5 structure
    print(f"Selected HDF5 file: {hdf5_file}")
    dataset_names = load_dataset_names(hdf5_file)
    
    # If there are no datasets, exit
    if not dataset_names:
        print("No datasets found in the file.")
        messagebox.showerror("Error", "No datasets found in the HDF5 file.")
        return

    # Show the list of available datasets to the user
    dataset_selection_window = tk.Toplevel()
    dataset_selection_window.title("Select Dataset")
    
    label = tk.Label(dataset_selection_window, text="Select Dataset to Convert:")
    label.pack(pady=10)
    
    dataset_listbox = tk.Listbox(dataset_selection_window, selectmode=tk.SINGLE, width=50, height=10)
    for dataset in dataset_names:
        dataset_listbox.insert(tk.END, dataset)
    dataset_listbox.pack(pady=10)
    
    def on_select_dataset():
        selected_index = dataset_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No dataset selected.")
            return
        
        selected_dataset = dataset_names[selected_index[0]]
        print(f"Selected dataset: {selected_dataset}")
        
        # Ask user where to save the CSV file
        csv_file = filedialog.asksaveasfilename(
            title="Save CSV as", 
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not csv_file:
            messagebox.showerror("Error", "No save location selected. Exiting.")
            return
        
        # Convert the dataset to CSV
        hdf5_to_csv(hdf5_file, selected_dataset, csv_file)
        dataset_selection_window.destroy()
    
    # Add a button to confirm the dataset selection
    select_button = tk.Button(dataset_selection_window, text="Select and Convert", command=on_select_dataset)
    select_button.pack(pady=20)
    
    dataset_selection_window.mainloop()

# Run the user-friendly function
select_file_and_save()
