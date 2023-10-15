# LSTM & YOLO를 활용한 CCTV 절도 이상탐지(Anormal Detection)

## 목차
  **1. 프로젝트 기획 이유**
  
  **2. 데이터 소개 및 전처리**
  
  **3. 모델링**
  
  **4. 비교 분석**
  
  **5. 추후 보안 방향**
  
  **6. 프로젝트 실행 방법**
  
  **7. 팀원 및 참고 자료**


## 1. 프로젝트 기획 이유
 **model : LSTM(Long Short-Term Memory) & YOLOv5**

CCTV 절도 이상탐지를 위해 LSTM( Long Short-Term Memory) 기획한 이유는 다음과 같습니다.
- **1. 보안 및 안전 강화 :** 범죄 예방과 안전 보안은 중요한 사회적 문제입니다. AI가 발전함에 따라 무인 편의점, 무인 카페 등이 생겨나는 동시에 절도 등의 범죄도 증가하는 추세입니다. 이는 절도 뿐만 아니라 기타 범죄 및 사고, 자살 등 안전과 관련하여 영상(CCTV 등)을 활용한 이상탐지 시스템은 범죄 예방 및 안전 강화에 기여할 수 있으며, 이는 도시 및 지역의 안전성을 향상시킬 수 있을 것이라 기대하였기 때문입니다.
- **2. 실시간 모니터링 :** CCTV 시스템은 실시간으로 작동하며, LSTM은 실시간 데이터 스트림을 다루는 데 적합한 모델입니다. 이상 행위가 감지되면 즉각적으로 경고를 보내거나 조치를 취할 수 있습니다.
- **3. 시간 순서에 따른 패턴 탐지 :** LSTM은 시간에 따른 데이터의 패턴을 감지하고 모델링하는 데 뛰어납니다. 그래서 절도 등 범죄와 관련된 데이터는 시간에 따른 행동 패턴을 가지고 있으며, 이러한 패턴을 식별하고 이상 행위를 탐지하는 데 효과적입니다. 특히 CCTV 영상 데이터는 연속적인 프레임 시퀀스로 구성되어 있기에 프레임 정보를 고려하여 현재 상황을 이해하고 이상 행위를 탐지할 수 있습니다.
- **4. 비용 절감 :** 이상탐지 시스템은 인적 자원에 의존하지 않고도 보안을 유지할 수 있으므로 비용 효율적인 해결책이 될 것입니다.
- **5. 성능 향상 :** 딥러닝 기술과 컴퓨팅 성능이 향상되면서, CCTV 절도 이상탐지 시스템은 더 정교하고 효과적으로 구축될 수 있습니다. 또한 이상탐지 시스템 자체로 인해 더욱 다양한 상황과 패턴을 학습할 수 있는 데이터를 추가로 생성되기에 LSTM은 이러한 발전을 활용하여 더 정확한 이상탐지를 제공할 수 있습니다.

- **사용한 프레임 워크**
![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/16104792-fe1b-4d2e-ad11-e7cd435882af)


## 2. 데이터 소개 및 전처리

![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/ee5128ae-f849-45c1-b718-9cf4bdb1e96b)
![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/1753f0cf-4208-476d-a3d3-a7de279d4b40)
- **AI Hub**에서 CCTV 영상 중 **절도** 데이터만 선별

![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/2dbbd5f7-4064-4450-a013-7f103edd859e)
![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/401daead-259a-4780-830d-91720d73c8cd)

- 데이터: 1개의 데이터는 평균 1분(fps:3) 영상
- 1분 개별 영상에서 10초 내외로 **절도 행위**를 하는 영상이 많아 10초로 끊어서 개별 데이터 생성.
- 절도 행위의 빈도를 확인하여, 같은 영상에서 일반 영상도 같은 빈도로 clip하여 추출.

![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/ce191e0b-bf6e-428b-a84c-1945c7e4d4f0)
- 10초를 기준으로 clip/추출한 영상 데이터를, mediapipe 에서 사람의 landmark의 부위를 선정하여 x, y 좌표를 추출하여 모델에 넣을 데이터 확보.
- 추출한 x, y 좌표의 움직임 패턴을 학습시켜 이상탐지를 할 계획.

## 3. 모델링

**LSTM**

![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/725a71e5-8ac9-4c81-bd5a-6270fcc96bb1)

