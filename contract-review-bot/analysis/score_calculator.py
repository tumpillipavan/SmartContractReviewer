def calculate_final_risk_score(ai_score: int, manual_risk_signals: list[str]) -> int:
    """
    Combines the AI's risk score with manual findings.
    
    Args:
        ai_score (int): Score 0-100 from Gemini.
        manual_risk_signals (list[str]): List of detected risky clauses/keywords manually found.
        
    Returns:
        int: Adjusted and capped score (0-100).
    """
    try:
        base_score = int(ai_score)
    except (ValueError, TypeError):
        base_score = 50 
        
    penalty = len(manual_risk_signals) * 5
    
    final_score = base_score + penalty
    
    if final_score > 100:
        return 100
    if final_score < 0:
        return 0
        
    return final_score