import os

# 라벨 디렉토리(train과 valid 둘다 바꿔줘야함)
# label_dir = '/home/samuel/Downloads/Worker_Data/train/labels'
label_dir = '/home/samuel/Downloads/Worker_Data/valid/labels'

# 라벨 파일을 순회하며 클래스 인덱스 변경
for label_file in os.listdir(label_dir):
    if label_file.endswith('.txt'):  # 라벨 파일이 .txt 파일인 경우
        file_path = os.path.join(label_dir, label_file) # 라벨링 파일 경로
        
        with open(file_path, 'r') as file:
            lines = file.readlines() # 파일의 모든 줄을 리스트 형식으로 lines에 저장

        # 변경된 내용을 다시 저장
        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.strip().split() # 각 줄의 공백 제거후 문자열을 분리하여 리스트 형식 parts에서 저장
                if parts[0] == '0': # 0인 클래스(신발) 제거
                    continue
                elif parts[0] == '3': # 클래스 변경(3 -> 2, 2 -> 1, 1 -> 0)
                    parts[0] = '2'
                elif parts[0] == '2':
                    parts[0] = '1'
                elif parts[0] == '1':
                    parts[0] = '0'
                file.write(' '.join(parts) + '\n')