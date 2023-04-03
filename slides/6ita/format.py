import re
import mistune
import os

def read_file(input_file_path):
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            print(f"path: {input_file_path}")
            content = file.read()
            print(content)
        return content
    except FileNotFoundError:
        print("文件未找到，请检查路径是否正确。")
        return None
    except Exception as e:
        print(f"读取文件时出错：{e}")
        return None

def write_to_file(output_file_path, content):
    try:
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"文件已成功写入：{output_file_path}\n内容如下:\n{content}")
    except Exception as e:
        print(f"写入文件时出错：{e}")

def get_output_file_path(input_file_path):
    file_name, _ = os.path.splitext(input_file_path)
    return f"{file_name}.html"

def convert_to_markdown(lines):
    markdown_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 第一种文本块：单行文本
        if not line.startswith('1'):
            if line:
                markdown_lines.append(f"<!-- Lecture: {line} -->\n")
            else:
                markdown_lines.append("\n")

        # 第二种文本块：双行文本
        elif i + 2 < len(lines) and not lines[i + 2].strip().startswith('1'):
            img_title = line
            img_alt = lines[i + 1].strip()
            markdown_lines.append(f"![{img_alt}]()\n")
            markdown_lines.append(f"#### {img_title}\n")
            i += 2  # 跳过已处理的行

            # 添加空行
            markdown_lines.append("\n")

        # 第三种文本块：多行文本
        else:
            title = line
            markdown_lines.append(f"### {title}\n")
            i += 1

            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('1'):
                markdown_lines.append(f"- {lines[i].strip()}\n")
                i += 1

            # 添加空行
            markdown_lines.append("\n")

        i += 1

    return ''.join(markdown_lines)


def convert_to_html(markdown_lines, first_data_rel_to):
    # 将 Markdown 转换为 HTML
    markdown = mistune.create_markdown(renderer=mistune.HTMLRenderer())
    html_lines = markdown(markdown_lines).split('\n')

    # 用于存储生成的 div 元素
    divs = []
    current_id = 0
    current_div_id = f"a{current_id}"
    data_rel_to = first_data_rel_to

    first_div = True

    # 遍历 HTML 内容
    for line in html_lines:
        if line.strip():
            if line.startswith("<!--"):
                # 将注释放在 div 标签之外
                divs.append(line)
            else:
                # 创建一个新的 div 元素
                div = f"""
    <div
        id            = "{current_div_id}"
        class         = "step markdown"
        data-rel-to   = "{data_rel_to}"
        data-rel-x    = "0"
        data-rel-y    = "0"
        data-rel-z    = "0"
        data-rotate-x = "0"
        data-rotate-y = "0"
        data-rotate-z = "0"
        data-scale    = "2">
    {line}
    </div>
    """
                divs.append(div)

                # 更新 id 和 data_rel_to
                current_id += 1
                current_div_id = f"a{current_id}"
                if not first_div:
                    data_rel_to = f"a{current_id - 1}"
                first_div = False
        else:
            divs.append(line)

    return "\n".join(divs)

def convert_file_to_html(input_file_path, output_file_path):
    # 读取输入文件
    raw_content = read_file(input_file_path)
    if raw_content is None:
        return

    # 将文本块转换为 Markdown
    markdown_content = convert_to_markdown(raw_content.splitlines())

    # 提取第一个 div 的 data-rel-to 值
    first_data_rel_to = f"c{markdown_content.split(' ')[0]}{markdown_content.split('.')[1][0]}t"
    
    # 将转换后的 Markdown 内容写入输出文件
    markdown_output_path = os.path.splitext(input_file_path)[0] + ".md"
    write_to_file(markdown_output_path, markdown_content)
    
    # 提取第一个 div 的 data-rel-to 值
    first_data_rel_to = f"c{markdown_content.split(' ')[0]}{markdown_content.split('.')[1][0]}t"

    # 将 Markdown 转换为 HTML
    html_content = convert_to_html(markdown_content, first_data_rel_to)
    
    # 将转换后的内容写入输出文件
    write_to_file(output_file_path, html_content)

print("程序开始运行...")

input_file_path = input("请输入要转换的文本文件路径：").strip()

output_file_path = get_output_file_path(input_file_path)

convert_file_to_html(input_file_path, output_file_path)

