import json
from pathlib import Path

from src.models import Founder, StartUp

print(Founder(**json.loads(Path("samples/founders/1.json").read_text())))
print(StartUp(**json.loads(Path("samples/startups/1.json").read_text())))
