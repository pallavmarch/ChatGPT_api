# ChatGPT_api

Import openai and we provide the api_key

Case 1
The specified engine ('text-davinci-002') and a prompt ('What is the difference between LIFO and FIFO?') was provided
the generated answer would be found within the 'choices' list, at index 0, and then within the 'text' key of the dictionary

Case 2
We generated another prompt. However, the temperature parameter was introduced, it brings randomness to the generation process, and the stop parameter is set to None to let the model decide when to stop generating.

Case 3
