# GAN
Introduce of GAN

# Proposal
찐개만(진짜 개 같이 만들자, 가제) 파티원 모집!!


1. 모집주제

- 기본 (dc, ls, ...)GAN(Generative Adversarial Network, 이하 GAN) 모델에 대한 지식 습득 및 이를 활용한 결과물 출력

- 최신 GAN 모델을 이해(하려고 노력)하고, 이를 활용하여 결과물을 출력


2. 파티목적

- 기본 GAN에 대한 지식 습득(책, 강의 등)

- Generative Dog Images(Kaggle)의 Notebooks를 참고(복붙)하여, 새로운 개 이미지 데이터를 생성

- 기본 GAN을 공부한 내용과 생성한 이미지를 파티의 발표자료로 활용

목적을 조기 달성시, GAN에 대한 최신 논문을 읽고(유튜버가 읽어주는 논문을 듣고 이해), 이를 구현(그 사람의 코드 복붙).

다양한 GAN 모델을 이해(하는 척)하고, 이를 구현(인터넷에서 밴치마킹)하여 결과물을 출력하여 발표에 반영



2. 우대조건

- 파티를 구하지 못하여 방황하고 있는 사람

- 성능 좋은 GPU를 소지한 사람(나 GTX1050 소유, 내꺼보다 구리면 흠..)

- GAN에 관심이 많거나 이에 대한 지식을 소유한 사람(나도 잘 모름)

- Tensorflow, Keras 등 언어를 이해할 수 있는 사람(나도 못함, 코드만 읽을 줄 알면 ok)

- PPT, Prezi 등 Presentation 툴을 잘 다루는 사람(나 둘다 다룰 줄 앎)

- 발표 잘하는 사람(나 발표 잘 못함)


3. 모집대상

- 타 파티에 소속되지 않은 사람

- 선장이 없는 배에 탑승하고 싶은 사람

- 성실한 사람


4. 지원방법

- 직접 문의


5. 지원기간

- 2020.02.21 24:00 까지

- 모집시 조기 마감될 수 있음

- 없으면 혼자 함


6. 직접 구현(그대로 배낀)한 Dcgan 모델로 생성한 이미지

■ 가벼운 Dcgan 모델을 활용하여, Celeb의 사진 20만장을 학습하고, 이미지를 생성



- 학습을 통해서 점점 사람다운 형상을 출력하기 시작함을 확인할 수 있었음.

- 학습을 빠르게 하기 위해서 input 픽셀수, batch_size, 신경망의 Layer 수를 줄여서 결과물이 좋지 않음.

- Parameter

batch_size = 16

z_dim = 100

learning_rate = 0.0002

beta1 = 0.5

epochs = 10

![9](https://user-images.githubusercontent.com/59387983/83408790-37469b80-a44e-11ea-969f-58a768c1dd5e.png)
![10](https://user-images.githubusercontent.com/59387983/83408792-37df3200-a44e-11ea-914b-f6e6d596f1c8.png)
![11](https://user-images.githubusercontent.com/59387983/83408795-3877c880-a44e-11ea-8cf9-88fee703c896.png)
![12](https://user-images.githubusercontent.com/59387983/83408797-39105f00-a44e-11ea-8bcb-48185d7deca5.png)
![13](https://user-images.githubusercontent.com/59387983/83408798-39105f00-a44e-11ea-8d26-feb52b639729.png)
![14](https://user-images.githubusercontent.com/59387983/83408802-39a8f580-a44e-11ea-8e3e-1e9ba8eb25f0.png)
![15](https://user-images.githubusercontent.com/59387983/83408805-3a418c00-a44e-11ea-83c9-49b03c05eba1.png)
![16](https://user-images.githubusercontent.com/59387983/83408806-3a418c00-a44e-11ea-9c00-f8caa819fdfe.png)
![17](https://user-images.githubusercontent.com/59387983/83408808-3ada2280-a44e-11ea-9dcf-17d529d03aec.png)
![18](https://user-images.githubusercontent.com/59387983/83408810-3b72b900-a44e-11ea-9e7c-d4d9f04db954.png)
![19](https://user-images.githubusercontent.com/59387983/83408811-3b72b900-a44e-11ea-9c37-9fbad2ba6dc4.png)
![20](https://user-images.githubusercontent.com/59387983/83408812-3c0b4f80-a44e-11ea-8a82-f2d7122c1a5a.png)
![21](https://user-images.githubusercontent.com/59387983/83408813-3c0b4f80-a44e-11ea-807b-515eca2ec478.png)
![23](https://user-images.githubusercontent.com/59387983/83408816-3d3c7c80-a44e-11ea-8404-5f340e63306c.png)
![24](https://user-images.githubusercontent.com/59387983/83408818-3d3c7c80-a44e-11ea-9e10-7d20d4477325.png)
![25](https://user-images.githubusercontent.com/59387983/83408819-3dd51300-a44e-11ea-80c7-4da2eda34e01.png)
![26](https://user-images.githubusercontent.com/59387983/83408823-3e6da980-a44e-11ea-8a33-6ca5544ecdcb.png)
![27](https://user-images.githubusercontent.com/59387983/83408827-3e6da980-a44e-11ea-9f36-4594ddd03e2f.png)
![29](https://user-images.githubusercontent.com/59387983/83408828-3f064000-a44e-11ea-8844-dbadb71b6822.png)
![30](https://user-images.githubusercontent.com/59387983/83408830-3f9ed680-a44e-11ea-8c41-1a89b8f314ec.png)
![31](https://user-images.githubusercontent.com/59387983/83408833-3f9ed680-a44e-11ea-957c-8ed71e6ea7ca.png)
![32](https://user-images.githubusercontent.com/59387983/83408834-40376d00-a44e-11ea-9351-9bd3feed58b4.png)
![33](https://user-images.githubusercontent.com/59387983/83408835-40d00380-a44e-11ea-956b-f0186292e403.png)
![34](https://user-images.githubusercontent.com/59387983/83408837-40d00380-a44e-11ea-9dde-c72295ce5dc9.png)
![35](https://user-images.githubusercontent.com/59387983/83408839-41689a00-a44e-11ea-8085-7cf0f58baf97.png)
![36](https://user-images.githubusercontent.com/59387983/83408840-41689a00-a44e-11ea-815f-d619e37a164c.png)
![37](https://user-images.githubusercontent.com/59387983/83408842-42013080-a44e-11ea-8011-16adfe7da39a.png)
![38](https://user-images.githubusercontent.com/59387983/83408843-4299c700-a44e-11ea-9dd8-6c4dc032bffe.png)
![39](https://user-images.githubusercontent.com/59387983/83408844-4299c700-a44e-11ea-895f-e9af3d94a4b1.png)
