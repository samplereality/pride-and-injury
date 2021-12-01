import translators as ts
import time

# Gots to get me the novel (text comes from the Project Gutenberg version)
with open('pride_and_prejudice_complete.txt') as f:
  novel = f.read()
  f.close

# It's a big novel! Can't translate all at once without breaking things! Will do it a paragraph at a time.
paragraphs = novel.split('\n\n')

# Now create a loop for the 2169 paragraphs. 
# Each paragraph will be translated four times (English > Chinese > Russian > Portuguese > English) and then saved to a new file
# Let's alternate between the Google and Alibaba APIs

start = 0 # inclusive, so it starts with this number
end = 2169 # not inclusive, so it will stop before this number
sleep = 90 # slow down the pace so I don't get booted from the translation APIs

for i in range(start,end):
    with open('pride-translated.txt', 'a') as f:
        paragraph_original = paragraphs[i]
        paragraph_translated = (ts.alibaba(paragraph_original, from_language='auto', to_language='zh', sleep_seconds=sleep))
        paragraph_translated = (ts.google(paragraph_translated, from_language='auto', to_language='ru', sleep_seconds=sleep))
        paragraph_translated = (ts.alibaba(paragraph_translated, from_language='auto', to_language='pt', sleep_seconds=sleep))
        paragraph_translated = (ts.google(paragraph_translated, from_language='auto', to_language='en', sleep_seconds=sleep))
        f.write(paragraph_translated + '\n\n')
        with open('pride-paragraph-count.txt', 'a') as f2:
          f2.write("Paragraph " + str(i) + " Completed\n")
          f2.close
        print("Paragraph " + str(i))
        f.close
        time.sleep(sleep)
