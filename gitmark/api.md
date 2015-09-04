##Starring

###List Stargazers

```
GET /repos/:repo_id/stargazers
```

###List repositories being starred

List repositories being starred by a user.

```
GET /users/:user_id/starred
```

List repositories being starred by the authenticated user.

```
GET /user/starred
```

###Star Activitiy

```
/user/starred/:repo_id
```

####Check if you are starring a repository

```
GET /user/starred/:repo_id
```

####Star a repository

```
PUT /user/starred/:repo_id
```

####Unstar a repository

```
DELETE /user/starred/:repo_id
```

