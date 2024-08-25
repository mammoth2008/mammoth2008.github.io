# HTML Generator
# Used to generate HTML slides from formatted Markdown documents.
# Manual adjustments to page layout and the content of the last page are required.
# V1.0
# 2023.06.22 WITH ChatGPT

# TODO

import os
import re

class HTMLGenerator:

    def __init__(self, markdown_file):
        self.markdown_file = markdown_file
        self.html_file = markdown_file.replace(".md", ".html")
        self.header = open("header.html", "r").read()
        self.footer = open("../sh/footer.html", "r").read()
        self.div_blocks = []
        self.div_id_counter = 1  # 用于追踪当前的div id，从1开始计数
        self.header_processed = False  # Add this line
        self.section = None
        self.chapter_number = None
        self.section_number = None
        self.nav_questions = ""

    def get_div_id(self, div_block):
        """使用正则表达式从 div 块中提取 id"""
        match = re.search(r'id\s*=\s*"([^"]*)"', div_block)
        return match.group(1) if match else None

    def identify_block_type(self, block):
        """Distinguish different types of content blocks"""
        # Remove blank lines within the block
        lines = [line for line in block.split('\n') if line.strip() != '']
        if not lines:  # If there are no lines left after removing blank lines, return 'unknown'
            return 'unknown'
        elif lines[0].startswith("### "):
            return 'list'
        elif lines[0].startswith("!["):
            # Check if there are at least two lines and the second line starts with "#### "
            if len(lines) > 1 and lines[1].startswith("#### "):
                return 'image_with_title'
            else:
                return 'image'
        elif block.startswith("    "):  # Start with 4 spaces
            return 'code'
        elif lines[0].startswith("$$") and lines[-1].endswith("$$"):  # Add a condition to identify equation blocks
            return 'equation'
        else:
            return 'unknown'  # Return 'unknown' for all other cases

    def process_div_block(self, block):
        """处理不同类型的内容块"""
        block_type = self.identify_block_type(block)
        if block_type == 'header':
            self.process_header(block)
        elif block_type == 'list':
            self.process_list(block)
        elif block_type == 'image_with_title':
            self.process_image_with_title(block)
        elif block_type == 'image':
            self.process_image(block)
        elif block_type == 'code':
            self.process_code(block)
        elif block_type == 'equation':
            self.process_equation(block)
        elif block_type == 'unknown':
            print("Unknown block type")

    def process_header(self, block):
        print("Processing header...")
        with open(self.markdown_file, 'r') as f:
            lines = f.readlines()

        chapter = lines[0].strip()
        self.section = lines[1].strip()

        # Extract chapter and section numbers
        self.chapter_number = chapter.split('.')[0]
        self.section_number = self.section.split('.')[1].split(' ')[0] # get only the section number, not the title

        # Create div block
        div_block = f'''    <div 
    id         = "c{self.chapter_number}{self.section_number}t"
    class      = "step"
    data-x     = "0"
    data-y     = "0"
    data-z     = "0"
    data-scale = "5">

    <!-- 修改标题 -->
        <h2>{chapter}</h2>
        <h3 style="text-align: center">{self.section}</h3>
        <p class="footnote">
            <inlinecode style="font-size: 16px">
            Powered by 
            </inlinecode>
                <a href="https://github.com/impress/impress.js/">
                    <inlinecode style="font-size: 16px">
                    impress.js
                    </inlinecode>
                    <img class="icon" src="../favicon.png" style="width:10px;height:10px;">
                </a>
                <br/>
                <inlinecode style="font-size: 16px">
                    Ver. 2408
                </inlinecode>
            </inlinecode>
        </p>

    </div>
        '''

        self.div_blocks.append(div_block)

    def process_list(self, block):
        print("Processing list...")
        """处理列表块"""
        lines = block.split('\n')
        title = lines[0]
        list_items = [line for line in lines[1:] if line.strip() != '']
        list_content = "\n".join(list_items)

        last_div_id = self.get_div_id(self.div_blocks[-1]) if self.div_blocks else None
        current_div_id = 'a' + str(self.div_id_counter)

        # 创建新的div块
        div_content = f'''
    <div 
    id            = "{current_div_id}"
    class         = "step markdown"
    data-rel-to   = "{last_div_id if last_div_id is not None else 'empty'}"
    data-rel-x    = "0"
    data-rel-y    = "800"
    data-rel-z    = "0"
    data-rotate-y = "0"
    data-scale    = "2">

{title}

{list_content}

    </div>
'''

        self.div_blocks.append(div_content)
        self.div_id_counter += 1

    def process_image(self, block):
        print("Processing image...")
        """处理图片"""
        lines = block.split('\n')
        image_link = lines[0]

        last_div_id = self.get_div_id(self.div_blocks[-1]) if self.div_blocks else None
        current_div_id = 'a' + str(self.div_id_counter)

        div_content = f'''
    <div
    id            = "a{self.div_id_counter}"
    class         = "step markdown"
    data-rel-to   = "{last_div_id}"
    data-rel-x    = "0"
    data-rel-y    = "1200"
    data-rel-z    = "0"
    data-rotate-y = "0"
    data-scale    = "2">

{image_link}

    </div>
'''

        self.div_blocks.append(div_content)
        self.div_id_counter += 1  # 更新div id计数器

    def process_image_with_title(self, block):
        print("Processing image with title...")
        """处理图片"""
        lines = block.split('\n')
        list_items = [line for line in lines[1:] if line.strip() != '']
        image_link = lines[0]
        image_title = "\n".join(list_items)

        last_div_id = self.get_div_id(self.div_blocks[-1]) if self.div_blocks else None
        current_div_id = 'a' + str(self.div_id_counter)

        div_content = f'''
    <div
    id            = "a{self.div_id_counter}"
    class         = "step markdown"
    data-rel-to   = "{last_div_id}"
    data-rel-x    = "0"
    data-rel-y    = "0"
    data-rel-z    = "0"
    data-rotate-y = "0"
    data-scale    = "2">

{image_link}
{image_title}

    </div>
'''

        self.div_blocks.append(div_content)
        self.div_id_counter += 1  # 更新div id计数器

    def process_equation(self, block):
        print("Processing equation...")
        """处理公式块"""
        lines = block.split('\n')
        list_items = [line for line in lines if line.strip() != '']
        list_content = "\n".join(list_items)

        last_div_id = self.get_div_id(self.div_blocks[-1]) if self.div_blocks else None
        current_div_id = 'a' + str(self.div_id_counter)

        # 创建新的div块
        div_content = f'''
    <div 
    id            = "{current_div_id}"
    class         = "step"
    data-rel-to   = "{last_div_id if last_div_id is not None else 'empty'}"
    data-rel-x    = "0"
    data-rel-y    = "1200"
    data-rel-z    = "0"
    data-rotate-y = "0"
    data-scale    = "2">

{list_content}

    </div>
'''

        self.div_blocks.append(div_content)
        self.div_id_counter += 1

    def process_code(self, block):
        print("Processing code...")
        """处理代码块"""
        lines = block.split('\n')
        list_items = [line for line in lines[1:] if line.strip() != '']
        list_content = "\n".join(list_items)

        last_div_id = self.get_div_id(self.div_blocks[-1]) if self.div_blocks else None
        current_div_id = 'a' + str(self.div_id_counter)

        # 创建新的div块
        div_content = f'''
    <div 
    id            = "{current_div_id}"
    class         = "step markdown"
    data-rel-to   = "{last_div_id if last_div_id is not None else 'empty'}"  
    data-rel-x    = "0"
    data-rel-y    = "1200"
    data-rel-z    = "0"
    data-rotate-y = "0"
    data-scale    = "2">

{list_content}

    </div>
'''

        self.div_blocks.append(div_content)
        self.div_id_counter += 1

    def process_navigation_and_questions(self, block):
        print("Processing nav and questions...")

        self.nav_questions = f'''
    <div
    id            = "mm{self.chapter_number}{self.section_number}"
    class         = "step markdown"
    data-rel-to   = "c{self.chapter_number}{self.section_number}t"
    data-rel-x    = "0"
    data-rel-y    = "-2000"
    data-rotate-y = "0"
    data-rotate   = "0"
    data-scale    = "1">

![course {self.chapter_number}.{self.section_number} mindmap](img/c0{self.chapter_number}/mindmap-{self.chapter_number}-{self.section_number}.png)

    </div>

<!-- 本节问题 -->

    <div
    id            = "c{self.chapter_number}{self.section_number}q"
    class         = "step markdown"
    data-rel-to   = "c{self.chapter_number}{self.section_number}t"
    data-rel-x    = "0"
    data-rel-y    = "-800"
    data-z        = "500"
    data-rotate-x = "77"
    data-rotate-y = "0"
    data-rotate-z = "180"
    data-scale    = "2">

### {self.section}

- 
- 

----

[ {self.section}](il-{self.chapter_number}-{self.section_number}.html#/overview)
[| 练习 |](il-exec.html)
[ {self.section}](il-{self.chapter_number}-{self.section_number}.html#/overview)

    </div>
'''

    def generate_html(self):
        with open(self.markdown_file, 'r') as f:
            markdown_lines = f.readlines()

        block = []
        for line in markdown_lines:
            if line == "\n":
                if not self.header_processed:  # Only process the first block as header
                    self.process_header("\n".join(block))
                    self.header_processed = True
                else:
                    self.process_div_block("\n".join(block))
                block = []
            else:
                block.append(line)
        if block:
            self.process_div_block("\n".join(block))
            self.process_navigation_and_questions("\n".join(block))

        self.div_blocks.append(self.nav_questions)

        with open(self.html_file, 'w') as f:
            f.write(self.header + '\n' + ''.join(self.div_blocks) + '\n' + self.footer)

        print("Everthing done.")

if __name__ == "__main__":
    markdown_file = input("Input the Markdown filename please:")
    if os.path.isfile(markdown_file):
        generator = HTMLGenerator(markdown_file)
        generator.generate_html()
    else:
        print("Something wrong. Please input again.")

