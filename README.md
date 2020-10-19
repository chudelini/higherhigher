# higherhigher

Code represents simplification of recruitment platform.
Admin can provide Candidates/Recruiters/Tasks/Grades to the Admin Platform, while end user can add a mark only.

Application is deployed into Heroku: https://higherhigher.herokuapp.com

EndPoints:
- "/" returns JSON in the following format:
``` 
    {
        "data": [
            {
                "pk": 1,
                "full_name": "Jan Kowalski",
                "avg_grade": 4.25,
                "grades": [4, 5, 5, 3]
            }
        ]
    }
```
- "/admin" returns login page to AdminPage
- "/api/add-mark/" returns form to be filled by enduser (grading) and data sent to DB
