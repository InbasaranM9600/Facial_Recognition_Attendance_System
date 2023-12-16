import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate ("fras-f7624-firebase-adminsdk-84x15-c040043db0.json" )
firebase_admin.initialize_app ( cred, {
    'databaseURL': "https://fras-f7624-default-rtdb.firebaseio.com/"
} )

ref = db.reference ( 'Students' )

data = {
    "104007":
        {
            "name": "Inbasaran M",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104029":
        {
            "name": "Sureshkumar G",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104013":
        {
            "name": "Karupaiyya",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104015":
        {
            "name": "Magehwaran",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104024":
        {
            "name": "SenthilKumar.v",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104022":
        {
            "name": "Samual",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104023":
        {
            "name": "Aravinth.S",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104030":
        {
            "name": "Thanesh",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        },
    "104024":
        {
            "name": "FelixMon.B.S",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-24 00:09:34"
        }
}

for key, value in data.items ():
    ref.child ( key ).set ( value )
