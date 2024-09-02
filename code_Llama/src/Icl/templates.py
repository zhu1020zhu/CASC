FinEntity_icl_templates = [
'''Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',
]
FinEntity_fixicl_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
Example 1: 
input: "\"For the moment, disruptions to oil supply are taking a back seat to concerns of weaker demand,\" ANZ analysts said in a note."
output: "{\"value\": \"ANZ\", \"start\": 97, \"end\": 100, \"tag\": \"Neutral\"}"
Example 2: 
input: "An official at a large Hyundai supplier who has spoken to senior officials at the company told Reuters that the automaker was caught off guard by the law. "
output: "{\"value\": \"Hyundai\", \"start\": 23, \"end\": 30, \"tag\": \"Negative\"}\n{\"value\": \"Reuters\", \"start\": 95, \"end\": 102, \"tag\": \"Neutral\"}"
Example 3: 
input: "Banks <.SPXBK>, which tend to benefit from a rising rate environment, gained 2.1%. Healthcare stocks <.SPXHC> got a boost from health insurer Humana Inc's <HUM.N> strong earnings forecast. "
output: "{\"value\": \"Banks\", \"start\": 0, \"end\": 5, \"tag\": \"Positive\"}\n{\"value\": \"Healthcare stocks\", \"start\": 83, \"end\": 100, \"tag\": \"Positive\"}\n{\"value\": \"Humana Inc\", \"start\": 142, \"end\": 152, \"tag\": \"Positive\"}"
Now please complete the task for the following input:\n""",
]
FinEntity_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Considering every sentence as a String in python, provide the entities with the start and end index to mark the boundaries of it including spaces and punctuation using zero-based indexing.
Do not give explanations for the sentiment. In the output,Tag means sentiment; value means entity name. If no entity is found in the sentence, the response should be empty. 
The sentence: \n"{input}"\nOutput:\n""",
]

FinEntity_correct_templates = ["""Performing an Entity-Level Sentiment Analysis and Correction Task
Task Description
Given a financial text, determine whether each entity and its sentiment polarity match the actual context within the text. If the sentiment polarity is incorrect, provide the correct entity-sentiment pairs. Sentiment polarity can be Positive, Negative, or Neutral.

Task Examples
Example 1: 
Sentence:  Abbott has said there is no evidence to link its formulas to the illnesses, while the FDA's inspection found bacteria in environmental testing and not in the product samples.
Pseudo-labels: {{\"value\": \"Abbott\", \"start\": 1, \"end\": 7, \"tag\": \"Neutral\"}}\n{{\"value\": \"FDA\", \"start\": 87, \"end\": 90, \"tag\": \"Neutral\"}}
Output: {{\"value\": \"Abbott\", \"start\": 1, \"end\": 7, \"tag\": \"Neutral\"}}\n{{\"value\": \"FDA\", \"start\": 87, \"end\": 90, \"tag\": \"Neutral\"}}

Example 2:
Sentence: However, technology stocks <.SX8P> continued to remain under pressure as Franco-Italian chipmaker STMicroelectronics <STM.PA> slumped 7.9% after it forecast sales growth to slow in the latter part of the year.
Pseudo-labels: {{\"value\": \"STMicroelectronics\", \"start\": 98, \"end\": 116, \"tag\": \"Negative\"}}
Output: {{\"value\": \"technology stocks\", \"start\": 9, \"end\": 26, \"tag\": \"Negative\"}}\n{{\"value\": \"STMicroelectronics\", \"start\": 98, \"end\": 116, \"tag\": \"Negative\"}}

Example 3:
Sentence: "This only encourages the striking workers, who are more united than ever", a CGT official at TotalEnergies' Feyzin refinery said of the company's conditional offer.
Pseudo-labels: {{\"value\": \"CGT\", \"start\": 78, \"end\": 81, \"tag\": \"Neutral\"}}\n{{\"value\": \"TotalEnergies\", \"start\": 94, \"end\": 107, \"tag\": \"Neutral\"}}
Output: {{\"value\": \"TotalEnergies\", \"start\": 94, \"end\": 107, \"tag\": \"Negative\"}}

Task Execution
Given Sentence: {content}
Pseudo-labels: {pre}

Is it correct?
If correct, please output the pseudo-labels.
If incorrect, please provide the correct answer:
Output:
""",]

FinEntity_correct_icl_templates = ["""Performing an Entity-Level Sentiment Analysis and Correction Task
Task Description
Given a financial text, determine whether each entity and its sentiment polarity match the actual context within the text. If the sentiment polarity is incorrect, provide the correct entity-sentiment pairs. Sentiment polarity can be Positive, Negative, or Neutral.

Task Examples
{example}

Task Execution
Given Sentence: {content}
Pseudo-labels: {pre}

Is it correct?
If correct, please output the pseudo-labels.
If incorrect, please provide the correct answer:
Output:
""",]


SEntFiN_icl_templates = [
'''Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Help me complete a task involving entity-level sentiment analysis in the financial domain.
This task involves named entity recognition (NER) and sentiment tagging within a text. 
Here's a detailed description of the task:
1.Entity Identification: Identify named entities within the input text.
2.Position Indices: Determine the start and end indices of each identified entity within the text.
3.Sentiment Tagging: Assign a sentiment tag to each identified entity based on the context in which it is mentioned (e.g., Positive, Negative, Neutral).
I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Help me complete an entity-level sentiment analysis task in the financial domain. This task includes recognizing named entities and tagging their sentiment within a text.
Here’s a detailed breakdown of the task:
Entity Identification: Identify the named entities within the provided text.
Position Indices: Determine the start and end positions of each identified entity in the text.
Sentiment Tagging: Assign a sentiment label (such as Positive, Negative, or Neutral) to each identified entity based on the context in which it appears.
I will provide some examples for reference.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Assist me with an entity-level sentiment analysis task in the financial domain. The task includes recognizing named entities and tagging their sentiment in a text.
Here's a concise breakdown:
Entity Identification: Find named entities in the text.
Position Indices: Determine the start and end positions of each entity.
Sentiment Tagging: Assign a sentiment label (Positive, Negative, Neutral) based on the context.
I will provide examples for clarity.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Help me with an entity-level sentiment analysis task in the financial domain. The task involves:
Identifying Entities: Recognize named entities in the text.
Locating Positions: Determine the start and end indices of each entity.
Tagging Sentiment: Assign sentiment labels (Positive, Negative, Neutral) based on the context.
I'll provide examples to illustrate.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Identify companies or organizations in the text and classify their sentiment as 'Neutral', 'Positive', or 'Negative'. For each entity, provide its name, start and end indices, and sentiment tag.
Task outline:
Entity Identification: Extract company or organization names from the text.
Position Indices: Determine start and end indices of each entity.
Sentiment Classification: Assign a sentiment tag (Neutral, Positive, Negative) based on context.
I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Identify and classify the sentiment of companies or organizations in the text. For each entity, provide its name, start and end indices, and sentiment tag.
Task details:
Entity Recognition: Find and extract company or organization names.
Indexing: Provide the start and end indices for each entity.
Sentiment Analysis: Tag each entity with 'Neutral', 'Positive', or 'Negative' sentiment based on context.
I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',

'''Extract company or organization names from the text and determine their sentiment ('Neutral', 'Positive', or 'Negative'). Include the entity's name, start and end indices, and sentiment tag in the output.
Steps:
Identify Entities: Locate and extract names of companies or organizations.
Mark Positions: Determine the start and end positions of each entity.
Classify Sentiment: Assign a sentiment label to each entity based on its context.
I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',
]


SEntFiN_fixicl_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
Example 1: 
input: "Unichem Lab Q1 net up 9 per cent at Rs 36 crore"
output: "{\"value\": \"Unichem Lab\", \"start\": 0, \"end\": 11, \"tag\": \"positive\"}"
Example 2: 
input: "Dependence on power sector may hit BHELs margins"
output: "{\"value\": \"BHEL\", \"start\": 35, \"end\": 39, \"tag\": \"negative\"}"
Example 3: 
input: "Infosys director Ann M Fudge wont seek reappointment after term expiry"
output: "{\"value\": \"Infosys\", \"start\": 0, \"end\": 7, \"tag\": \"neutral\"}"
Now please complete the task for the following input:\n""",

"""Help me complete a task involving entity-level sentiment analysis in the financial domain.
This task involves named entity recognition (NER) and sentiment tagging within a text. 
Here's a detailed description of the task:
1.Entity Identification: Identify named entities within the input text.
2.Position Indices: Determine the start and end indices of each identified entity within the text.
3.Sentiment Tagging: Assign a sentiment tag to each identified entity based on the context in which it is mentioned (e.g., Positive, Negative, Neutral).
I will give you some examples.
Example 1: 
input: "Investors should avoid power sector till the Lok Sabha elections: G Chokkalingam, Equinomics"
output: "{\"value\": \"power sector\", \"start\": 23, \"end\": 35, \"tag\": \"negative\"}\n{\"value\": \"Equinomics\", \"start\": 82, \"end\": 92, \"tag\": \"neutral\"}"
Example 2: 
input: "BoB profit rises 61% to Rs 1,019 cr"
output: "{\"value\": \"BoB\", \"start\": 0, \"end\": 3, \"tag\": \"positive\"}"
Example 3: 
input: "Nickel futures down 0.27 per cent on overseas cues, low demand"
output: "{\"value\": \"Nickel futures\", \"start\": 0, \"end\": 14, \"tag\": \"negative\"}"
Now please complete the task for the following input:\n""",

"""Help me complete an entity-level sentiment analysis task in the financial domain. This task includes recognizing named entities and tagging their sentiment within a text.
Here’s a detailed breakdown of the task:
Entity Identification: Identify the named entities within the provided text.
Position Indices: Determine the start and end positions of each identified entity in the text.
Sentiment Tagging: Assign a sentiment label (such as Positive, Negative, or Neutral) to each identified entity based on the context in which it appears.
I will provide some examples for reference.
Example 1: 
input: "Oil prices extend losses in Asian trade"
output: "{\"value\": \"Oil\", \"start\": 0, \"end\": 3, \"tag\": \"negative\"}"
Example 2: 
input: "XL Energy bags Rs 130 mn solar power contract;stk up"
output: "{\"value\": \"XL Energy\", \"start\": 0, \"end\": 9, \"tag\": \"positive\"}"
Example 3: 
input: "Gold steadies as buoyant equities balance Ukraine tensions"
output: "{\"value\": \"Gold\", \"start\": 0, \"end\": 4, \"tag\": \"neutral\"}"
Now please complete the task for the following input:\n""",

"""
Assist me with an entity-level sentiment analysis task in the financial domain. The task includes recognizing named entities and tagging their sentiment in a text.
Here's a concise breakdown:
Entity Identification: Find named entities in the text.
Position Indices: Determine the start and end positions of each entity.
Sentiment Tagging: Assign a sentiment label (Positive, Negative, Neutral) based on the context.
I will provide examples for clarity.
Example 1: 
input: "Nikkei rises as yen plumbs 6-year lows"
output: "{\"value\": \"Nikkei\", \"start\": 0, \"end\": 6, \"tag\": \"positive\"}\n{\"value\": \"yen\", \"start\": 16, \"end\": 19, \"tag\": \"negative\"}"
Example 2: 
input: "TVS Motor tanks over 11 per cent despite strong Q1 show"
output: "{\"value\": \"TVS Motor\", \"start\": 0, \"end\": 9, \"tag\": \"negative\"}"
Example 3: 
input: "Nasdaq Record: Then and Now"
output: "{\"value\": \"Nasdaq\", \"start\": 0, \"end\": 6, \"tag\": \"neutral\"}"
Now please complete the task for the following input:\n""",

"""
Help me with an entity-level sentiment analysis task in the financial domain. The task involves:
Identifying Entities: Recognize named entities in the text.
Locating Positions: Determine the start and end indices of each entity.
Tagging Sentiment: Assign sentiment labels (Positive, Negative, Neutral) based on the context.
I'll provide examples to illustrate.
Example 1: 
input: "JSW Energy Q2 net up 54% at Rs 492 crore"
output: "{\"value\": \"JSW Energy\", \"start\": 0, \"end\": 10, \"tag\": \"positive\"}"
Example 2: 
input: "Neyveli Lignite shares gain as Sebi gives Tamil Nadu consent to buy stake"
output: "{\"value\": \"Neyveli Lignite\", \"start\": 0, \"end\": 15, \"tag\": \"positive\"}\n{\"value\": \"Sebi\", \"start\": 31, \"end\": 35, \"tag\": \"neutral\"}"
Example 3: 
input: "Cardamom futures fall 0.92 per cent on sluggish demand"
output: "{\"value\": \"Cardamom\", \"start\": 0, \"end\": 8, \"tag\": \"negative\"}"
Now please complete the task for the following input:\n""",
"""Identify companies or organizations in the text and classify their sentiment as 'Neutral', 'Positive', or 'Negative'. For each entity, provide its name, start and end indices, and sentiment tag.
Task outline:
Entity Identification: Extract company or organization names from the text.
Position Indices: Determine start and end indices of each entity.
Sentiment Classification: Assign a sentiment tag (Neutral, Positive, Negative) based on context.
I will give you some examples.
Example 1: 
input: "Gold dips on firmer equities; Middle East, Ukraine tensions eyed"
output: "{\"value\": \"Gold\", \"start\": 0, \"end\": 4, \"tag\": \"negative\"}"
Example 2: 
input: "200-DMA strong support for Nifty; index may bounce back to 6,200 levels"
output: "{\"value\": \"Nifty\", \"start\": 27, \"end\": 32, \"tag\": \"positive\"}"
Example 3: 
input: "Mumbai HC to hear govt's case against FTIL board on Wednesday"
output: "{\"value\": \"FTIL\", \"start\": 38, \"end\": 42, \"tag\": \"neutral\"}"
Now please complete the task for the following input:\n""",

"""Identify and classify the sentiment of companies or organizations in the text. For each entity, provide its name, start and end indices, and sentiment tag.
Task details:
Entity Recognition: Find and extract company or organization names.
Indexing: Provide the start and end indices for each entity.
Sentiment Analysis: Tag each entity with 'Neutral', 'Positive', or 'Negative' sentiment based on context.
I will give you some examples.
Example 1: 
input: "Infosys' March guidance for next fiscal is very crucial"
output: "{\"value\": \"Infosys\", \"start\": 0, \"end\": 7, \"tag\": \"neutral\"}"
Example 2: 
input: "Diageo makes $1.9 bn second open offer, USL surges 15%: Should investors tender shares"
output: "{\"value\": \"USL\", \"start\": 40, \"end\": 43, \"tag\": \"positive\"}\n{\"value\": \"Diageo\", \"start\": 0, \"end\": 6, \"tag\": \"neutral\"}"
Example 3: 
input: "10-year bond falls on profit-booking"
output: "{\"value\": \"10-year bond\", \"start\": 0, \"end\": 12, \"tag\": \"negative\"}"
Now please complete the task for the following input:\n""",

"""Extract company or organization names from the text and determine their sentiment ('Neutral', 'Positive', or 'Negative'). Include the entity's name, start and end indices, and sentiment tag in the output.
Steps:
Identify Entities: Locate and extract names of companies or organizations.
Mark Positions: Determine the start and end positions of each entity.
Classify Sentiment: Assign a sentiment label to each entity based on its context.
I will give you some examples.
Example 1: 
input: "Russian rouble slips as support from tax period fades"
output: "{\"value\": \"Russian rouble\", \"start\": 0, \"end\": 14, \"tag\": \"negative\"}"
Example 2: 
input: "Apollo Tyres Q1 net rises 37.36% to Rs 227.94 crore"
output: "{\"value\": \"Apollo Tyres\", \"start\": 0, \"end\": 12, \"tag\": \"positive\"}"
Example 3: 
input: "LIC's Rs 45,000 crore purchase exceeds 2014 infusion, accumulates tech and banking shares"
output: "{\"value\": \"tech\", \"start\": 66, \"end\": 70, \"tag\": \"positive\"}\n{\"value\": \"banking\", \"start\": 75, \"end\": 82, \"tag\": \"positive\"}\n{\"value\": \"LIC\", \"start\": 0, \"end\": 3, \"tag\": \"neutral\"}"
Now please complete the task for the following input:\n""",

]
SEntFiN_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Considering every sentence as a String in python, provide the entities with the start and end index to mark the boundaries of it including spaces and punctuation using zero-based indexing.
Do not give explanations for the sentiment. In the output,Tag means sentiment; value means entity name. If no entity is found in the sentence, the response should be empty. 
The sentence: \n"{input}"\nOutput:\n""",
]


SEntFiN_correct_templates = ["""Performing an Entity-Level Sentiment Analysis and Correction Task
Task Description
Given a financial text, determine whether each entity and its sentiment polarity match the actual context within the text. If the sentiment polarity is incorrect, provide the correct entity-sentiment pairs. Sentiment polarity can be positive, negative, or neutral.

Task Examples
Example 1: 
Sentence: Steady demand, rain woes push up Guar prices
Pseudo-labels: {{\"value\": \"Guar\", \"start\": 33, \"end\": 37, \"tag\": \"positive\"}}
Output: {{\"value\": \"Guar\", \"start\": 33, \"end\": 37, \"tag\": \"positive\"}}

Example 2:
Sentence: Kotak Mahindra top bet in banking sector; likely to hit Rs 1550 in one year: Gaurang Shah
Pseudo-labels: {{\"value\": \"Kotak\", \"start\": 0, \"end\": 5, \"tag\": \"positive\"}}
Output: {{\"value\": \"Kotak Mahindra\", \"start\": 0, \"end\": 14, \"tag\": \"positive\"}}\n{{\"value\": \"banking sector\", \"start\": 26, \"end\": 40, \"tag\": \"positive\"}}

Example 3:
Sentence: SKS scrip snaps losing streak, ends 3% up after rate reduction
Pseudo-labels: {{\"value\": \"SKS\", \"start\": 0, \"end\": 3, \"tag\": \"negative\"}}
Output: {{\"value\": \"SKS\", \"start\": 0, \"end\": 3, \"tag\": \"positive\"}}

Task Execution
Given Sentence: {content}
Pseudo-labels: {pre}

Is it correct?
If correct, please output the pseudo-labels.
If incorrect, please provide the correct answer:
Output:
""",]

SEntFiN_correct_icl_templates = ["""Performing an Entity-Level Sentiment Analysis and Correction Task
Task Description
Given a financial text, determine whether each entity and its sentiment polarity match the actual context within the text. If the sentiment polarity is incorrect, provide the correct entity-sentiment pairs. Sentiment polarity can be positive, negative, or neutral.

Task Examples
{example}
Task Execution
Given Sentence: {content}
Pseudo-labels: {pre}

Is it correct?
If correct, please output the pseudo-labels.
If incorrect, please provide the correct answer:
Output:
""",]
# 执行一项实体级情感分析判断与改正任务
# 任务描述：给定一段金融文本，请判断其中每一组金融实体及其情感极性是否符合文本中的真实情况。如发现不正确的情感极性，请给出你认为正确的所有实体情感对。情感极性包括：正面、负面和中立。
# 任务示例
# 示例一：
# 句子：
# 伪标签：
# 输出：
# 示例二：
# 句子：
# 伪标签：
# 输出：
# 示例三：
# 句子：
# 伪标签：
# 输出：
#
# 给定句子：input
# 伪标签：pre
# 是否正确？
# 如果正确，请输出伪标签。
# 如果不正确，输出正确的答案：
# 输出：


EFSA_icl_templates = [
'''Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
{example}
Now please complete the task for the following input:\n"{input}"\nOutput:\n''',
]
EFSA_fixicl_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Provide a sentiment polarity for each entity span appearing in the sentences in sequence. In the output, value means entity name, provide the entities with the start and end index to mark the boundaries of it, Tag means sentiment. I will give you some examples.
Example 1: 
input: "\"For the moment, disruptions to oil supply are taking a back seat to concerns of weaker demand,\" ANZ analysts said in a note."
output: "{\"value\": \"ANZ\", \"start\": 97, \"end\": 100, \"tag\": \"Neutral\"}"
Example 2: 
input: "An official at a large Hyundai supplier who has spoken to senior officials at the company told Reuters that the automaker was caught off guard by the law. "
output: "{\"value\": \"Hyundai\", \"start\": 23, \"end\": 30, \"tag\": \"Negative\"}\n{\"value\": \"Reuters\", \"start\": 95, \"end\": 102, \"tag\": \"Neutral\"}"
Example 3: 
input: "Banks <.SPXBK>, which tend to benefit from a rising rate environment, gained 2.1%. Healthcare stocks <.SPXHC> got a boost from health insurer Humana Inc's <HUM.N> strong earnings forecast. "
output: "{\"value\": \"Banks\", \"start\": 0, \"end\": 5, \"tag\": \"Positive\"}\n{\"value\": \"Healthcare stocks\", \"start\": 83, \"end\": 100, \"tag\": \"Positive\"}\n{\"value\": \"Humana Inc\", \"start\": 142, \"end\": 152, \"tag\": \"Positive\"}"
Now please complete the task for the following input:\n""",
]
EFSA_templates = [
"""Identify the entities which are companies or organizations from the following content and classify the sentiment of the corresponding entities into ‘Neutral’, ‘Positive’, or ‘Negative’ classes. 
Considering every sentence as a String in python, provide the entities with the start and end index to mark the boundaries of it including spaces and punctuation using zero-based indexing.
Do not give explanations for the sentiment. In the output,Tag means sentiment; value means entity name. If no entity is found in the sentence, the response should be empty. 
The sentence: \n"{input}"\nOutput:\n""",
]













aspe_icl_templates = [
'''Now let's do an ASPE (Aspect-Sentiment Pair Extraction) task. Task definition: The output will be the aspects (clearly appear in the text) and the aspects sentiment polarity (positive, neutral, negative). I will give you some example.

{example}
Now please complete the ASPE task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASPE (Aspect-Sentiment Pair Extraction) task. Task definition: Your aim is to identify explicit aspects and determine their sentiment polarity (positive, neutral, negative). For clarity, here are some examples:

{example}
Now, using the above examples as guidance, perform the ASPE task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASPE task (Aspect-Sentiment Pair Extraction). Here's what you need to do: Extract aspects, and determine their sentiment polarities, which can be positive, neutral, or negative. I've provided some examples to guide you:

{example}
Using the examples as a reference, apply the ASPE procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASPE (Aspect-Sentiment Pair Extraction) task. Your objective is to extract aspects, and categorize their sentiment polarities as positive, neutral, or negative. Here are some instances for your reference:

{example}
Keeping the examples as a baseline, evaluate the next input via the ASPE procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''For the ASPE task, identify aspects and their sentiment polarities (positive, neutral, negative). Consider these examples to grasp the essence:

{example}
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASPE (Aspect-Sentiment Pair Extraction). The goal is to detect aspects and their sentiment polarities which can be either positive, negative, or neutral. Some examples you can learn for reference are below:

{example}
Ready? Let's apply this to the sentence below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment pair extraction task: locate and extract explicit aspects mentioned in the sentence and classify their sentiment as either positive, negative, or neutral. Provide both the aspect and its corresponding sentiment polarity. Refer to the example below:

{example}
Now, tackle the following input:\n"{input}",Can you tell me what your results are?\n''',

'''I need you to do an ASPE (Aspect-Sentiment Pair Extraction) task. The goal is to extract aspects and their corresponding sentiment polarities (positive, neutral, negative). Here are some examples:

{example}
Now, based on the examples and its format, evaluate the following sentence:\n"{input}"\nThe ASPE task results:\n''',

'''I'm feeling overwhelmed with an ASPE (Aspect-Sentiment Pair Extraction) task. Can you pitch in and help? The task is aimed at extracting aspects and their corresponding sentiment polarities from the given sentences. Aspects will be explicitly mentioned, and sentiment polarities can only be positive, negative, or neutral. Here are some templates you can refer to:

{example}
Now, I'm handing this task over to you. The input sentences are:\n"{input}"\nWhat are your results?\n''',

'''Could you please lend me a hand with an ASPE (Aspect-Sentiment Pair Extraction) task? The task's goal is to find and extract aspects explicitly mentioned in the sentence, and then determine their associated sentiment polarities as positive, negative, or neutral. Report both the aspect and its sentiment polarity. I will give you some templates to learn how to extract.

{example}
Now, it's your show time. The input sentences are:\n"{input}"\nWhat is your output?\n'''
]

