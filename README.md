<h1 align='center'><a href='https://ptorr-api.herokuapp.com/'>PTORR-API</a></h1>
<p>
Welcome to <a href='https://ptorr-api.herokuapp.com/'><b>PTORR-API</b></a>, a RESTful API for torrents!

**NOTE:**
 This Project is just for educational purpose (of mine), It doesn't encourage the pirated content avaiable on the internet! 

</p>

# INDEX

- [Hosting API locally](#Hosting-the-API-locally)
- [Setting up development enviornment](#How-to-set-up-the-development-environment)
- [Modules used](#Stack)
- [Route Methods](#Methods)
- [To contribute to the project](#How-to-contribute)
## Hosting the API locally:

**NOTE**: To replicate, you will need **CREDENTIALS**. Go get yours at by signing up [here](https://www.chd4.com/) (If you need help with this step, feel free to ask for help in our [Support Server](https://discord.gg/FjVVkTtbgp)

- Clone this repo using `git clone`
- cd into the bot folder.
- Add the token in a `.env` file in the project root as follows:

```text
UNAME=<your username>
PSWRD=<your password>
```

- Install the `pipenv` via `pip install pipenv` and then run:

```
pipenv install
```

- Enjoy! 
- You may do bug-reporting or ask for help in on the SupportServer... or just open an issue on this repo.
## How to set up the development environment

#### Requirements:
- git
- pip
- python `3.8.6` or higher

1. Fork and clone the repository with `git clone https://github.com/<your-username>/ptorr-api`
2. Get to the clone directory using the command `cd ptorr-api`
3. Copy the contents of the `.env.sample` file into a new file - `.env` and add your DISCORD bot token in there.
4. Now follow these steps

   (Requires [pipenv](https://pipenv.pypa.io/en/latest/))
   \- Install pipenv\
   \- Run `pipenv sync --dev` to install project dependencies and development dependencies\
   \- Run `pipenv run start` to run the bot.\
   \- For downloading more libraries, use `pipenv install <package-name>`\
   \- If you're adding any development-dependencies, use-> `pipenv install <package-name> --dev`\


## How to contribute

Before contributing, here is some information that might help your **PR (Pull Request)** get merged.


**Note**: For more detailed information about how to contribute, please refere to the [CONTRIBUTING.md](docs/CONTRIBUTING.md) file.

### To contribute changes follow these steps:

**Note**: Make sure you have been assigned the issue to which you are making a PR. If you make PR before being assigned, It will be labeled invalid and closed without merging.

1. Add a upstream link to main branch in your cloned repo

```
git remote add upstream https://github.com/pvcodes/pi_bot.git
```

2. Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

```
git pull upstream master
```

3. Create your feature branch

```
git checkout -b <feature-name>
```

4. Commit all the changes

```
git commit -am "Meaningful commit message"
```

5. Push the changes for review

```
git push origin <branch-name>
```

6. Create a PR from our repo on Github.

### How to report a bug

Submit an issue on GitHub and add as much information as you can about the bug, with screenshots of inputs to the bot and bot response if possible (if the issue is regarding bugs).

## Stack:

- python 3
- requests
- BeautifulSoup4

## Methods
### Response Object Example:
- #### SUCCESS RESPONSE
```text
{
   "_status": "OK",
    "result": [
        {
            "id": "torr-id",
            "title": "torr-tile",
            "size": "torr-size",
            "imdb": "torr's imdb link"
    
        }
    ]
}
```

- #### ERROR RESPONSE
```text
{
   "_status": "ERROR",
    "result": [
       "message" : "Error Message"
    ]
}
```



**&#10158; Get Torrs :**
----
  Returns json data containing the torr id's and title's.

* **URL**

  /key=keyword&maxCount=max_reponse_object

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `keyword=[string]` or `k=[string]`

   **Optional:**
   
   `maxCount=[integer]` or `mx=[integer]`

**&#10158; Get Recent Torrs :**
----
  Returns json data containing the torr id's and title's.

* **URL**

  /recent or /r 

* **Method:**

  `GET`
  
*  **URL Params**
   
   - No Params required. 

**&#10158; Download Torr :**
----
  Returns a torrent file to 

* **URL**

  /getorr-torr-id   

* **Method:**

  `GET`
  
*  **URL Params**

   **Required**
   
   `torr-id=[string]`


* **Example**

   ![Alt Text](https://user-images.githubusercontent.com/54075838/118957373-18eaf000-b97e-11eb-9f2a-6bf98432cfd7.gif)







</p>

<div align="center">
<a href="docs/LICENSE.md"><img src="https://img.shields.io/github/license/pvcodes/ptorr-api/?style=flat-square" alt="MIT license"></a>
</div>
