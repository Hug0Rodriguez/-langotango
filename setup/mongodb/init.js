db.getSiblingDB('admin').auth('user', 'password')
db.accounts.createIndex({"username": 1}, {unique: true})
