from faster_whisper import WhisperModel
import os

class TranscriberEngine:
    def __init__(self, model_size="small", device="cpu"):
        """
        Initializes the Whisper model.
        Args:
           model_size: tiny, base, small, medium, large-v2.
           device: cpu or cuda.
        """
        print(f"Loading Whisper model '{model_size}' on {device}...")
        
        from src.utils import resource_path
        
        # Check if we have the model bundled
        model_path = resource_path(os.path.join("assets", "models", model_size))
        
        if os.path.exists(model_path):
            print(f"Using bundled model from: {model_path}")
            # When path is provided, faster-whisper loads from there
            self.model = WhisperModel(model_path, device=device, compute_type="int8")
        else:
            print(f"Bundled model not found, using default cache.")
            # compute_type="int8" is good for CPU efficiency
            self.model = WhisperModel(model_size, device=device, compute_type="int8")

    def transcribe(self, audio_path, language=None):
        """
        Transcribes the audio file.
        Returns a list of dicts: {'start': float, 'end': float, 'text': str}
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        print("Starting transcription...")
        segments_generator, info = self.model.transcribe(audio_path, language=language)
        
        print(f"Detected language: {info.language} with probability {info.language_probability}")
        
        results = []
        for segment in segments_generator:
            # You can add a callback or yield here for progress bars in GUI
            # For now, we collect all.
            results.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            })
            
        return results, info.language, info.language_probability
