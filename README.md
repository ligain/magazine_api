# Simple Magazine API
The magazine has three groups of users: 	`Editors`, `Users` and `Journalists`.
Journalists can add posts and edit own ones.
`Editors` can approve `Journalists`	 posts and edit/delete them.
Users can read posts approved by `Editors`

### Up and running
Before setting up the project you have to install [git](https://git-scm.com/) and [docker](https://www.docker.com/).
```
$ git https://github.com/ligain/magazine_api
$ cd magazine_api/
$ docker build -t username/magazine .
$ docker run -p 8000:8000 username/magazine
```
### Usage
Swagger doc is avaliable here: http://0.0.0.0:8000/api-doc/
#### Get auth token for user
```
$ curl -X POST -d "email=superadmin@example.com&password=sdf#DFDf1212" "http://0.0.0.0:8000/api-token-auth/"
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN1cGVyYWRtaW5AZXhhbXBsZS5jb20iLCJleHAiOjE1NDI5ODY5MzksImVtYWlsIjoic3VwZXJhZG1pbkBleGFtcGxlLmNvbSJ9.CdF2cdns4nC1wLYCoVJ8XzsIcsiHQdx0B1oH0wm_q0U"}
```
#### Get user profile by token
```
$ curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN1cGVyYWRtaW5AZXhhbXBsZS5jb20iLCJleHAiOjE1NDI5ODc5OTIsImVtYWlsIjoic3VwZXJhZG1pbkBleGFtcGxlLmNvbSJ9._aeByl9Qj0GA42ZOJUUAdFPG7eklPCzFPvoN-hP_syo" "http://0.0.0.0:8000/api/users/1/"
{
	"id": 1,
	"email": "superadmin@example.com",
	"is_admin": true
}
```
#### Create post by token (for `Editors` and `Journalists`)
```
$ curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN1cGVyYWRtaW5AZXhhbXBsZS5jb20iLCJleHAiOjE1NDI5OTczNDcsImVtYWlsIjoic3VwZXJhZG1pbkBleGFtcGxlLmNvbSJ9.WXvcHqoemIXEwtxmnCG7wxblAigUzLUkjQfRyyfe1fM" -d "title=Some title2&body=new post body2" "http://0.0.0.0:8000/api/posts/"
{
	"title": "Some title2",
	"body": "new post body2",
	"created_at": "2018-11-23T18:18:02.149499Z",
	"is_published": false,
	"author": 1
}
```
#### Get posts (for `Editors` and `Journalists`)
`Editors` can view all posts
`Journalists` can view only their own posts
`Users` can view only published posts

Request for `Editors` and `Journalists`:
```
$ curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMiwidXNlcm5hbWUiOiJqb3VybmFsaXN0QGV4YW1wbGUuY29tIiwiZXhwIjoxNTQzMDAxMDI0LCJlbWFpbCI6ImpvdXJuYWxpc3RAZXhhbXBsZS5jb20ifQ.gAS8vBxYCGdanun13FCu7nf2ayvGhis4sKkQ0E1pBMU" "http://0.0.0.0:8000/api/posts/"
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [{
		"title": "Some title",
		"body": "new post body",
		"created_at": "2018-11-23T18:03:34.544481Z",
		"is_published": false,
		"author": 12
	}]
}
```

Request for others:
```
$ curl -X GET "http://0.0.0.0:8000/api/posts/"
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [{
		"title": "Oil price plummets to low not seen since October 2017",
		"body": "The oil price has slumped to its lowest point this year, as concerns mount about a glut of crude supply and fears that economic headwinds could lessen demand.\r\n\r\nBrent crude fell as low as $59.26 a barrel on Friday, a level last seen in October 2017.",
		"created_at": "2018-11-23T15:52:27Z",
		"is_published": true,
		"author": 11
	}]
}
```
#### Search inside post body and title
```
$ curl -X GET "http://0.0.0.0:8000/api/posts/search/?q=some"
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [{
		"title": "Some title",
		"body": "new post body",
		"created_at": "2018-11-23T18:03:34Z",
		"is_published": true,
		"author": 12
	}]
}
```
### Project Goals
This is a test project for Archer company.
