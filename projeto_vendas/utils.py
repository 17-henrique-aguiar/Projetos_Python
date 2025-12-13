import pandas as pd

def carregar_dataframe():
  if "id" in pd.session.state:
    return pd.session.state["df"]
  return None
