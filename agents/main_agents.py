import os
from dotenv import load_dotenv

from huggingface_hub import login
from smolagents import CodeAgent
from smolagents.models import TransformersModel


from app.tools import web_search, VisitWebpageTool

load_dotenv()
token = None
login(token)

model = TransformersModel(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    max_new_tokens=128,
    temperature=0.0,        # VERY IMPORTANT
    top_p=1.0,
)
tokenizer = model.tokenizer

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model.model.config.pad_token_id = tokenizer.pad_token_id
if hasattr(model, "tokenizer") and model.tokenizer is not None:
    model.tokenizer.chat_template = "{% for message in messages %}{{ message['content'] }}{% endfor %}"
agent = CodeAgent(
    model=model,
    tools=[web_search, VisitWebpageTool()],
    
)