import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, I am Rohit Kumar"
tokens = enc.encode(text)

print("Tokens:", tokens)

tokens = [13225, 11, 357, 939, 65416, 278, 70737]
decoded = enc.decode(tokens)

print("Decoded Text:", decoded)

text = "Hello, I am Kumar Rohit"
tokens = enc.encode(text)

print("Tokens new:", tokens)

tokens = [13225, 11, 357, 939, 70737, 65416, 278]
decoded = enc.decode(tokens)

print("Decoded Text:", decoded)

