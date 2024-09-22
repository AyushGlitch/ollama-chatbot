import pandas as pd

def main():
    df1 = pd.read_csv("./dataset/test_text_final.csv")
    df= df1.copy()
    df.reset_index(drop=True, inplace=True)

    rows = len(df)
    batches = rows // 10000  # Use integer division to get the number of batches

    for i in range(batches + 1):  # Include the last batch if there are remaining rows
        startInd = i * 10000
        endInd = (i + 1) * 10000
        batch_df = df[startInd:endInd]
        batch_df.to_csv(f"./dataset/test-text-input-{i+1}.csv", index=False)  # Use f-string and exclude index

if __name__ == "__main__":
    main()
