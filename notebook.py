
import nbformat

# Give the correct notebook path
file_path = "/Users/vaibhav/Desktop/AI_project/intelligent-crop-recommendation/ml-engine/notebooks/01_groundwater_data_exploration.ipynb"

try:
    notebook = nbformat.read(file_path, as_version=4)

    nbformat.validate(notebook)

    print("Notebook is valid!")
    print("Total cells:", len(notebook.cells))

except Exception as e:
    print("Notebook validation failed:", e)
