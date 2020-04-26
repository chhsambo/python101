f1 = open('test.txt', encoding='utf-8')
# mode='r' => Read
# mode='w' => Write
# mode='a' => Append
# mode='w+' => Write & Read
# mode='a+' => Append & Read
# mode='x' => Create file (if file already exist error)

# print(f1)
# text = f1.read()

# print(text)
# How many lines in this text
# How many words in this text

f1.close()

with open('test.txt', encoding='utf-8') as f1:
    text = f1.read()

print(text)