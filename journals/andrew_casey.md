# The Days of Our Coding

## W14D1 - Auth - August 14th, 2023

```
Woke up this morning feeling fine; /
Had some fun code on my mind. /
Started with some stand-up with my team. /
Beau was driving; we were living the dream.
```

```
Hit some errors but we didn't care. /
Debugging like bosses, wind in our hair, /
Requests got 200s so we said, "That's it! /
Call it a day, save, add, commit.
```

```
Little did we know...
```

## W14D2 - Auth Strikes Back - August 15th, 2023

### A haiku

```
How could this happen?
All day just bugs and errors...
Betrayed by repos.
```

### For Real Though

```
At the end of the day, it seems we got auth working alright.
Got back the 200s for our create account requests, responses looked right.
Tomorrow we will re-attack and make sure login/logout work before working on endpoints for messages.
We also need to clean up our queries so that the hashed password is getting written to the db instead of the normal one.
```

## W14D3 - August 16th, 2023

### Auth

```
We completed auth today and ensured that get token, login, logout, and create user all work as expected.
We merged the branch into main and closed out the relevant issues.
```

### Messages

```
We began writing models for our messages, but quickly realized that we need to actually clarify our intent for data flow and API usage.
We spent much of the afternoon doing additional research and agreed that by COB tomorrow we would have our APIs chosen and documented.
```

## W14D4 - August 17th, 2023

### Planning

```
Today we spent most of the afternoon in planning and discussion. Our goal was to select and agree on our APIs for speech-to-text, text-based chatbot conversation, and text-to-speech.
Following afternoon attendence, we had our end-of-day meeting to settle our decisions and document our plan and MVP in the README. We also wrote down our extensive stretch goal list.

To end our planning, we set realistic timetables to achieve our MVP in the next two weeks.
We agreed that, by the end of next week, we would have API endpoints completed so that we can send requests using Swagger UI to our APIs and get responses back. By the end of the week after we will need to have complete integration between front and back ends.
```

## W15D1 - August 21st, 2023

### Whispe- Oh, nevermind

```
We spent much of today trying to properly configured and implement Whisper API, and then Peter figured out a really easy way to do Speech-to-Text in the browser and we threw all our efforts away. Not that I'm bitter.
We thought of using RabbitMQ to send messages from the post router function to a consumer so that we don't have to handle all the API requests in our router function.
```

## W15D2 - August 22nd, 2023

### More Confusion

```
We spent a lot of time today dealing with git confusion and figuring out how to set everything up to receive from front end.
Our goal for tomorrow is to get responses working from Bard and establish RabbitMQ messaging.
```

## W15D3 - August 23rd, 2023

### The Bard and The Rabbit

```
We made good headway early in the day in getting successful HTTP responses. We got Bard to give us successful text responses.
We got hung up on getting a Rabbit consumer to work. Took a break in late afternoon to research better methods.
```

## W15D4 - August 24th, 2023

### House of Bard Troubles

```
I was not present for groupwork today because of a wedding, but the group discovered a potential alternative to Google text-to-speech.
They also tried implementing WebSockets.
```

## W15D5 - August 25th, 2023

### Moving On

```
We decided this morning to move on from RabbitMQ andWebSockets, especially because the
React Text-to-Speech toolkit rendered the return of chatbot text with the http response
viable. No need for event messages, background texts, or back-to-front forced messages.
Wealso abandoned Bard in favor of OpenAI's chat models.
```

## W16D1 - August 28th, 2023

### We Have Words!

```
Today we made great headway in bring together all of our different functionality plans.
OpenAI is giving us responses, we made progress in our database setup, and we havea solid foundation to finish up minimum functionality this week.
```

## W16D2 - August 29th, 2023

### Front-End Auth Success and DB Work

```
This morning after stand up we got right on front-end auth completion. Peter drove and we got
everything set up so that We were hitting all our endpoints, and the useToken hook is now controlling which auth buttons are visible based on token status.
We had to do a refactor because our App.js file was not being used in our index.js, so our baseUrl variable wasn't getting called by useToken.

After getting front-end auth finished, we moved on to query and model planning. We spent much of the late-afternoon plotting the course of our database.
```

[Here's a useful markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists "Markdown Cheatsheet")
