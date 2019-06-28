# Alexa Skill - 2019 Women World Cup update

## Info 

The Women World Cup 2019 starts on Friday, June 7th, 2019! This is the 8th Women's World Cup! Never miss a moment of the game: this Amazon Alexa skill will keep you up-to-date with the daily schedules of the game, highlighting the city and stadium that host each game. In addition, this app will use the abundance of memories from previous tournaments, enabling fans to re-live past World Cup history from the last 28 years! Connecting the past to the prsent, the app tell which team played this day, who won, who score in which tournament. Stay up-to-date with each day's schedule, and remember the previous world cup. 

The "Women World Cup Updates Skill" is an Amazon Alexa's skill that tells the user game information and history of the Women World Cup. When activating the skill, Alexa will report which day of tournament competition, the teams are playing, the local time of the game, the city hosting the game, and the name of the stadium. 

For example: 
`Today is day 3 of 25 of the Women's World cup in France. 
Today, Australia plays Italy at 05:00 AM in Stade du Hainaut stadium in Valenciennes.
Brazil plays Jamaica at 07:30 AM in Stade des Alpes stadium in Grenoble.
England plays Scotland at 10:00 AM in Stade de Nice stadium in Nice.
`

The second part of the skill tells a history from the same day of tournament from previous 8 Women World Cup. Alexa tells the World Cup year, the team, the final score, and the goal scorers. 

For example: 
`Today in history, Norway played Canada to a score of 7 to 1 in Women's World Cup USA 1999, scored for Norway by Hege RIISE,Ann Kristin AARONES,Linda MEDALEN,Marianne PETTERSEN,Unni LEHN,Solveig GULBRANDSEN, scored for Canada by Charmaine HOOPER`

## How to Use

To activate the skill, say "Alexa, open women world cup updates skill". After Alexa have reported on the day's game schedule and a history, you can tell Alexa to return more history from the day, or repeat the day's game schedule ("tell me today's schedule")

Timezone is currently hard-coded as 'America/New York'

## Runnig the Skill 

### Option 1) 

Find and enable the "Women World Cup Update and History" skill from Alexa store on mobile or Amazon Alexa devices. [link to Skill store](https://skills-store.amazon.com/deeplink/dp/B07SVWXJ6H?deviceType=app&share&refSuffix=ss_copy)

![Alexa skill](/img/alexa-skill.png)

### Option 2)

Sign in at `https://developer.amazon.com/alexa`

email: haitansle@gmail.com
password: <FIFA.....>

Select `Alexa` tab, then `Alex Skill Set`

Select `Women World Cup Update and History` skill under Alexa Skills

Then select `Test` tab. Here you can test the app. Type or say "women world cup updates" in the input box, to activate the Alexa skill. Alexa will start and prompt you for the next command (see screenshot below)

![Developer Console](/img/developer-console.png)

### Option 3) 

To run, create an Alexa skill, then copy the `output.json` file into the alexa developer console under the JSON Editor tab. 

Then, create a lambda function in AWS. Copy all files inside 'alexa-voice-fifa' directory to the function code. 'Save' the code. 

Connect the Alexa Skill to the lambda function..




