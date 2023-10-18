import spacy

nlp = spacy.load(r"C:\Users\bradl\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\en_core_web_sm\en_core_web_sm-3.7.0")
txt_file_path = r"C:\Users\bradl\Desktop\Wiki.txt"

print(f"Reading file: {txt_file_path}")
with open(txt_file_path) as txt:
    text = txt.read()

print("File content:")
print(text)