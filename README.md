# Goal of Project
Learn about GAN, the most innovative AI learning method of the past decade, and use it by participating in the kaggle competition. https://www.kaggle.com/c/generative-dog-images

# Details
Much of the project was conducted with reference to kaggle. The project will be based on a lecture by Yeon-Soo Yoo, deep learning in February 2020. I read papers on various models of GAN, modified the model, and printed the results.

The project proposal is as follows.


# 가벼운 Dcgan 모델을 활용하여, Celeb의 사진 20만장을 학습하고, 이미지를 생성


- 학습을 통해서 점점 사람다운 형상을 출력하기 시작함을 확인할 수 있었음.

- 학습을 빠르게 하기 위해서 input 픽셀수, batch_size, 신경망의 Layer 수를 줄여서 결과물이 좋지 않음.

- Parameters

batch_size = 16, z_dim = 100, learning_rate = 0.0002, beta1 = 0.5, epochs = 10

![34](https://user-images.githubusercontent.com/59387983/83408837-40d00380-a44e-11ea-9dde-c72295ce5dc9.png)
![35](https://user-images.githubusercontent.com/59387983/83408839-41689a00-a44e-11ea-8085-7cf0f58baf97.png)
![36](https://user-images.githubusercontent.com/59387983/83408840-41689a00-a44e-11ea-815f-d619e37a164c.png)
![37](https://user-images.githubusercontent.com/59387983/83408842-42013080-a44e-11ea-8011-16adfe7da39a.png)
![38](https://user-images.githubusercontent.com/59387983/83408843-4299c700-a44e-11ea-9dd8-6c4dc032bffe.png)
![39](https://user-images.githubusercontent.com/59387983/83408844-4299c700-a44e-11ea-895f-e9af3d94a4b1.png)

# Data Preprocessing
![캡처](https://user-images.githubusercontent.com/59387983/83991664-6f873600-a988-11ea-889e-6bb2ab40cb8b.PNG)


# DC GAN
![dcgan(64x64) result](https://user-images.githubusercontent.com/59387983/83991466-c5a7a980-a987-11ea-9faf-ee1499d3ea60.jpg)

# Loss
![그림1](https://user-images.githubusercontent.com/59387983/83991144-dc99cc00-a986-11ea-8103-377b3a8aa5bf.png)

Generator의 초기 Loss가 큰 이유는 학습을 빠르게 하기 위해서 초반부의 기울기가 큰 Loss function을 사용했기 때문이다. 60에폭쯤 진행했을 때, discriminator가 generator를 지나치게 압도하여 학습이 종료되는 것을 볼수 있다. 의도와 관계없이 학습이 종료되는 가장 흔한 경우.

기존 GAN에 학습의 안정성에 도움이 되는 기법을 사용하였지만, 개의 모습은 사람의 얼굴보다 더 복잡하고, 다양한 분포를 가졌으므로 학습하기 더 어려웠다. 생성자와 판별자 사이의 능력에 적절한 균형을 이루면서, 두 네트워크가 안정적으로 전역해로 수렴하도록 만드는 것이 GAN이 해결해야 할 숙제인데, 나의 모델에 적용할 수 있는 방법을 사용했음에도 결과가 좋지 않았다.


# Conditional Progan
![progan output1](https://user-images.githubusercontent.com/59387983/83746225-c3003800-a699-11ea-8fcd-394b2a6cc9c2.jpg)

![biggan output1](https://user-images.githubusercontent.com/59387983/83746217-c1cf0b00-a699-11ea-911b-e790e2852abd.jpg)

# Loss
![그림2](https://user-images.githubusercontent.com/59387983/83991146-dd326280-a986-11ea-953e-ae644f000136.png)

High resolution image를 생성하는 경우에는 training image와 generated image를 구분하기가 더 쉬워지는 경향이 있어서 학습이 불안정해진다. Pro GAN의 핵심 아이디어는 generator와 discriminator를 점진적으로 키운다는 것이다. 저해상도에서 시작해서 세밀한 점들을 배울 수 있도록 새로운 레이어들을 추가하는 방식이다. 이런 방식을 취함으로 인해 기존 GANs을 보다 안정적이면서 빠르게 학습하는 것이 가능해졌다. 이 방식의 사용함으로써 학습에 불리한 점은 깊은 층의 문제점, 오차의 전파가 약해지고, 학습이 느려진다. 이를 보완하기 하고, 점진적으로 네트워크 레이어를 추가할 때 sudden shock이 일어나지 않도록 새로 추가하는 레이어를 부드럽게 (fade in) 넣어준다. 이를 레지듀얼 블록, Highway Network이라 한다. 이는 모델을 깊게 만들면서도 정보의 흐름을 통제하고 학습 가능성을 극대화할 수 있도록 해준다. ResNet에서 사용하는 아이디어를 차용해 온듯하다.

# Files
model - Big Gan, Conditional Progan, DC GAN

outputs	- Outputs of Models

papers - Referenced papers

utils - Preprocess of data

Generative Dogs Images PPT.pdf - resentation / If you want a presentation PPT file, please email me.
                               - About DC GAN, LS GAN, C GAN, SA GAN

