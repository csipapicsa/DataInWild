import pandas as pd
import pathlib
import re


def main():
    current_dir = pathlib.Path().resolve()
    df = pd.read_csv(current_dir / ".." / "4_fullTextCleaning" / "FullText_ALL.csv")

    print(df.columns)



    accuracy = re.findall(r'Accuracy:?\s*([\d.]+)%?', text)
    f1_score = re.findall(r'F1 Score:?\s*([\d.]+)', text)

if __name__ == "__main__":
    main()