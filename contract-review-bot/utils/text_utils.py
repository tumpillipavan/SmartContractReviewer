import re
import difflib

def find_context_snippet(raw_text: str, risky_sentence: str, padding: int = 150) -> str:
    """
    Finds the exact or near-exact risky sentence in the raw text and returns it with context.
    Uses basic string searching with a fallback to fuzzy matching.
    """
    if not risky_sentence or not raw_text:
        return "Source text not found."
    
    match_index = raw_text.find(risky_sentence)
    
    if match_index == -1:
        
        clean_sentence = re.sub(r'\s+', ' ', risky_sentence).strip()
        pattern = re.escape(clean_sentence).replace(r'\ ', r'\s+')
        match = re.search(pattern, raw_text, re.IGNORECASE)
        if match:
            match_index = match.start()
        else:
            
            lines = raw_text.split('\n')
            best_matches = difflib.get_close_matches(risky_sentence, lines, n=1, cutoff=0.6)
            if best_matches:
                match_index = raw_text.find(best_matches[0])
            else:
                return f"Could not precisely locate this clause in the source text. Snippet: \"{risky_sentence[:50]}...\""

    start = max(0, match_index - padding)
    end = min(len(raw_text), match_index + len(risky_sentence) + padding)
    
    snippet = raw_text[start:end]
    
    highlighted = snippet.replace(risky_sentence, f"⭐ **{risky_sentence}** ⭐")
    
    return f"...{highlighted}..."