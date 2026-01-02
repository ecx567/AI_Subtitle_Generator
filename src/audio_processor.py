import os
import ffmpeg

def extract_audio(video_path, output_audio_path):
    """
    Extracts audio from a video file and saves it as a WAV file.
    Args:
        video_path (str): Path to the input video file.
        output_audio_path (str): Path to save the extracted audio.
    Returns:
        str: Path to the audio file if successful, None otherwise.
    """
    try:
        if os.path.exists(output_audio_path):
            os.remove(output_audio_path)
            
        print(f"Extracting audio from {video_path} to {output_audio_path}...")
        
        # Check for bundled FFmpeg (for PyInstaller)
        from src.utils import resource_path
        ffmpeg_exe = resource_path(os.path.join("assets", "ffmpeg", "ffmpeg.exe"))
        
        if os.path.exists(ffmpeg_exe):
            print(f"Using bundled FFmpeg: {ffmpeg_exe}")
            # Ensure ffmpeg-python uses this binary
            # ffmpeg-python doesn't easily allow setting binary path per call without environ
            os.environ["FFMPEG_BINARY"] = ffmpeg_exe
        
        (
            ffmpeg
            .input(video_path)
            .output(output_audio_path, ac=1, ar='16k')
            .overwrite_output()
            .run(quiet=True, capture_stdout=True, capture_stderr=True)
        )
        return output_audio_path
    except ffmpeg.Error as e:
        print(f"Error extracting audio: {e.stderr.decode('utf8')}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None
