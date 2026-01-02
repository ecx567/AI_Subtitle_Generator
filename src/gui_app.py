import customtkinter as ctk
import threading
import os
from tkinter import filedialog, messagebox
from src.audio_processor import extract_audio
from src.transcription_engine import TranscriberEngine
from src.translator_service import translate_segments
from src.subtitle_writer import save_to_srt

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AutoSubtitles - CapCut Style")
        self.geometry("600x600")
        
        # Determine theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.video_path = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        self.header_label = ctk.CTkLabel(self, text="AutoSubtitles AI", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=20)
        
        # Input Section
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10, padx=20, fill="x")
        
        self.file_label = ctk.CTkLabel(self.input_frame, text="Select Video:")
        self.file_label.pack(side="left", padx=10)
        
        self.file_entry = ctk.CTkEntry(self.input_frame, placeholder_text="No file selected")
        self.file_entry.pack(side="left", padx=10, expand=True, fill="x")
        
        self.browse_btn = ctk.CTkButton(self.input_frame, text="Browse", command=self.browse_file, width=80)
        self.browse_btn.pack(side="right", padx=10)
        
        # Settings Section
        self.settings_frame = ctk.CTkFrame(self)
        self.settings_frame.pack(pady=10, padx=20, fill="x")
        
        # Language Selection
        ctk.CTkLabel(self.settings_frame, text="Translate to:").grid(row=0, column=0, padx=10, pady=10)
        
        # Mapping for display -> code
        self.languages = {
            "Original (No Translation)": "Original",
            "Spanish": "es",
            "English": "en",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Russian": "ru",
            "Japanese": "ja",
            "Chinese": "zh"
        }
        
        self.lang_option = ctk.CTkOptionMenu(self.settings_frame, values=list(self.languages.keys()))
        self.lang_option.grid(row=0, column=1, padx=10, pady=10)
        self.lang_option.set("Spanish")
        
        # Model Selection
        ctk.CTkLabel(self.settings_frame, text="Model Size:").grid(row=0, column=2, padx=10, pady=10)
        self.model_option = ctk.CTkOptionMenu(self.settings_frame, values=["tiny", "base", "small", "medium"])
        self.model_option.grid(row=0, column=3, padx=10, pady=10)
        self.model_option.set("small")
        
        # Action Section
        self.start_btn = ctk.CTkButton(self, text="Generate Subtitles", command=self.start_process_thread, height=50, font=ctk.CTkFont(size=18))
        self.start_btn.pack(pady=20, padx=20, fill="x")
        
        # Log Section
        self.log_box = ctk.CTkTextbox(self, height=200)
        self.log_box.pack(pady=10, padx=20, fill="both", expand=True)
        self.log("Ready. Select a video to begin.")

    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")
        
    def browse_file(self):
        filetypes = (
            ('Video files', '*.mp4 *.mkv *.avi *.mov *.flv'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(title='Open a video', initialdir='/', filetypes=filetypes)
        if filename:
            self.video_path = filename
            self.file_entry.delete(0, "end")
            self.file_entry.insert(0, filename)
            self.log(f"Selected: {os.path.basename(filename)}")

    def start_process_thread(self):
        if not self.video_path:
            messagebox.showerror("Error", "Please select a video file first.")
            return
            
        self.start_btn.configure(state="disabled", text="Processing...")
        threading.Thread(target=self.run_process, daemon=True).start()
        
    def run_process(self):
        try:
            video_path = self.video_path
            output_dir = os.path.dirname(video_path)
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            audio_path = os.path.join(output_dir, f"{base_name}_temp.wav")
            srt_path = os.path.join(output_dir, f"{base_name}.srt")
            
            # 1. Extract Audio
            self.log(">>> Step 1/4: Extracting audio...")
            if not extract_audio(video_path, audio_path):
                raise Exception("Audio extraction failed. Check ffmpeg.")
                
            # 2. Transcribe
            model_size = self.model_option.get()
            self.log(f">>> Step 2/4: Transcribing with model '{model_size}' (this takes time)...")
            
            transcriber = TranscriberEngine(model_size=model_size)
            segments, detected_lang, probability = transcriber.transcribe(audio_path)
            
            precision_percent = f"{probability * 100:.2f}%"
            self.log(f"Transcription complete.")
            self.log(f"Detected Language: '{detected_lang}' (Confidence: {precision_percent})")
            
            # 3. Translate (Optional)
            selected_label = self.lang_option.get()
            target_lang = self.languages[selected_label]
            
            final_segments = segments
            
            if target_lang != "Original" and target_lang != detected_lang:
                self.log(f">>> Step 3/4: Translating to '{selected_label}' ({target_lang})...")
                final_segments = translate_segments(segments, target_lang)
            else:
                self.log("Skipping translation (Original language selected).")
                
            # 4. Save
            self.log(">>> Step 4/4: Saving SRT file...")
            save_to_srt(final_segments, srt_path)
            
            # Cleanup
            if os.path.exists(audio_path):
                os.remove(audio_path)
                
            self.log(f"DONE! Subtitles saved to:\n{srt_path}")
            messagebox.showinfo("Success", f"Subtitles generated successfully!\n\nDetected Lang: {detected_lang} ({precision_percent})\nFile: {srt_path}")
            
        except Exception as e:
            self.log(f"ERROR: {str(e)}")
            messagebox.showerror("Error", str(e))
        finally:
            self.start_btn.configure(state="normal", text="Generate Subtitles")

if __name__ == "__main__":
    app = App()
    app.mainloop()
