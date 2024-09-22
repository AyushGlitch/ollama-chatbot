import pandas as pd

def join():
    outputPaths= [
        "test-text-output-0.csv",
        "test-text-output-1.csv",
        "test-text-output-2.csv",
        "test-text-output-3.csv",
        "test-text-output-4.csv",
        "test-text-output-5.csv",
        "test-text-output-6.csv",
        "test-text-output-7.csv",
        "test-text-output-8.csv",
        "test-text-output-9.csv",
        "test-text-output-10.csv",
        "test-text-output-11.csv",
        "test-text-output-12.csv",
        "test-text-output-13.csv",
        "test-text-output-14.csv",
    ]

    cnt= len(outputPaths)
    outputFolderPath= "./dataset/"

    df= pd.DataFrame()

    for outputPath in outputPaths:
        tempPath= outputFolderPath + outputPath
        print(tempPath)

        tempDf= pd.read_csv(tempPath)
        df= pd.concat([df, tempDf])

    df.to_csv("./final_test_output.csv", index=False)
    

join()