aspe_templates = [
'''Now let's do an ASPE (Aspect-Sentiment Pair Extraction) task. Task definition: The output will be the aspects (clearly appear in the text) and the aspects sentiment polarity (positive, neutral, negative).
Now please complete the ASPE task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASPE (Aspect-Sentiment Pair Extraction) task. Task definition: Your aim is to identify explicit aspects and determine their sentiment polarity (positive, neutral, negative).
Now, using the above examples as guidance, perform the ASPE task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASPE task (Aspect-Sentiment Pair Extraction). Here's what you need to do: Extract aspects, and determine their sentiment polarities, which can be positive, neutral, or negative.
Using the examples as a reference, apply the ASPE procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASPE (Aspect-Sentiment Pair Extraction) task. Your objective is to extract aspects, and categorize their sentiment polarities as positive, neutral, or negative.
Keeping the examples as a baseline, evaluate the next input via the ASPE procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''For the ASPE task, identify aspects and their sentiment polarities (positive, neutral, negative).
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASPE (Aspect-Sentiment Pair Extraction). The goal is to detect aspects and their sentiment polarities which can be either positive, negative, or neutral.
Ready? Let's apply this to the sentence below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment pair extraction task: locate and extract explicit aspects mentioned in the sentence and classify their sentiment as either positive, negative, or neutral. Provide both the aspect and its corresponding sentiment polarity.
Now, tackle the following input:\n"{input}",Can you tell me what your results are?\n''',

'''I need you to do an ASPE (Aspect-Sentiment Pair Extraction) task. The goal is to extract aspects and their corresponding sentiment polarities (positive, neutral, negative).
Now, based on the examples and its format, evaluate the following sentence:\n"{input}"\nThe ASPE task results:\n''',

'''I'm feeling overwhelmed with an ASPE (Aspect-Sentiment Pair Extraction) task. Can you pitch in and help? The task is aimed at extracting aspects and their corresponding sentiment polarities from the given sentences. Aspects will be explicitly mentioned, and sentiment polarities can only be positive, negative, or neutral.
Now, I'm handing this task over to you. The input sentences are:\n"{input}"\nWhat are your results?\n''',

'''Could you please lend me a hand with an ASPE (Aspect-Sentiment Pair Extraction) task? The task's goal is to find and extract aspects explicitly mentioned in the sentence, and then determine their associated sentiment polarities as positive, negative, or neutral. Report both the aspect and its sentiment polarity.
Now, it's your show time. The input sentences are:\n"{input}"\nWhat is your output?\n'''
]