- 시간 순서에 따른 패턴을 학습시키기 위해 RNN(순환신경망) 계열 사용.
- RNN 문제점 : RNN hidden layers들은 같은 weight를 공유하며 엣지로 연결되어 순환구조를 이룬다. input weight와 hidden layers에서 공유되는 weight를 연산하여 output으로 데이터를 보낸다. 이 때 hidden layer에서 같은 weight 공유하기에 hidden layer 연산 과정에서 weight 연산이 1보다 크다면 **Gradient Exploding**이 되어 학습이 진행되지 않고, 1보다 작으면 **Gradient Vanishing**이 되어 학습이 진행되지 않는 문제가 발생한다.
- LSTM의 3개의 게이트와 cell state를 추가해서 **Gradient Exploding/Vanishing** 문제를 해결한다. **forget gate**(옆 레이어에서 들어오는 정보를 얼마나 잊어버릴 것인지 결정)와 **input gate**(input으로 들어오는 데이터를 얼마나 받아들일 것인지), **cell state**(forget/input 게이트에서 들어온 값을 업데이트) 3개의 게이트를 통해 들어온 데이터를 **output gate**(얼마만큼 내보낼 것인지 결정)에서 결정하여 내보낸다.
- GRU 모델은 LSTM 모델에서 cell state가 빠진 모델이다.
- 해당 프로젝트를 진행할 때는 landmark x, y 좌표를 input data로 활용할 것이기에 비교적 짧은 hidden layers 가지기에 LSTM 모델을 활용하기로 결정했다. 추후에 든 생각이지만, GRU 모델도 같이 비교를 해보았으면 더 좋았을 것이다.
- 추출한 x, y좌표를 모델에 입력시켜 하이퍼파라미터들을 변경하며 비교 분석을 진행한다.

## 4. 비교 분석

- **여러 조건들을 비교하며 진행**

- 1단계 :  object detection을 **mediapipe**만 사용하여 landmark 좌표를 찾을 것인지, **yolo**를 사용하여 detect한 후 mediapipe로 landmark를 할 것인지 비교.
- 2단계 : 3fps 10초 시퀀스가 기본(30frame) -> 이 10초 시퀀스를 이어 붙여서(30frame * 3 = 90frame) 15frame씩 윈도우 슬라이싱하여 30frame씩 데이터 생성.
- 3단계 : landmark 좌표를 추출할 때, 얼굴 좌표(얼굴부터 발까지)도 사용할 것인지 몸의 좌표(어깨부터 발까지)만 사용할 것인지 비교.
![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/4404472a-6646-48c8-b56e-f7f5c634caeb)

**1단계 :**
- 문제 1 : **mediapipe** 사람이 아닌 다른 object를 detect하는 경우 발생. **train 데이터셋**도 문제 소지.
  
![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/cbb42c7e-d3df-46c0-b8e6-b53329e714c0)


- 해결 1 : **yolo**를 통해서 사람을 먼저 detect한 후, 사람의 landmark 좌표를 추출하도록.
- 주의 1 :  제일 마지막 frame을 중복으로 누적해야 하는 경우의 문제 발생(data len: 30frame : 28frame += frame[-1] 길이가 30frame가 될 때까지). 하지만 사람이 아닌 object를 detect하지 않아서 방해되는 데이터 생성을 어느 정도 막아주는 역할도 함.

![image](https://github.com/seonydg/LSTM-for-Anomaly-Detection/assets/85072322/47ae22ce-3305-4c28-8c29-f7f9cdd7f086)

- 문제 2 : **yolo** 적용 시 detect를 못하는 경우 landmark 좌표를 얻을 수 없어 input data의 길이가 상이한 경우가 발생하여 input data 오류 발생.
- 해결 2 : 제일 마지막 frame을 중복으로 누적(data len: 30frame : 28frame += frame[-1] 길이가 30frame가 될 때까지). 그래서 좌표의 패턴을 학습하기에 방해가 될 소지가 있음. 하지만 사람이 아닌 object를 detect하지 않아서 방해되는 데이터 생성을 어느 정도 막아주는 역할도 함.

mediapipe가 사람을 찾지 못하는 환경들, 즉 탁자나 의자가 사람을 가려버리는 경우에는 yolo로 사람을 찾은 후 mediapipe 적용.
mediapipe도 기본적으로 사람을 잘 찾기에 사람을 찾는 방해물이 없는 경우에는 mediapipe만 적용.

**2단계**
- 3fps 10초 시퀀스가 기본(30frame)인 경우를 이어붙인 이유:
  1. 조금 더 많은 데이터를 넣기 위해 : 10초를 이어 붙여서 30초로 만든 후 윈도우 슬라이싱으로 5초 단위(15frame)로 건너띄며 30frame 생성
  2. 개별 패턴 30frame는 '처음-끝'이고 이어붙여서 15frame로 건너뛰면서 데이터를 생성하게 되면 '중간-중간'의 패턴이 생성되며, 이것을 학습할 경우 패턴에 어떤 영향이 있는지 확인하기 위해.

 결론은 이어붙여 만든 시퀀스는 개별 시퀀스로 학습한 결과보다 좋지 못한 결과로 인해 개별 시퀀스를 사용하기로 함.

 **3단계**
 

























