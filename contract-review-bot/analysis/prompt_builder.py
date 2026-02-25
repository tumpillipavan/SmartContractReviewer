
SCHEMA_INSTRUCTIONS = """
You are an expert corporate lawyer and contract analyst. Your task is to analyze the provided contract and extract the requested fields strictly in JSON format. Do not include markdown codeblocks or any conversational text around the JSON. ONLY output the JSON object.

Your required JSON schema is exactly:
{
  "contract_type": "The classified type of the contract (e.g., NDA, Employment, Service Agreement)",
  "parties": "Detailed description of the parties involved",
  "contract_duration": "The term of the contract",
  "renewal_terms": "Details about renewal, specifying if it is auto-renewal",
  "payment_terms": "Payment structure, amounts, and terms",
  "termination_clauses": "How the contract can be terminated by either party",
  "liability_clauses": "Detailed summary of indemnification and liability caps/limits",
  "risk_flags": {
      "auto_renewal_risk": {
          "severity": "High/Medium/Low/None",
          "likelihood": "High/Medium/Low/None",
          "explanation": "Detailed explanation"
      },
      "liability_risk": {
          "severity": "High/Medium/Low/None",
          "likelihood": "High/Medium/Low/None",
          "explanation": "Detailed explanation"
      },
      "missing_exit_clause_risk": {
          "severity": "High/Medium/Low/None",
          "likelihood": "High/Medium/Low/None",
          "explanation": "Detailed explanation"
      }
  },
  "risky_sentences": ["Array of direct quotes from the text that are risky"],
  "plain_english_summary": "A 1-2 paragraph summary written in plain English that a non-lawyer can perfectly understand.",
  "overall_risk_score": 0, // An integer strictly between 0 and 100 representing the riskiness of the contract
  "confidence_score": 0 // An integer strictly between 0 and 100 representing your confidence in this extraction
}
"""

def generate_analysis_prompt(contract_text: str, personality: str = "Neutral Summarizer", sensitivity: int = 75) -> str:
    """
    Constructs the prompt securely for the LLM, incorporating custom analyst personality and risk sensitivity.
    """
    prompt = f"""
You are an expert corporate lawyer and contract analyst acting as a '{personality}'. 
Your risk detection sensitivity is set to {sensitivity}/100.
    
{SCHEMA_INSTRUCTIONS}

==== START OF CONTRACT TEXT ====
{contract_text}
==== END OF CONTRACT TEXT ====

Analyze the contract according to the schema above. Provide ONLY valid JSON.
"""
    return prompt