aste_icl_templates = [
'''Now let's do an ASTE (Aspect-Sentiment Triple Extraction) task. Task definition: The output will be the aspects (clearly appear in the text), the aspects opinion (may not be present in the text, if not be present, please replace it with 'NULL'), and the aspects sentiment polarity (positive, neutral, negative). I will give you some examples.

{example}
Now please complete the ASTE task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASTE (Aspect-Sentiment Triple Extraction) task. Task definition: Your aim is to identify explicit aspects, extract the opinions of the aspects (if not exist in the sentence, please replace the position with 'NULL'), and determine their sentiment polarity (positive, neutral, negative). For clarity, here are some examples:

{example}
Now, using the above examples as guidance, perform the ASTE task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASTE (Aspect-Sentiment Triple Extraction) task. Here's what you need to do: Extract aspects, identify the opinions corresponding to the aspects (if not exist, can be implicitly represented as 'NULL'), and determine their sentiment polarity, which can be positive, neutral, or negative. I've provided some examples to guide you:

{example}
Using the examples as a reference, apply the ASTE procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASTE (Aspect-Sentiment Triple Extraction) task. Your objective is to extract aspects, find the opinions of these aspects (if can't find, you can represent them as 'NULL'), and categorize their sentiment polarity as positive, neutral, or negative. Here are some instances for your reference:

{example}
Keeping the examples as a baseline, evaluate the next input via the ASTE procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''Now, let's begin an ASTE task, for ASTE task, you need to identify aspects, opinions (you can replace them with 'NULL' if you can't), and their sentiment polarity (positive, neutral, negative). Consider these examples to grasp the essence:

{example}
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASTE (Aspect-Sentiment Triple Extraction). The goal is to detect explicit aspects, opinions (please replace with 'NULL' if can't), and their sentiment polarities (positive, neutral, negative) from given sentences. Some examples are below:

{example}
Ready? Let's apply this to the sentences below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment triple extraction task: Extract fine-grained aspects, opinions (you can replace them with 'NULL' if not be present), and their respective sentiment polarities (positive, neutral, negative) from the sentences. Be attentive to nuanced aspect-opinion pairs and ensure the sentiment polarities' accuracy. You can refer to the example below:

{example}
Now, tackle the following input:\n"{input}"\nPlease give me your output''',

'''I need you to do an ASTE (Aspect-Sentiment Triple Extraction) task. The goal is to extract aspects, the opinion of each of them (if not exist, please replace it with 'NULL'), and their sentiment polarity (positive, neutral, negative). Here are some examples you can learn:

{example}
Now, based on the examples and its format, evaluate the following sentence:\n"{input}"\nThe ASTE task results:\n''',

'''Suppose you are a researcher in the field of NLP actively tackling the ASTE (Aspect-Sentiment Triple Extraction) task. Your task is to extract the aspects from the given sentences and their corresponding opinions and sentiment polarities (positive, neutral, negative). Be attentive to replace opinion's position with 'NULL' if cannot detect. Below are some templates for your reference:

    {example}
Now, you have learned the provided templates, please start tackling the given sentences! The pending sentences are below:\n"{input}"\nWhat is your output\n''',

'''I need you to help me complish an ASTE (Aspect-Sentiment Triple Extraction) task. Next, you need to extract aspects and corresponding opinions from sentences, meanwhile, ensure that the sentiment polarity (positive, neutral, negative) is accurately labeled for each opinion. If an aspect lacks an opinion, use 'NULL' to replace the opinion. Here are some templates you can learn:

{example}
Next, please begin your task based on the templates provided above. The sentences you input are:\n"{input}"\nplease tell me what is your output?\n''',

'''I am working on an ASTE task in the NLP field, and I need your assistance.Please help me extract the aspect, corresponding opinion (use "NULL" if no opinion is expressed), and assign one of the sentiment polarities: "positive," "negative," or "neutral" for each given sentence. Ensure that you include all aspects, even if their corresponding opinions are empty, and consider the three sentiment polarities only: positive, negative, and neutral. Next, I will provide you with some examples for your reference.

{example}
Now, please begin, the sentences input are:\n"{input}" what are your results?\n''',

'''Hello, I need you! your task is to extract aspects, opinions (use "NULL" if no opinion exists), and assign sentiment polarities ("positive," "negative," or "neutral") for each sentence provided. Please ensure that all aspects are identified, even if their corresponding opinions are empty, and limit the sentiment polarities to positive, negative, and neutral. Some templates are below:

{example}
Now, it's your show time, the sentences input are:\n"{input}" please give me your output\n'''
]

