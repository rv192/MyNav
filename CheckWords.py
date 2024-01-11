# 从文件中读取words.txt和story.txt的内容
with open('words.txt', 'r', encoding='utf-8') as words_file:
    # 读取words.txt的内容，并只保留词汇部分
    words = [line.split()[0] for line in words_file.read().splitlines()]

with open('story.txt', 'r', encoding='utf-8') as story_file:
    story = story_file.read()

# 定义一个函数，用于检查词汇是否在故事中被使用（忽略大小写），并返回被用到的词汇和序号
def find_used_words(story, words):
    used_words = {}
    story_lower = story.lower()  # 将故事内容转换为小写以进行大小写不敏感的匹配
    for word in words:
        if word.lower() in story_lower:
            index = story_lower.index(word.lower())
            used_words[word] = index
    return used_words

# 调用函数获取被使用的词汇和其序号
used_words = find_used_words(story, words)

# 在output.md中输出整篇文章内容，用到的词汇加粗显示
with open('output.md', 'w', encoding='utf-8') as output_file:
    output_file.write("### 整篇文章内容\n")
    story_with_highlight = story
    for word in used_words.keys():
        story_with_highlight = story_with_highlight.lower().replace(word.lower(), f'**{word} ({words.index(word) + 1})**')
    output_file.write(story_with_highlight)

    output_file.write("\n\n### 用到的词汇\n")
    for word, index in used_words.items():
        output_file.write(f'- {word} ({words.index(word) + 1})\n')

# 找到未用到的词汇
unused_words = set(words) - set(used_words.keys())

# 在output.md中输出未用到的词汇
with open('output.md', 'a', encoding='utf-8') as output_file:
    output_file.write("\n### 未用到的词汇\n")
    for word in unused_words:
        output_file.write(f'- {word} ({words.index(word)+ 1})\n')

print("处理完成，结果已保存到output.md文件中。")
