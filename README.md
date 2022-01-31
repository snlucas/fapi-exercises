# fapi-exercises
Fast API Exercises!

## How to Run:
You can use Docker or run through your own environment.

**🐋 Using Docker:**

(Unavailable for now)
```sh
$ docker build -t fapi:latest .
$ docker run -it fapi:latest
```

**💻 Using Your Local Environment:**

First, create and activate a virtual environment:
```sh
$ python3 -m venv .venv
$ . .venv/bin/activate
```
Install dependencies:
```sh
$ pip install -U pip -r requirements.txt
```
*Run tests:*
```sh
$ pytest app
```
*Run app (change exercise number for each exercise):*
```sh
$ uvicorn app.exercise01.app:app --reload
```


**🚀 List of Exercises**
 1. CRUD in "Hello, World!" String:

    | Details                 | Method |
    | ----------------------- | ------ |
    | Create a String         | POST   |
    | Read the whole String   | GET    |
    | Update the String       | PUT    |
    | Delete the whole String | DELETE |
 
 2. Use Svelte in CRUD Hello, World!;
 3. Test Database;
 4. Authorization; 
 5. Scraping Bit is Myth Blog;
