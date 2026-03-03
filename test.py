import pandas as pd
import numpy as np


df = pd.read_csv("data/survey_results_public.csv")

df_dev_ai = df[['AIThreat', 'DevType']].copy()
df_dev_ai.to_csv("df_dev_ai.csv", index=False)