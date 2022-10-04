## Slogan-Smithy-Web
### gpt2, Kogpt2을 파인튜닝한 슬로건 생성 모델을 활용한 웹서비스 구현

슬로건 스미시 프로젝트는 슬로건 데이터를 수집하여 정제하고, 사전 학습된 언어모델에 파인튜닝하여 프로토타입 웹까지 구현한 프로젝트로
사용자가 직접 웹서비스 방문을 통해 기업정보를 입력하고 슬로건을 생성할 수 있습니다.
 
English, Beta Korean 버전은 다운스크림 태스크에 맞게 언어모델을 파인튜닝한 버전입니다.

Korean 버전은 프리트레인 태스크와 같이 generating 방식으로 학습하여(AINIZE 온라인 서비스 활용) 생성된 결과 값에서 필요한 슬로건 부분만 추출하고, 유사도를 분석하여 유사도가 가까운 슬로건 리스트를 만들었습니다.


> 진입 화면

![image](https://user-images.githubusercontent.com/86090355/193762925-8bf7b0fc-6a06-4760-af4a-4dbd3ab49ce5.png)

> 모델 선택 및 유사도 값 조절

![image](https://user-images.githubusercontent.com/86090355/193763053-4db69490-477f-4af0-a0d6-7e9eec8c00ac.png)

> 결과 확인 및 선택 화면

![image](https://user-images.githubusercontent.com/86090355/193763099-712c9140-6597-473e-981b-5b80d3e6c50e.png)

> 선택한 슬로건을 이미지화

![image](https://user-images.githubusercontent.com/86090355/193763181-052dcf2d-7510-4069-bf4c-6f4f32f58810.png)

