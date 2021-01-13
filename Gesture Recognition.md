# Gesture Recognition

전체적인 몸 동작을 수행하기에는 계산량이 너무 많고 복잡해진다. 따라서 주요 관절의 움직임들만 주목하여 계산량을 줄이고 단순화하여 관절들의 움직임을 통해 제스쳐를 인식하도록 한다.

* ## PoseNet 

구글, 안드로이드에서 개발한 모델로 이미지에서 사람의 팔꿈치 및 무릎 위치를 추정할 수 있다.

포즈 추정 모델은 이미지에 나와있는 사람이 누군지 식별하는 것이 아니라, 주요 인체 부위만 식별

또한 PoseNet은 웹과 모바일(안드로이드, 아이폰)용만 제공하고 윈도우 상에서 쓸 수가 없어서 별도로 변환하는 코드를 짜서 사용해야 한다. 	

* [관련 github 코드1](https://github.com/rwightman/posenet-python) 

	* [관련 blog 코드2](https://blog.naver.com/PostView.nhn?blogId=tramper2&logNo=221834379945&categoryNo=105&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search)

* **PoseNet workflow**

![](C:\Users\pc\Desktop\Gesture_Recognition\img\PoseNet workflow.PNG)

* **PoseNet 이용하기**
  * [PoseNet 앱 사용 코드(Tensorflow lite 관련 문서)](https://github.com/tensorflow/tfjs-models/tree/master/posenet)
  * [PoseNet 응용하기](https://0urtrees.tistory.com/80)
* **PoseNet 모델에 의해 감지 된 신체관절 목록**

| 0    | 코            |
| ---- | ------------- |
| 1    | 왼쪽 눈       |
| 2    | 오른쪽 눈     |
| 3    | 왼쪽 귀       |
| 4    | 오른쪽 귀     |
| 5    | 왼쪽 어깨     |
| 6    | 오른쪽 어깨   |
| 7    | 왼쪽 팔꿈치   |
| 8    | 오른쪽 팔꿈치 |
| 9    | 왼쪽 손목     |
| 10   | 오른쪽 손목   |
| 11   | 왼쪽 엉덩이   |
| 12   | 오른쪽 엉덩이 |
| 13   | 왼쪽 무릎     |
| 14   | 오른쪽 무릎   |
| 15   | 왼쪽 발목     |
| 16   | 오른쪽 발목   |

## 개괄적인 프로젝트 방향

* 1월 12일 - 1월 17일 (실습 위주로 진행)

>* PoseNet 사용법 익히기
>* Android Studio  익히기 (Tensorflow Lite 예제)
>* Kotlin(or JAVA) 기본적인 문법 및 활용
>* Gesture(자세) 분류하는 법 익히기

* 1월 18일 - 1월 25일(실습 예제 변형 및 구현)

>* DataSet 구하기(없으면 만들기)
>* 예제 활용하여 최종 프로젝트 만들기
>* 최종점검





