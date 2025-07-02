prompt styles for LLM

ALPACA
CHATML
INST

when we chat with a model, the input and output is cached, for further communications and it charges cached tokens at a separate price. whch is lower than input tokens price and output tokens price as well.
this cache is at backend of openai.

if the nr of messages grow to 500, summary of last 400 and latest 100 messages is snet..

