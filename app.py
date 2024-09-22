from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import re
import pandas as pd


def findAndFromContext(context, entityName):
    template = """
        Context: {context}
        Question: {question}

        Context contains the text extracted from an image. Use the given context to give answer to the question asked. Answer should be in the format: --numerical_value--, --unit--. For example, if the answer is 5 grams, then the answer should be written as: --5.0--, --gram--.
        "unit" should be written as it is one of the following: gram, cup, milligram, kilogram, ounce, gallon, volt, watt, pound, millilitre, foot, ton, decilitre, inch, litre, microgram, centimetre, quart, horsepower, kilowatt, hour, gigabyte, millimetre, pint, centilitre, metre, carat, nits

        Answer:
    """

    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOllama(model="gemma2:2b", temperature=0.5)
    # model = ChatOllama(model="qwen2:1.5b", temperature=0.5)
    # model = ChatOllama(model="qwen2:0.5b", temperature=0.5)

    chain = prompt | model

    question = f"Numerical value as floating integer of {entityName}."

    result = chain.invoke({"context": context, "question": question})
    print(result.content)

    matches = re.findall(r'\-\-(.*?)\-\-', result.content)
    print(matches)

    if len(matches) == 2:
        return matches[0] + " " + matches[1]
    else:
        return ""




# Load CSV data
df1 = pd.read_csv('./dataset/test-text-input-5.csv')
outputPath= './dataset/test-text-output-5.csv'

# Take a copy of the slice of the DataFrame
df = df1.copy()  # Change the slice if needed
df['ans_entity_val'] = ""  # Initialize the new column

# Loop through the rows and update the DataFrame
for i in range(len(df)):
    entityName = df['entity_name'][i]
    context = df['extracted_text'][i]

    # Call your function to get the answer
    ans = findAndFromContext(context, entityName)

    # Use .loc[] to update the DataFrame safely
    df.loc[i, 'ans_entity_val'] = ans

    # Save after every 10th iteration
    if (i + 1) % 10 == 0:
        print(f"Saving progress at iteration {i+1}")
        df10 = df[['index', 'ans_entity_val']]
        df10.to_csv(outputPath, index=False)

# Save the final updated DataFrame
df10 = df[['index', 'ans_entity_val']]
df10.to_csv(outputPath, index=False)
