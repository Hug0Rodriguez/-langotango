W14D2
Spent today implemeting a delete and login/logout endpoint.
Ran into 3 hour issue because the boilerplate code we copied was ne\ot relevant.
We tried to fix bugs related to "SessionQueries" because we believed that it was related to login. SessionQueries is in fact, related to websockets. We will put that on the backburner.
Delete user and login/logout seem to be working. We must now ensure that the user info stored is in the correct mold a la hashed password.
