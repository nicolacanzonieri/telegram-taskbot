# Task Manager Bot

A simple task manager bot for Telegram.

This bot allows you to add, remove, and list tasks.

## Features

* Add tasks
* Remove tasks
* List tasks

## Usage

To add a task, send the following message to the bot:

```
/add Buy grocieries
```

To remove a task, send the following message to the bot:

```
/remove Buy grocieries
```

To show the list of your tasks, send the following message to the bot:

```
/list
```


## How can I run this bot on Telegram?


In the following lines you will be able to run this bot on a server for free!


### BotFather instructions


Open Telegram and search for `@BotFather` than run the command:

```
/newbot
```


and follow the instructions!


At the end you have to remember the: 
- the Bot username (for example `task_manager_bot` without the '@'),
- the Bot TOKEN (for example `639076465218:AAFHRUYvVsd4gSsdathO3hDiGVybCcT5xpK54`),
- your username (for example `your_username` without the '@')


**Remember that Bot Name is different from Bot Username!**


### Using PythonAnywhere to host your Bot 24/7 for free


Create an account to [PythonAnywhere](https://www.pythonanywhere.com) and inside your `Dashboard` click on `Files` (top-right edge of the window)


Than create a new file, for example `my_taskbot_telegram.py`


Once the editor opens, paste the code of `taskbot.py` that you can find by clicking on this file here on GitHub


Than you have to modify the lines 7-8-9-10 with the Bot Token, Bot username, Your username and your name.


In the end these lines should look more or less like this:

```
...
TOKEN: Final = '6390764218:AAFUSBUYvV894gSwhrhO3hDiHVybCcT5xpK54'
BOT_USERNAME: Final = 'task_manager_bot'
USER_USERNAME: Final = 'mark03'
CUSTOM_USERNAME: Final = 'Mark'
...
```


Than, at the bottom of the page, click on `$ Bash console here` and run the following command:

```
pip install python-telegram-bot
```


And wait untill the process is finished.


Than press `>>> Run` and when you see the following lines inside the console:

```
Starting Bot...
Polling...
```

it means that your Bot is **running** and you can use it on **Telegram**!
