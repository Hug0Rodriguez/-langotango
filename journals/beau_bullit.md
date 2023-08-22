W14D2
Spent today implemeting a delete and login/logout endpoint.
Ran into 3 hour issue because the boilerplate code we copied was ne\ot relevant.
We tried to fix bugs related to "SessionQueries" because we believed that it was related to login. SessionQueries is in fact, related to websockets. We will put that on the backburner.
Delete user and login/logout seem to be working. We must now ensure that the user info stored is in the correct mold a la hashed password.

W14D3
Today we tested the authentication endpoints. We noticed that the User models had a visible password field so we deleted the password property within the account querie. Lastly, we started in depth research on the api's we want to use. WE began reading their documentation to figure out how integrateable they were.

W15D1
Today we experimented with apis that convert audio to text. We were able to integrate whisper after 2 hours and get sucessful text responses. After lunch, Peter found an easier way of speech to text with "Diction"/"Dictation". We are now in the process of integrating a messaging queue so for our apis talking to each other.
