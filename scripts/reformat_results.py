import pandas as pd


df = pd.read_csv("results/results.csv")
df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="ms").dt.strftime("%m-%d-%Y")
df.to_csv("results/formatted_results.csv", index=False)
