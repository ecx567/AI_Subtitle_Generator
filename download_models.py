from faster_whisper import download_model
import shutil
import os

def download_local_model(model_size, output_dir):
    print(f"Downloading model '{model_size}' to '{output_dir}'...")
    # faster-whisper returns the path to the model, but we want it in our specific dir
    # It usually downloads to cache. We can use the 'output_dir' argument if supported or move it.
    # checking docs... download_model(size_or_id, output_dir=None, ...)
    
    path = download_model(model_size, output_dir=output_dir)
    print(f"Model downloaded to: {path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(current_dir, "assets", "models")
    
    # Download 'small' as it is the default we set
    download_local_model("small", os.path.join(models_dir, "small"))
    # Download 'tiny' as a fallback/faster option
    download_local_model("tiny", os.path.join(models_dir, "tiny"))
