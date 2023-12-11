# reads a text file containing some English text and replace special symbol
f =open('text.txt','r')
text = f.read()
text = text.replace(',','').replace('.','')
word=text.split()

# count text with at least 4 letters long and start with a capital letter or are all capitalized
word_count = 0
for a in word:
  if len(a)>=4 and str.isupper(a) or str.istitle(a):
    word_count += 1
print(word_count)

# Print a list of those words and the number of their occurrences
word_dic={}
for i in word:
    if len(i) >= 4 and str.isupper(i) or str.istitle(i):
        if i in word_dic.keys():
            word_dic[i] += 1
        else:
            word_dic[i] = 1
print(word_dic)

# sort list then get top 10 words
w = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
top_10 = w[:10]
print(top_10)

# Use matplotlib or plotly and generate a bar chart
import matplotlib.pyplot as plt
words,counts =zip(*top_10)
plt.bar(words, counts, color = 'orange')
plt.show()

# wordcloud for whole text
import wordcloud
wc = wordcloud.WordCloud(background_color='white')
wc.generate(text)
wc.to_file('wordcloud_fulltext.png')

# wordcloud with applying conditions 1a and 1b
wa = wordcloud.WordCloud(background_color='white')
wa.generate_from_frequencies(word_dic)
wa.to_file('wordcloud_condition.png')
