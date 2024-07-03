import os
import re

# 获取当前文件夹路径
current_directory = os.path.dirname(os.path.realpath(__file__))

# 定义一个函数来处理单个文件
def process_file(file_path):
    print(f"Processing file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取 YAML Front Matter 和正文
    match = re.match(r'---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        print("No YAML Front Matter found. Skipping file.")
        return

    yaml_content = match.group(1)
    body_content = match.group(2)

    # 提取 title 字段
    title_match = re.search(r'(title:\s*")(.*)(")', yaml_content)
    if not title_match:
        print("No title found in YAML Front Matter. Skipping file.")
        return

    full_title = title_match.group(2).strip()
    
    # 去除重复的部分
    title_parts = full_title.split(' ')
    seen = set()
    cleaned_title_parts = []
    for part in title_parts:
        if part not in seen:
            cleaned_title_parts.append(part)
            seen.add(part)
    cleaned_title = ' '.join(cleaned_title_parts)

    # 修改 YAML Front Matter 中的 title 字段
    new_yaml_content = re.sub(r'(title:\s*")(.*)(")', r'\1' + cleaned_title + r'\3', yaml_content)

    # 组合新的文件内容
    new_content = f'---\n{new_yaml_content}\n---\n{body_content}'

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Updated title in file: {file_path}")

# 处理当前文件夹中的所有 Markdown 文件
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith('review.md'):
            process_file(os.path.join(root, file))

