import pandas as pd
import requests

data = pd.read_json(requests.get('http://localhost:8000/trending').content)
