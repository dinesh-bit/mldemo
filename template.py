import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved.models",
    "src"
]
for d in dirs:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, ".gitkeep"), "w") as f:
        pass

    files = [
        "dvc.yaml",
        "params.yaml",
        ".gitignore",
        os.path.join("src", "__init__.py")
    ]
for f in files:
  with open(f, "w")as f:
    pass

