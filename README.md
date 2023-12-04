# 연관 게시글 추천 알고리즘 및 단어 연관지도 구현
## 프로젝트 소개
이 프로젝트는 코딩허브 강의 관련 정보에 대한 게시판을 구축하는 과제입니다. Python 기반의 Django 프레임워크를 사용하여 구현되었습니다. 해당 과제에서는 게시글 간의 연관성을 분석하고 시각화하는 기능을 중점으로 다룹니다.
## 배포 링크 바로가기 https://codinghub.sungbinlee.dev/
이 프로젝트는 AWS 환경에서 uwsgi와 nginx를 사용하여 배포되었습니다.
## https://codinghub.sungbinlee.dev/admin
ID: admin 
PW: qwer1234!!
## 데모 
![ezgif-3-ac46f0253e](https://github.com/sungbinlee/S.B.Lee-WikiPage/assets/52542229/6c03e4bb-874f-42c5-bdd6-672f19a24e08)

![ezgif-3-7b6dc2f03c](https://github.com/sungbinlee/S.B.Lee-WikiPage/assets/52542229/8c4d6d4d-94ec-4d80-9990-589da2aef4bf)

## 접근 방식

이 프로젝트는 다음과 같은 방법으로 게시글 간의 연관성을 분석합니다.

### TF-IDF와 코사인 유사도

- **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - 텍스트에서 각 단어의 상대적인 중요도를 평가하는 데 사용됩니다. 이는 각 단어가 특정 문서 내에서 얼마나 자주 등장하는지와 전체 문서에서 얼마나 자주 등장하는지를 고려하여 가중치를 부여합니다.
  
- **코사인 유사도**
  - TF-IDF로 벡터화된 문서들 간의 유사성을 계산하는 데 사용됩니다. 두 벡터 간의 코사인 각도를 측정하여 문서 간의 유사도를 측정합니다.

### 데이터 전처리

텍스트 데이터의 전처리는 다음과 같은 단계를 거쳐 이루어집니다.

- **조사 및 부사 제거**
  - 정규표현식을 사용하여 의미를 담지 않는 조사, 부사 등을 제거합니다.
  
- **불용어 제거**
  - 불용어 리스트를 활용하여 의미적으로 중요하지 않은 단어를 제거합니다.

## 고도화 방향

현재의 접근 방식을 보완하고 더 나은 분석과 결과를 위해 다음과 같은 방향으로 고도화 시킬 수 있습니다.

- **형태소 분석기 활용**
  - 한국어의 특성에 맞게 형태소 분석기를 사용하여 단어의 의미적 연결성을 더욱 정확히 파악합니다.

- **Word2Vec 및 임베딩 기법 적용**
  - 단어 간의 의미적 유사성을 고려하여 단어를 벡터로 표현하고, 이를 활용하여 보다 정교한 연관성 분석을 시도합니다.

## 관련 프로젝트

1. [**가짜 뉴스 감지 프로젝트**](https://sungbinlee.github.io/artificial%20intelligence/how-to-detect-fake-news/ ):
   - **목적**: 가짜 뉴스를 탐지하고 진실된 정보를 구별하는데 텍스트 분류 모델 사용.
   - **과정**: 데이터 수집 후 텍스트 전처리 및 특징 추출, 머신러닝 모델 학습 및 검증을 통해 가짜 뉴스 식별.

3. [**헬스케어 앱 리뷰 분석 프로젝트**](https://sungbinlee.github.io/artificial%20intelligence/mobile-app-review-insights-through-lda-topic-modeling/):
   - **목적**: 건강 앱의 사용자 리뷰를 텍스트 마이닝하여 고객 요구사항 파악.
   - **과정**: Google Play Store에서 리뷰 크롤링, 데이터 전처리, LDA 주제 모델링을 통해 긍정적 및 부정적 리뷰 주제 도출.

4. [**연관규칙을 이용한 데이터 마이닝 프로젝트**](https://sungbinlee.github.io/artificial%20intelligence/association-rule-mining/):
   - **목적**: 데이터 내의 패턴 및 연관성 파악을 통한 인사이트 발굴.
   - **과정**: 연관규칙 분석을 통해 항목 간의 관련성을 찾고 이를 통해 데이터 세트 내의 유용한 규칙 도출.
