from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name("students.csv")

if not csv_path.exists():
    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie"],
            "Marks": [85, 90, 88],
        }
    )
    df.to_csv(csv_path, index=False)
else:
    df = pd.read_csv(csv_path)

s = df["Name"]

print("Series:")
print(s)


