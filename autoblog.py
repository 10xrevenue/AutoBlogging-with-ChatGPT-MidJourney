import pandas as pd
import openai


dataframe = pd.read_csv("input.csv")

# Substitute your OpenAI API key here
openai.api_key = "Your_openai_key_here"

results = []

for index, row in dataframe.iterrows():
  
    prompt = f"Please write a detailed article about {row['topic']}. Use this information to write the article: {row['context']}"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.7,max_tokens=2048,top_p=0.5)
    results.append([row['topic'], response.choices[0].text])
output_df = pd.DataFrame(results, columns = ['Topic', 'Generated Text'])

output_df.to_csv('output.csv', index=False)
