import os
import json
import shutil

root_directory = "02.라벨링데이터"

for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename == '.DS_Store':
            continue
        if filename.endswith(".json"):  # JSON 파일만 처리
            file_path = os.path.join(dirpath, filename)  # 파일 전체 경로
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)  # JSON 파일 읽기
                age = data['age_past']
                age_now = data['age_now']
                source_file = data['filename']
                if age <= 10:
                    continue
                
                elif age >= 11 and age <= 15:
                    if age_now > 20:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./11-15"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)
                
                elif age >= 16 and age <= 20:
                    if age_now > 21:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./16-20"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)
                
                elif age >= 21 and age <= 25:
                    if age_now > 26:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./21-25"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)
                
                elif age >= 26 and age <= 30:
                    if age_now > 31:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./26-30"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)

                elif age >= 31 and age <= 35:
                    if age_now > 36:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./31-35"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)

                elif age >= 36 and age <= 40:
                    if age_now > 41:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./36-40"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)
                
                elif age >= 41 and age <= 50:
                    if age_now > 51:
                        continue
                    source_path = '01.원천데이터'+dirpath.replace('02.라벨링데이터','').replace('L','S')+'/'+source_file+'.png'
                    print(f"찾는 파일 경로: {source_path}")
                    destination_path = "./41-50"
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.copy2(source_path, destination_path)