## Overview
- Serve as practising project. Will add more contents as I progress
- This directory is a virtual environment created using venv, with command `python -m venv venv`.
- Inside hello.py is my first Flask application that prints Hello World on browser using the given URL.
- Inside make_requests.py, I made GET request (form) and POST request using  `request` from Flask library

## Steps: Hello World
1. Create virtual environment, with the name `venv` and activate it.

2. Create the app in hello.py

3. Run hello.py

![run](https://user-images.githubusercontent.com/92832451/191206039-7a95f65d-718d-4ec5-802e-286721b12644.png)

4. Open my application in browser using the address given.

![app](https://user-images.githubusercontent.com/92832451/191206396-32b5ffd9-bc08-4aa3-b868-09b421afd4bf.png)


## Different Ways to Specify Routes
1. Main Page

![image](https://user-images.githubusercontent.com/92832451/191213313-a730fd63-57bb-4818-8136-9650daa6e0f2.png)


![image](https://user-images.githubusercontent.com/92832451/191213269-b669dcb6-3ccb-429e-9bf7-e80afeaba84f.png)

2. Same Contents for More than One Route

![image](https://user-images.githubusercontent.com/92832451/191213579-4a002ec0-b0e3-4c29-a148-b40371301e97.png)


![image](https://user-images.githubusercontent.com/92832451/191213425-6341d65c-c0fc-4979-9e77-271aaaef7aab.png)

![image](https://user-images.githubusercontent.com/92832451/191213525-a5a303f8-20d7-412d-b753-b58130bdda27.png)


3. Template

![image](https://user-images.githubusercontent.com/92832451/191213673-6659cfdf-aff4-4124-9c39-9240989ca995.png)

![image](https://user-images.githubusercontent.com/92832451/191213749-19751975-ec2f-47ea-a2bd-fb0e813eb28d.png)

![image](https://user-images.githubusercontent.com/92832451/191213827-0baa5613-2cc8-4b1b-a0de-67a3423b6a95.png)

![image](https://user-images.githubusercontent.com/92832451/191214009-8898b96c-bb12-4522-a860-1805dada3b07.png)

![image](https://user-images.githubusercontent.com/92832451/191214068-d4c75721-43ea-481a-a369-a1a810a5c104.png)


4. Type Conversion (data passed to URL is always a string, Conversion from string to other)

![image](https://user-images.githubusercontent.com/92832451/191216260-3f08a0ac-62d7-416e-b652-1769871b6caa.png)



## Make Requests (in make_requests.py)

How it looks like when I just opened the address link. (GET request by default)

![image](https://user-images.githubusercontent.com/92832451/191435071-71da964b-65bd-4711-9e6e-382c2ba7a0c6.png)

After click on button `auth`, application sent POST request

![image](https://user-images.githubusercontent.com/92832451/191435141-e4bb960c-9ad8-4bfa-b335-1c5940e6fbe5.png)

Records:

![image](https://user-images.githubusercontent.com/92832451/191436088-0045ca99-a7e0-4947-9085-5f89b725a6cf.png)

