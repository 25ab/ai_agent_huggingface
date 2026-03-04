from typing import TypedDict

class ResearchState(TypedDict):
    query: str
    plan: str
    research: str
    reflection: str
    final_answer: str
    score: int