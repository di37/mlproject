import os

dirs = [
    "src",
    os.path.join("src", "components"),
    os.path.join("src", "pipeline"),
    "notebook",
    "artifacts",
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    # ".dockerignore",
    # ".gitignore",
    # "README.md",
    # "main_fastapi.py",
    # "main.py",
    os.path.join("src", "__init__.py"),
    os.path.join("src", "exception.py"),
    os.path.join("src", "logger.py"),
    os.path.join("src", "utils.py"),
    os.path.join("src", "components", "__init__.py"),
    os.path.join("src", "components", "data_ingestion.py"),
    os.path.join("src", "components", "data_transformation.py"),
    os.path.join("src", "components", "model_trainer.py"),
    os.path.join("src", "pipeline", "__init__.py"),
    os.path.join("src", "pipeline", "predict_pipeline.py"),
    os.path.join("src", "pipeline", "train_pipeline.py"),
]

for file_ in files:
    with open(file_, "w") as f:
        pass