# Flower Predictor

🛠️ This flower predictor combines advanced models (VGG16, Resnet50, and InceptionV3) to identify flowers from uploaded images. Plus, it comes with an interactive interface featuring both light and dark themes.<br>
<br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="30" alt="vscode logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="30" alt="html5 logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="30" alt="css3 logo"  />
<img width="12" />
<img src="https://www.pngfind.com/pngs/m/128-1286693_flask-framework-logo-svg-hd-png-download.png" height="30" alt="flask logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="30" alt="tensorflow logo"  />

## Video Demo
🎥 Here you can find a video of the working project
https://github.com/user-attachments/assets/4043c481-7b9b-4516-97c0-d64decb7f723


## Prerequisites

Install Python on your system 👉 [Python](https://www.python.org/downloads/)
<br><br>
Intall the flower dataset to train your model from 👉 [Flower](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)<br>
(🚨NOTE: Extract the folder and paste the flower folder in the dataset folder after cloning the repository)

## Deployment

To run this project first clone this repository using

```bash
  git clone https://github.com/aka-Harsh/Flower-Predictor.git
```
Locate this repository using terminal and then create a virtual enviroment and activate it

```bash
  python -m venv venv
  .\venv\Scripts\activate
```
Perform this in your VScode editor to select python intepreter
```bash
  Select View > Command Palette > Python: Select Interpreter > Enter Interpreter path > venv > Script > python.exe
```

Install all the required packages 
```bash
  pip install -r requirements.txt
```
Train the Models (This will create 3 trained model in your empty models folder)
```bash
  python train_model.py
```

Finally run the app.py file
```bash
  python app.py
```

Open a web browser and go to http://localhost:5000

## Project Outlook
<br>

![Screenshot 2024-08-29 053057](https://github.com/user-attachments/assets/55d25748-3a1c-4e20-a15c-f159d6e31add)<br>
![Screenshot 2024-08-29 053112](https://github.com/user-attachments/assets/6e1afbc4-4b0b-4a8f-b933-7137f3540103)
