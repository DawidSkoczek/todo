import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    filepaths = [
        r"C:\Users\dawid\Desktop\!MyPython\!Python Mega Course Learn Python in 60 Days, Build 20 Apps\Project_1\dsds.txt",
        r"C:\Users\dawid\Desktop\!MyPython\!Python Mega Course Learn Python in 60 Days, Build 20 Apps\Project_1\todos.txt"
    ]
    dest_dir = r"C:\Users\dawid\Desktop\!MyPython\Project_1\dest"
    make_archive(filepaths=filepaths, dest_dir=dest_dir)
