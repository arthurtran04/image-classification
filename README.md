# Image Classification Application using pre-trained ResNet-18 model

## Introduction

This repository features an **Image Classification Application** built on the **ResNet-18 model**, leveraging pre-trained weights for efficient and accurate classification. Developed entirely in **Python**, this project highlights the power of transfer learning in simplifying complex image recognition tasks. It's a practical tool for exploring deep learning in image classification!

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- ![Python 3.9](https://img.shields.io/badge/Python-3.9-blue) or above: [Download here](https://python.org/downloads)

## Project Structure

```
image-classification/
├── .gitignore
├── image_classification.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Features

- Image Captioning Application using pre-trained ResNet-18 model
- Using Gradio UI

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```sh
    $ git clone https://github.com/arthurtran04/image-classification.git
    ```

2. Change the directory to `image-classification`:

    ```sh
    $ cd "$(find . -type d -name "image-classification")"
    ```

3. Create a Python virtual environment `venv` and install the required dependencies:

    ```sh
    $ python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the `image_classification.py` file:

   ```sh
   $ python image_classification.py
   ```
This application will run locally at `http://127.0.0.1:7860`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/c81f14b7-3c18-44ba-97b6-747ab46a476b"/>

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/af441881-7525-4ca1-908d-06180f77a904"/>

Upload your photo in the left box and click **Submit** button, The application will generate classifications with percentages of probability of matching your photo in the right box:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/fa4aebaa-c944-44f8-b513-a4b839bebcda"/>

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
