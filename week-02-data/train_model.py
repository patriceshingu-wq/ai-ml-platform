#train_model.py
import pandas as pd, datetime, os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score)

df = pd.read_csv('..data/transactions.csv')
x = df[['amount', 'time']]
y = df['is_fraud']
x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_tr, y_tr)
y_pred = model.predict(x_te)

acc = accuracy_score(y_te, y_pred)
prec = precision_score(y_te, y_pred, zero_division=0)
rec = recall_score(y_te, y_pred, zero_division=0)
print(f'Acc:{acc:.3f}, Prec:{prec:.3f}, Rec:{rec:.3f}')

os.makedirs('..logs', exist_ok=True)
ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f'..logs/experiments.txt', 'a') as f:
    entry = f'{ts} | Acc={acc:.3f}'
    entry += f' | Prec={prec:.3f} | Rec={rec:.3f}\n'
    f.write(entry)
print('Logged to logs/experiments.txt')