## Some sample prompts to test out your Falcon7b endpoint

- **Sample 1: QA example:**

```
User: Can you tell me what is AI?
Assistant:
```

- **Sample 2: Instruct example:**

```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:
```

- **Sample 3: Context QA**

```
Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say "I don't know".

Context:
Neeraj Chopra, the Indian athlete, achieved a historic milestone at the 2020 Summer Olympics held in Tokyo by securing the gold medal in the men's javelin throw event. His performance was remarkable, as he set a new national record with a throw of 87.58 meters during his second attempt. This victory was not only significant for him personally but also for India as a nation. Neeraj Chopra became the first Indian athlete to win a gold medal in track and field at the Olympic Games, a momentous achievement celebrated widely across the country. In a highly competitive field of javelin throwers from around the world, Neeraj's consistent and exceptional performance led to his well-deserved gold medal. His win had a profound impact, inspiring countless aspiring athletes in India and drawing attention to the sport of javelin throw, cementing Neeraj Chopra's status as a symbol of excellence in Indian athletics.

Ques: Who won the 2020 Summer Olympics men's Javelin throw?

Ans:
```

- **Sample 4: Summary**

```
Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say "I don't know".

Context:
Neeraj Chopra, the Indian athlete, achieved a historic milestone at the 2020 Summer Olympics held in Tokyo by securing the gold medal in the men's javelin throw event. His performance was remarkable, as he set a new national record with a throw of 87.58 meters during his second attempt. This victory was not only significant for him personally but also for India as a nation. Neeraj Chopra became the first Indian athlete to win a gold medal in track and field at the Olympic Games, a momentous achievement celebrated widely across the country. In a highly competitive field of javelin throwers from around the world, Neeraj's consistent and exceptional performance led to his well-deserved gold medal. His win had a profound impact, inspiring countless aspiring athletes in India and drawing attention to the sport of javelin throw, cementing Neeraj Chopra's status as a symbol of excellence in Indian athletics.

Summary:

```

- **Sample 5: QA Example**

```
Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, respond with "I can't answer that"

>>QUESTION<< What is 2+2?

>>ANSWER<<

```

- **Sample 6: QA Example**

```
>>QUESTION<<
What would be the most likely results for earth if the moon was suddenly beamed away by an alien species ?

>>ANSWER<<
```
