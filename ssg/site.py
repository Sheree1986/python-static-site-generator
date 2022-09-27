from os import mkdir
import Path from pathlib
import os

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / relative_to(path)
        mkdir(directory, parents=True, exists_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if os.path.isdir(path):
                self.create_dir(path)
