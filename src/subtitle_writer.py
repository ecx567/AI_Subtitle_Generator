def format_timestamp(seconds):
    """Converts seconds (float) to SRT timestamp format: HH:MM:SS,mmm"""
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    mins = seconds // 60
    hours = mins // 60
    mins = mins % 60
    seconds = seconds % 60
    return f"{hours:02}:{mins:02}:{seconds:02},{millis:03}"

def save_to_srt(segments, output_file):
    """
    Saves a list of segments to an SRT file.
    segments structure: [{'start': float, 'end': float, 'text': str}, ...]
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(segments, start=1):
                start_time = format_timestamp(segment['start'])
                end_time = format_timestamp(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{text}\n\n")
        print(f"SRT file saved to: {output_file}")
        return True
    except Exception as e:
        print(f"Error saving SRT: {str(e)}")
        return False
