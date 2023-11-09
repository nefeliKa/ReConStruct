import pickle
import pandas
import numpy

# Specify the file path where you saved the dictionary
file_path = "D:\OneDrive - Delft University of Technology\CORE\python files\final\grid_chosen_house_dict.pkl"
# Load the dictionary from the file using Pickle
with open(file_path, 'rb') as file:
    grid_chosen_house_dict = pickle.load(file)

# print(grid_chosen_house_dict.keys())