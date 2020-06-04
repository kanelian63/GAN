# Goal of Project
Learn about GAN, the most innovative AI learning method of the past decade, and use it by participating in the kaggle competition. https://www.kaggle.com/c/generative-dog-images

# Details
Much of the project was conducted with reference to kaggle. The project will be based on a lecture by Yeon-Soo Yoo, deep learning in February 2020. I read papers on various models of GAN, modified the model, and printed the results.

The project proposal is as follows.


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

![34](https://user-images.githubusercontent.com/59387983/83408837-40d00380-a44e-11ea-9dde-c72295ce5dc9.png)
![35](https://user-images.githubusercontent.com/59387983/83408839-41689a00-a44e-11ea-8085-7cf0f58baf97.png)
![36](https://user-images.githubusercontent.com/59387983/83408840-41689a00-a44e-11ea-815f-d619e37a164c.png)
![37](https://user-images.githubusercontent.com/59387983/83408842-42013080-a44e-11ea-8011-16adfe7da39a.png)
![38](https://user-images.githubusercontent.com/59387983/83408843-4299c700-a44e-11ea-9dd8-6c4dc032bffe.png)
![39](https://user-images.githubusercontent.com/59387983/83408844-4299c700-a44e-11ea-895f-e9af3d94a4b1.png)


# Files
model - Big Gan, Conditional Progan, DC GAN

outputs	- Outputs of Models

papers - Referenced papers

utils - Preprocess of data

Generative Dogs Images PPT.pdf - resentation / If you want a presentation PPT file, please email me.

# Results
Conditional Progan

![progan output1](https://user-images.githubusercontent.com/59387983/83746225-c3003800-a699-11ea-8fcd-394b2a6cc9c2.jpg)

Big Gan

![biggan output1](https://user-images.githubusercontent.com/59387983/83746217-c1cf0b00-a699-11ea-911b-e790e2852abd.jpg)
