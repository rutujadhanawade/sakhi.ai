# sakhi.ai
![screen2](https://user-images.githubusercontent.com/46274158/125912601-3fdf4907-1b89-4ec4-bcf9-62b840b82d91.png)
## "The problem it solves":
Detecting emotional state of a person by analyzing a text document written by him/her

appear challenging but also essential many times due to the fact that most of the times

textual expressions are not only direct using emotion words but also result from the

interpretation of the meaning of concepts and interaction of concepts which are

described in the text document. Recognizing the emotion of the text plays a key role in

the human-computer interaction. Emotions may be expressed by a person‟s speech,

face expression and written text known as speech, facial and text based emotion

respectively. But text based emotion recognition system still needs attraction. In computational linguistics, the detection of human emotions in text is becoming increasingly important from an applicative point of view.
![screen1](https://user-images.githubusercontent.com/46274158/125912629-e3479638-f32a-481f-a8d7-31a9ed6b071a.png)
## Emotion Classification in Short Messages
It is a Multi-class sentiment analysis problem to classify texts into five emotion categories: joy, sadness, anger, fear, neutral. This includes dataset preparation, traditional machine learning with scikit-learn, Dataset was combined from daily dialog, isear, and emotion-stimulus to create a balanced dataset with 5 labels: joy, sad, anger, fear, and neutral. The texts mainly consist of short messages and dialog utterances.
## Experiments
### Traditional Machine Learning:
Data preprocessing: noise and punctuation removal, tokenization, stemming

Text Representation: TF-IDF

Classifiers: Naive Bayes, Random Forrest, Logistic Regression, SVM

Approach F1-Score<br>
Naive Bayes 0.6702<br>
Random Forrest 0.6372<br>
Logistic Regression 0.6935<br>
SVM    0.7271<br>

![accuracyhigh](https://user-images.githubusercontent.com/46274158/125912637-fe8498d7-2a45-4dce-8844-6d45671b71f1.png)
<br> [https://colab.research.google.com/drive/1YY6xYdz6Jds6ltw_wMSZkI8ywHQiBKfS?usp=sharing#scrollTo=WVHAzcNp8vCU](url) Check accuracy from here
## Use Case/ Example:
Nowadays within the Internet, there's an immense amount of textual data. It’s fascinating to extract emotion from various goals like those of business. As an example, in luxury merchandise, the emotional aspect as brand, individuality, and prestige for purchasing confirmations, are a lot necessary than other aspects like technical, functional, or price. In such conditions, buyers are happy to shop for a product even with high costs. Emotion selling aims to simulate emotions in clients for tying them to brand and then increase the selling of service/product
