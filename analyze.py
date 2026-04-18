import pandas as pd

# create a simple dataset
data = {
    'name': ['Alice','Bob','Charlie','Diana'],
    'score': [88, 92, 75, 95],
    'grade': ['B','A','C','A']
}

df = pd.DataFrame(data)
df['passed'] = df['score'] >= 80

print("Dataset:")
print(df)
print("\nAverage Score:", df['score'].mean())
print("Top student:",df.loc[df['score'].idxmax(), 'name'])