aste_templates = [
'''Now let's do an ASTE (Aspect-Sentiment Triple Extraction) task. Task definition: The output will be the aspects (clearly appear in the text), the aspects opinion (may clear appear or not be present in the text, if not be present, please replace it with 'NULL'), and the aspects sentiment polarity (positive, neutral, negative).
Now please complete the ASTE task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASTE (Aspect-Sentiment Triple Extraction) task. Task definition: Your aim is to identify explicit aspects, extract the opinions of the aspects (if not exist in the sentence, please replace the position with 'NULL'), and determine their sentiment polarity (positive, neutral, negative).
Now, using the above examples as guidance, perform the ASTE task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASTE (Aspect-Sentiment Triple Extraction) task. Here's what you need to do: Extract aspects, identify the opinions corresponding to the aspects (if not exist, can be implicitly represented as 'NULL'), and determine their sentiment polarity, which can be positive, neutral, or negative.
Using the examples as a reference, apply the ASTE procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASTE (Aspect-Sentiment Triple Extraction) task. Your objective is to extract aspects, find the opinions of these aspects (if can't find, you can represent them as 'NULL'), and categorize their sentiment polarity as positive, neutral, or negative.
Keeping the examples as a baseline, evaluate the next input via the ASTE procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''Now, let's begin an ASTE task, for ASRE task, you need to identify aspects, opinions (you can replace them with 'NULL' if you can't), and their sentiment polarity (positive, neutral, negative).
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASTE (Aspect-Sentiment Triple Extraction). The goal is to detect explicit aspects, opinions (please replace with 'NULL' if can't), and their sentiment polarities (positive, neutral, negative) from given sentences.
Ready? Let's apply this to the sentences below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment triple extraction task: Extract fine-grained aspects, opinions (you can replace them with 'NULL' if not be present), and their respective sentiment polarities (positive, neutral, negative) from the sentences. Be attentive to nuanced aspect-opinion pairs and ensure the sentiment polarities' accuracy.
Now, tackle the following input:\n"{input}"\nPlease give me your output''',

'''I need you to do an ASTE (Aspect-Sentiment Triple Extraction) task. The goal is to extract aspects, the opinion of each of them (if not exist, please replace it with 'NULL'), and their sentiment polarity (positive, neutral, negative).
Now, based on the examples and its format, evaluate the following sentence:\n"{input}"\nThe ASTE task results:\n''',

'''Suppose you are a researcher in the field of NLP actively tackling the ASTE (Aspect-Sentiment Triple Extraction) task. Your task is to extract the aspects from the given sentences and their corresponding opinions and sentiment polarities (positive, neutral, negative). Be attentive to replace opinion's position with 'NULL' if cannot detect.
Now, you have learned the provided templates, please start tackling the given sentences! The pending sentences are below:\n"{input}"\nWhat is your output?\n''',

'''I need you to help me complish an ASTE (Aspect-Sentiment Triple Extraction) task. Next, you need to extract aspects and corresponding opinions from sentences, meanwhile, ensure that the sentiment polarity (positive, neutral, negative) is accurately labeled for each opinion. If an aspect lacks an opinion, use 'NULL' to replace the opinion.
Next, please begin your task based on the templates provided above. The sentences you input are:\n"{input}"\nplease tell me what is your output?\n''',

'''I am working on an ASTE task in the NLP field, and I need your assistance.Please help me extract the aspect, corresponding opinion (use "NULL" if no opinion is expressed), and assign one of the sentiment polarities: "positive," "negative," or "neutral" for each given sentence. Ensure that you include all aspects, even if their corresponding opinions are empty, and consider the three sentiment polarities only: positive, negative, and neutral.
Now, please begin, the sentences input are:\n"{input}" what are your results?\n''',

'''Hello, I need you! your task is to extract aspects, opinions (use "NULL" if no opinion exists), and assign sentiment polarities ("positive," "negative," or "neutral") for each sentence provided. Please ensure that all aspects are identified, even if their corresponding opinions are empty, and limit the sentiment polarities to positive, negative, and neutral.
Now, it's your show time, the sentences input are:\n"{input}" please give me your output\n'''
]

