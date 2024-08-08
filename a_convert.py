import os
import json
count = 0
def process_folder(folder_path):
    global count
    entries = []
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        if 'source.txt' in files and 'target.txt' in files:
            source_file_path = os.path.join(root, 'source.txt')
            target_file_path = os.path.join(root, 'target.txt')
            
            with open(source_file_path, 'r', encoding='utf-8') as source_file:
                source_lines = source_file.readlines()
            
            with open(target_file_path, 'r', encoding='utf-8') as target_file:
                target_lines = target_file.readlines()
            
            # 确保两者行数相等
            if len(source_lines) == len(target_lines):
                for source_line, target_line in zip(source_lines, target_lines):
                    entry = {
                        "output": source_line.strip(),
                        "input": target_line.strip(),
                        "instruction": "请把现代汉语翻译成古文"
                    }
                    entries.append(entry)
                    count+=1
                    print(f"正在处理：{count} - {source_line.strip()}")
    
    return entries

def write_to_jsonl(entries, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in entries:
            json_line = json.dumps(entry, ensure_ascii=False)
            file.write(json_line + '\n')

if __name__ == "__main__":
    # 设定待处理的根文件夹路径
    folder_path = './'
    output_file = 'dataset.jsonl'
    
    # 处理文件夹
    entries = process_folder(folder_path)
    
    # 写入 JSONL 文件
    write_to_jsonl(entries, output_file)
    
    print(f"转换完成，结果保存在 {output_file}")
