<h1 align="center">Maintenance Bot</h1>
<p align="center">
  <a href="https://github.com/HeimanPictures/Maintainance-Bot">
    <img src="https://github.com/HeimanPictures/Maintainance-Bot/blob/master/Maintainance-Bot.png" alt="Cover Image" width="200">
  </a>
<p align="center">
  <a href="https://github.com/HeimanPictures/Maintainance-Bot">
  </a>
  <p align="center">
    A Telegram Repo For Bots Under Maintenance
    <br />
    <a href="https://telegram.dog/HeimanSupport"><strong>Requests »</strong></a>
    <br />
    <a href="https://github.com/HeimanPictures/Maintainance-Bot/issues">Report a Bug</a>
    |
    <a href="https://github.com/HeimanPictures/Maintainance-Bot/issues">Request Feature</a>
  </p>
</p>

<hr>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-this-bot">About this Bot</a>
    </li>
    <li>
      <a href="#how-to-make-your-own">How to make your own</a>
      <ul>
        <li><a href="#deploy-on-heroku">Deploy using Heroku</a></li>
        <li><a href="#host-it-on-vps-or-locally">Run it in a VPS / local</a></li>
      </ul>
    </li>
    <li><a href="#setting-up-things">Setting up things</a></li>
    <ul>
      <li><a href="#mandatory-vars">Mandatory Vars</a></li>
    </ul>
    <li><a href="#how-to-use-the-bot">How to use the bot</a></li>
    <li><a href="#to-be-added">To Be Added</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>


## About This Bot

<p align="center">
    <a href="https://github.com/HeimanPictures/Maintainance-Bot/">
        <img src="https://telegra.ph/file/b15170ea0826d49c730a3.png" height="200" width="200" alt="Telegram Logo">
    </a>
</p>
<p align='center'>
    This Bot Is For Developers, If Your Bot Is Down, Use This Repo To Give Your Dear Subscribers Some Support By Providing Them Response.
</p>


## How to make your own

Either you could locally host or deploy on [Heroku](https://heroku.com)

### Deploy on Heroku

Press the below button to Fast deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HeimanPictures/Maintainance-Bot/tree/master/)

then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables.

### Host it on VPS or Locally

```sh
git clone https://github.com/HeimanPictures/Maintainance-Bot
cd Maintainance-Bot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m plugins
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

## Setting up things

If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:

```sh
APP_ID=123456
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=12345678:yourtbottokenhere
UPDATE_CHANNEL=https://t.me/HeimanSupports
SUPPORT_GROUP=https://t.me/HeimanSupport
AUTH_USERS=your_user_id
MAINTAINANCE_TEXT=your-text
WEBHOOK=ANYTHING (Keep It Default)
```

### Mandatory Vars

`APP_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`UPDATE_CHANNEL` : Your Telegram Channel Link

`SUPPORT_GROUP` : Your Telegram Support Group Link

`AUTH_USERS` : The ID of the Owner or Maintainer


## How to use the bot

`/start` : To check if the bot is alive or not.

Check This [Click Here](#about-this-bot)

## To Be Added:
- Added Broadcast Feature!
- Made Better Bin Channel Logging!

## Credits

- [Heiman Creation](https://github.com/HeimanPictures/)