asqp_icl_templates = [
'''Now let's do an ASQP (Aspect-Sentiment Quad Prediction) task. Task definition: The output will be the aspects along with their corresponding categories, opinions, and sentiment polarities (positive, neutral, negative). But you need to pay attention to two points: Firstly, Aspect and Opinion may not appear in the sentences, in such cases, please replace them with 'NULL'. Secondly, the determination of the Category should be chosen from the given set of categories, and you should learn the category set from the provided examples. Some examples are below.

{example}
Now please complete the ASQP task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASQP (Aspect-Sentiment Quad Prediction) task. Task definition: Your aim is to identify aspects (if the sentence does not contain it, please replace it with NULL) and determine their categories (you need to learn how to determine the category from the given examples.), opinions (if the sentence does not contain it, please replace it with NULL) and sentiment polarities (positive, neutral, negative). For clarity, here are some examples:

{example}
Now, using the above examples as guidance, perform the ASQP task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASQP (Aspect-Sentiment Quad Prediction) task. Here's what you need to do: Extract aspects (if not exist, can be implicitly represented as 'NULL'), identify categories (you should learn the set of categories from given examples) and opinions (if not exist, can be implicitly represented as 'NULL') corresponding to the aspects, and determine their sentiment polarity, which can be positive, neutral, or negative. I've provided some examples to guide you:

{example}
Using the examples as a reference, apply the ASQP procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASQP (Aspect-Sentiment Quad Prediction) task. Your objective is to extract aspects, categorize the aspects based on the provided examples, find the opinions of these aspects (if can't find, you can represent them as 'NULL'), and classify their sentiment polarities as positive, neutral, or negative. Here are some instances for your reference:

{example}
Keeping the examples as a baseline, evaluate the next input via the ASQP procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''For the ASQP task, identify aspects (you can replace them with 'NULL' if you can't), categories (you should chose one of categories which learn from given examples), opinions (you can replace them with 'NULL' if you can't), and their sentiment polarity (positive, neutral, negative). Consider these examples to grasp the essence:

{example}
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASQP (Aspect-Sentiment Quad Prediction). The goals are below: 
1. Aspect Extraction: Identify aspects or entities mentioned in the sentence. If no aspect is present, use "NULL" to indicate its absence.
2. Category Assignment: Determine the category associated with each identified aspect. The category set should be learned from the provided template examples.
3. Opinion Extraction: Detect any opinions expressed in the sentence related to the identified aspects. If no opinion is expressed, replace it with "NULL."
4. Sentiment Polarity Assignment: Assign one of three sentiment polarities—positive, negative, or neutral—to each opinion identified.
There are some examples for your learning:

{example}
Ready? Let's apply this to the sentences below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment quadruple extraction task:
1.Aspect Extraction: Identify aspects/entities, using "NULL" if none are present.
2.Category Assignment: Determine categories for each aspect from provided templates.
3.Opinion Extraction: Detect opinions, replacing with "NULL" if absent.
4.Sentiment Polarity: Assign sentiment polarity (positive, negative, neutral) to each opinion.
Ensure your annotations cover all aspects of the sentence following guidelines.
Refer to the examples below, you can learn and draw inspiration.

{example}
Now, tackle the following input:\n"{input}"\nPlease give me your output''',

'''Suppose you are a researcher in the field of NLP actively tackling the ASQP (Aspect-Sentiment Quad Prediction) task. Your task is to extract the aspects from the given sentences and their corresponding categories, opinions and sentiment polarities (positive, neutral, negative). However, please be mindful of the following: 
Firstly, aspects and opinions may not always be present in the sentences. If they are missing, use 'NULL' to replace the aspect or opinion. 
Secondly, the categories for aspects come from a predefined set, but this set needs to be learned from the provided template examples.
Below are some templates for your reference:

{example}
Now, you have learned the provided templates, please start tackling the given sentences! The pending sentences are below:\n"{input}"\nWhat is your output?\n'''
]

