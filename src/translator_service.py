from deep_translator import GoogleTranslator

def translate_segments(segments, target_lang='es'):
    """
    Translates the 'text' field of each segment to the target language.
    Does not modify timestamps.
    """
    if not segments:
        return []
        
    print(f"Translating {len(segments)} segments to '{target_lang}'...")
    
    # We can batch translate if the library supports it to speed up, 
    # but for simplicity and error handling in deep_translator, we might iterate.
    # deep-translator handles batching automatically in `translate_batch`
    
    texts = [seg['text'] for seg in segments]
    
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        # Split into chunks to avoid potential query length limits if the video is very long
        translated_texts = []
        chunk_size = 50
        
        for i in range(0, len(texts), chunk_size):
            chunk = texts[i:i + chunk_size]
            translated_chunk = translator.translate_batch(chunk)
            translated_texts.extend(translated_chunk)
            
        # Reconstruct segments with translated text
        translated_segments = []
        for i, seg in enumerate(segments):
            new_seg = seg.copy()
            new_seg['text'] = translated_texts[i]
            translated_segments.append(new_seg)
            
        return translated_segments
    except Exception as e:
        print(f"Translation Error: {str(e)}")
        return segments # Return original if translation fails
