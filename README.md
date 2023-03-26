# Pavan-s_audiobook

Pavan's Audiobook in Python is a Python program that converts any PDF file into an audiobook. It uses the PyPDF2 library to extract text from the PDF file and the pyttsx3 library to convert the text into an audio file. The program allows the user to select the desired PDF file and choose the speed and volume of the audiobook. It also provides the option to select the voice of the reader, including both male and female voices. This audiobook creator is an excellent tool for individuals who prefer to listen to books rather than read them, making it ideal for people who are visually impaired or have difficulty reading.


# Dockerised file

I have created a docker file with all the details to use docker use below commands.


<h2> To build the Docker image, navigate to the directory with the Dockerfile and run </h2>

<li>To build the Docker image, navigate to the directory with the Dockerfile and run </li>

<ol>
  <br>
  <li>docker build -t pavankumar-scraper . </li>
</ol>
<br>
<br>

<li>  run the program in a Docker container </li>

<ol>
  <br>
  <li>docker run -p 80:80 pavankumar-scraper </li>
</ol>