asqp_templates = [
'''Now let's do an ASQP (Aspect-Sentiment Quad Prediction) task. Task definition: The output will be the aspects along with their corresponding categories, opinions, and sentiment polarities (positive, neutral, negative). But you need to pay attention to one point: Aspect and Opinion may not appear in the sentences, in such cases, please replace them with 'NULL'.
Now please complete the ASQP task for the following input:\n"{input}"\nOutput:\n''',

'''Now let's do an ASQP (Aspect-Sentiment Quad Prediction) task. Task definition: Your aim is to identify aspects (if the sentence does not contain it, please replace it with NULL) and determine their categories (you need to infer which category each fine-grained aspect belongs to on your own), opinions (if the sentence does not contain it, please replace it with NULL) and sentiment polarities (positive, neutral, negative).
Now, using the above examples as guidance, perform the ASQP task for the sentence below:\n"{input}"\nOutput:\n''',

'''Let's dive into the ASQP (Aspect-Sentiment Quad Prediction) task. Here's what you need to do: Extract aspects (if not exist, can be implicitly represented as 'NULL'), identify categories (you should deduce the category for each fine-grained aspect yourself) and opinions (if not exist, can be implicitly represented as 'NULL') corresponding to the aspects, and determine their sentiment polarity, which can be positive, neutral, or negative.
Using the examples as a reference, apply the ASQP procedure to the following input:\n"{input}"\nOutput:\n''',

'''It's time for the ASQP (Aspect-Sentiment Quad Prediction) task. Your objective is to extract aspects, categorize the aspects based on you common sense, find the opinions of these aspects (if can't find, you can represent them as 'NULL'), and classify their sentiment polarities as positive, neutral, or negative.
Keeping the examples as a baseline, evaluate the next input via the ASQP procedure:\n"{input}"\nPlease give the extraction results:\n''',

'''For the ASQP task, identify aspects (you can replace them with 'NULL' if you can't), categories (you need to deduce on your own which category each fine-grained aspect belongs to), opinions (you can replace them with 'NULL' if you can't), and their sentiment polarity (positive, neutral, negative).
Now, based on the understanding, evaluate the following sentence:\n"{input}"\nOutput:\n''',

'''Your next task is ASQP (Aspect-Sentiment Quad Prediction). The goals are below: 
1. Aspect Extraction: Identify aspects or entities mentioned in the sentence. If no aspect is present, use "NULL" to indicate its absence.
2. Category Assignment: Determine the category associated with each identified aspect. However, the category set needs to be formulated by you based on your own common sense.
3. Opinion Extraction: Detect any opinions expressed in the sentence related to the identified aspects. If no opinion is expressed, replace it with "NULL."
4. Sentiment Polarity Assignment: Assign one of three sentiment polarities—positive, negative, or neutral—to each opinion identified.
Ready? Let's apply this to the sentences below:\n"{input}"\nGive me your output:\n''',

'''Help me complete an aspect sentiment quadruple extraction task:
1.Aspect Extraction: Identify aspects/entities, using "NULL" if none are present.
2.Category Assignment: Determine categories for each aspect from your common sense.
3.Opinion Extraction: Detect opinions, replacing with "NULL" if absent.
4.Sentiment Polarity: Assign sentiment polarity (positive, negative, neutral) to each opinion.
Ensure your annotations cover all aspects of the sentence following guidelines.
Now, tackle the following input:\n"{input}"\nPlease give me your output''',

'''Suppose you are a researcher in the field of NLP actively tackling the ASQP (Aspect-Sentiment Quad Prediction) task. Your task is to extract the aspects from the given sentences and their corresponding categories, opinions and sentiment polarities (positive, neutral, negative). However, please be mindful of the following: 
Firstly, aspects and opinions may not always be present in the sentences. If they are missing, use 'NULL' to replace the aspect or opinion. 
Secondly, the categories for aspects come from a predefined set, but the category set needs to be defined by you based on your own knowledge.
Now, you have learned the provided templates, please start tackling the given sentences! The pending sentences are below:\n"{input}"\nWhat is your output?\n'''
]