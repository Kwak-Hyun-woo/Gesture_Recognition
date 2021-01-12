# Gesture Recognition

전체적인 몸 동작을 수행하기에는 계산량이 너무 많고 복잡해진다. 따라서 주요 관절의 움직임들만 주목하여 

* ## PoseNet 

구글, 안드로이드에서 개발한 모델로 이미지에서 사람의 팔꿈치 및 무릎 위치를 추정할 수 있다.

포즈 추정 모델은 이미지에 나와있는 사람이 누군지 식별하는 것이 아니라, 주요 인체 부위만 식별

또한 PoseNet은 웹과 모바일(안드로이드, 아이폰)용만 제공하고 윈도우 상에서 쓸 수가 없어서 별도로 변환하는 코드를 짜서 사용해야 한다. [관련 github 코드1](https://github.com/rwightman/posenet-python) [관련 blog 코드2](https://blog.naver.com/PostView.nhn?blogId=tramper2&logNo=221834379945&categoryNo=105&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search)

**PoseNet workflow**

![](C:\Users\pc\Desktop\Gesture_Recognition\img\PoseNet workflow.PNG)

**PoseNet 이용하기**

[PoseNet 앱 사용 코드(Tensorflow lite 관련 문서)](https://github.com/tensorflow/tfjs-models/tree/master/posenet)

[PoseNet 응용하기](https://0urtrees.tistory.com/80)





