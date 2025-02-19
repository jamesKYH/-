import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import re

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model('keras_model.h5', compile=False)

# Load the labels
class_names = [line.strip() for line in open('labels.txt', 'r').readlines()]

# 사용자 실제 나이 입력
actual_age = st.number_input("실제 나이를 입력하세요:", min_value=1, max_value=120, step=1)

# 선택 옵션: 카메라 입력 또는 파일 업로드
input_method = st.radio("이미지 입력 방식 선택", ["카메라 사용", "파일 업로드"])

if input_method == "카메라 사용":
    img_file_buffer = st.camera_input("정중앙에 사물을 위치하고 사진찍기 버튼을 누르세요")
else:
    img_file_buffer = st.file_uploader("이미지 파일 업로드", type=["png", "jpg", "jpeg"])

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

if img_file_buffer is not None:
    # 원본 이미지 불러오기
    image = Image.open(img_file_buffer).convert('RGB')
    
    # 모델 입력 크기(224x224)로 변환
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    
    # 넘파이 배열로 변환 및 정규화
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    
    # 데이터 배열에 이미지 추가
    data[0] = normalized_image_array
    
    # 모델 예측 실행
    prediction = model.predict(data)
    index = np.argmax(prediction)
    predicted_label = class_names[index]  # 원본 라벨 (예: "2 21-25")
    confidence_score = prediction[0][index]
    
    # 연령대만 추출 (예: "21-25")
    match = re.search(r'(\d+-\d+)', predicted_label)
    if match:
        predicted_age_range = match.group(1)
    else:
        st.write("❌ 예측된 연령대를 확인할 수 없습니다.")
        st.stop()
    
    # "결과 확인하기" 버튼 추가
    if st.button("결과 확인하기 🎯"):
        st.write(f"### 🏷️ 예측된 연령대: {predicted_age_range}")
        st.write(f"📊 신뢰도: {confidence_score:.2f}")
        
        # 실제 나이와 예측된 연령대의 평균값을 비교하여 차이 계산
        age_range_values = list(map(int, predicted_age_range.split('-')))
        predicted_avg_age = sum(age_range_values) // 2
        age_difference = abs(predicted_avg_age - actual_age)
        
        if predicted_avg_age > actual_age + 10:
            st.write(f"😲 실제 나이보다 **{age_difference}살 많게** 예측되었습니다!")
        elif predicted_avg_age < actual_age - 5:
            st.write(f"🎉 **매우 동안이시네요!** 😍 실제 나이보다 {age_difference}살 적게 나왔어요!")
        else:
            st.write(f"✅ 실제 나이와 {age_difference}살 차이입니다.")