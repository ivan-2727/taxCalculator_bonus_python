# Python solution for bonus scenario of Congestion Tax Calculator 

The solution implements Python 3. 

For necessary packages:
- `pip3 install -r requirements.txt` 

To run app on localhost:5000 and use hardcoded tax rules from file localTaxRules:
- `FLASK_APP=server.py FLASK_ENV=development flask run`  

To fetch tax rules from Mongo DB (credentials provided within the code, without env file):
- `FLASK_APP=server.py FLASK_ENV=production flask run`  

 The request can be run via postman. Below is an example of JSON with data for which the tax should be calculated. It is in array of objects, one object per each vehicle, with properties `vehicle` for vehicle type and `dates` for the array of dates in usual human-readable format. The dates from assgnment.md were used. 

```
[
    {
        "vehicle": "A",
        "dates": [
            "2013-01-14 21:00:00",
            "2013-01-15 21:00:00",
            "2013-02-07 06:23:27",
            "2013-02-07 15:27:00",
            "2013-02-08 06:27:00"
        ]
    },
    {
        "vehicle": "tRaCtOr",
        "dates": [
            "2013-02-08 06:20:27",
            "2013-02-08 14:35:00",
            "2013-02-08 15:29:00",
            "2013-02-08 15:47:00",
            "2013-02-08 16:01:00"
        ]
    }
]
```

Response will be an array of numbers, one fee per each vehicle.