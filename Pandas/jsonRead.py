# json -> handles big data sets
import pandas as pd
df = pd.read_json(r"D:\CODING_CODES\AIML\Pandas\dataset.json")
print(df.to_string())