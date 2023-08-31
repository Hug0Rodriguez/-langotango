# LangoTango Project Documentation
##### Team Members
- Andrew
- Beau
- Hugo
- Peter

## Project Intent

### Background

When brainstorming for the project, Beau pointed out that languages apps like Duolingo are very heavy on vocab and grammar, but don't do a good job at giving the user speaking practice. He had a great idea for a langauge app that would allow the user to speak in a foreign language and receive a response back in-language.

### Application Objective

We want to provide an application, as stated above, that allows users to practice their target language conversationally. To this end, we have designed our application so that, building on our MVP, users will have features available to them that help them improve their conversational abilities with well-paced feedback in an environment that makes the learner  feel safe and comfortable.

## MVP Criteria

Our application must, at minimum:

- Allow users to provide audio input in at least two languages
- Convert user speech into text
- Send a message to a chatbot and receive a response in target language
- Convert the text response back into audio
- Push the audio data back to the front end for the user

## Stretch Goals

- [ ] Conversation Histories
- [ ] Update Account Endpoint
- [ ] Audio Histories
- [ ] Application Language
- [ ] Deploying to AWS
- [ ] Difficulty Setting
- [ ] Corrections
- [ ] English translations
- [ ] In-Language text display
- [ ] Text Input
- [ ] Logo/Branding
- [ ] Demo on landing page
- [ ] Contact us page
- [ ] WebSockets?
- [ ] Premium features
- [ ] Limits by role
- [ ] Interactive background
- [ ] Themes
- [ ] Dynamic page styles
- [ ] On-Screen timer
- [ ] "Gamification", goals, objectives, daily benchmarks
- [ ] Cross-platform compatability
- [ ] MORE LANGUAGES, MORE FLAGS

## APIs, Frameworks, and Libraries

### In-House

FastAPI

- [Main Page](https://fastapi.tiangolo.com/)
- [Documentation](https://fastapi.tiangolo.com/)
- [Source Code](https://github.com/tiangolo/fastapi)
- [FastAPI Implementation](docs\tech-docs\FASTAPI_README.md)

MongoDB

- [Main Page]()
- [Mongo Documentation]()
- [Pymongo Documentation]()
- [Web Speech Implementation](docs\tech-docs\WEBSPEECHAPI_README.md)

React

- [Main Page](https://react.dev/)
- [Documentation](https://react.dev/reference/react)
- [Web Speech Implementation](docs\tech-docs\REACT_README.md)


### 3rd Party

Speech-to-Text: Browser Web Speech API (Chrome only)
- [Main Page](https://developer.mozilla.org/en-US/)
- [Documentation](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)
- [Web Speech Implementation](docs\tech-docs\WEBSPEECHAPI_README.md)

Chatbot: OpenAI ChatGPT Model 3.5
- [Homepage](https://platform.openai.com/)
- [Documentation](https://platform.openai.com/docs/api-reference/)
- [OpenAI Implementation](docs\tech-docs\OPENAI_README.md)

Text-to-Speech: React-Speech-Kit
- [Homepage](https://www.npmjs.com/)
- [Documentation](https://www.npmjs.com/package/react-speech-kit#install)
- [React Speech Kit Implementation](docs\tech-docs\RSK_README.md)
