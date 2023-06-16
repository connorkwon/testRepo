import os

# out 디렉터리 생성
os.makedirs('out', exist_ok=True)

# 파일 경로
file_path = os.path.join('out', 'sample.txt')

# 파일 내용 작성
file_size = 300 * 1024  # 300KB
with open(file_path, 'w') as file:
    file.write('A' * file_size)

print(f"File created: {file_path}")
