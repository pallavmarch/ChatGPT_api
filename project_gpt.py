# -*- coding: utf-8 -*-


!pip install openai
import openai

import pandas as pd

openai.api_key=######################################

"""# case 1"""

response = openai.Completion.create(
    engine='text-davinci-002',
    prompt='What is the difference between LIFO and FIFO?'
)
print(response)

print(response['choices'][0]['text'])

"""# Case 2"""

import openai
openai.api_key=openai.api_key
def generate_text(prompt,model='text-davinci-002',length=100):
  response=openai.Completion.create(
      engine=model,
      prompt=prompt,
      max_tokens=length,
      temperature=0.5, #for randomness
      stop=None  )
  #text=response['choices'][0]['text'].strip()
  text=response.choices[0].text.strip()
  return text

prompt='Write a sad song like the Beatles wrote it'
text=generate_text(prompt)
print(text)

"""CASE 3"""

import openai
import pandas as pd

categories =['Positive','Negative']

openai.api_key=openai.api_key

data=pd.read_csv('/content/drive/MyDrive/Python/iphone14.csv')

classification=[]

for i,row in data.iterrows():
  text=row['text']
  response=openai.Completion.create(
      model='text-davinci-002',
      prompt=f'Please classify the following text into one of the following categories: {categories}\n\n{text}\n\nCategory',
      max_tokens=1,
      temperature=0,
      stop=None  )
  category=response.choices[0].text.strip()

  classification.append(category)

data['Category']=classification
data.to_csv('iphn14_gpt.csv',index=False)
