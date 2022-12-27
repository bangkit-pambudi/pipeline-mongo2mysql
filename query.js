db.createCollection("vaksin_covid")

db.vaksin_covid.insertMany([{
    "_id" : "5ffdf9f4f90ec3ce06b1185f",
    "vaccinePatient" : {
        "profession" : "doctor",
        "fullName" : "Wiyaaaaa",
        "gender" : "M",
        "bornDate" : "1976-01-14",
        "mobileNumber" : "081212345678",
        "nik" : "3271041401761234"
    },
    "channel" : "umb",
    "createdAt" : ISODate("2021-01-13T02:35:16.904+07:00"),
    "updatedAt" : ISODate("2021-01-13T02:35:16.904+07:00"),
    "vaccination" : {
            "vaccineLocation" : {
                "name" : "KLINIK WASPADA (PASPAMPRES)",
                "faskesCode" : "N123456"
            },
            "vaccineCode" : "W-12345678",
            "vaccineDate" : "2021-01-13",
            "vaccineStatus" : 2,
            "type" : "second"
      }
  },
  {
    "_id" : "5ffdf9f4f90ec3ce06b11892",
    "vaccinePatient" : {
        "profession" : "teacher",
        "fullName" : "Veraaaaa",
        "gender" : "F",
        "bornDate" : "1990-09-13",
        "mobileNumber" : "089912345671",
        "nik" : "1105095309901232"
    },
    "channel" : "loket",
    "createdAt" : ISODate("2021-01-13T02:35:16.966+07:00"),
    "updatedAt" : ISODate("2021-08-14T04:05:00.307+07:00"),
    "vaccination" :
        {
            "vaccineDate" : "2021-01-13",
            "vaccineLocation" : {
                "name" : "KLINIK SETIA",
                "faskesCode" : "CC23456"
            },
            "vaccineCode" : "W-87654321",
            "vaccineStatus" : "2",
            "type" : "second"
        }
  },
  {
    "_id" : "5ffdf9f5f90ec3ce06b1197d",
    "vaccinePatient" : {
        "mobileNumber" : "085865432145",
        "nik" : "7106081105874322",
        "gender" : "M",
        "bornDate" : "1987-05-11",
        "profession" : "teacher",
        "fullName" : "Rudi Vero"
    },
    "updatedAt" : ISODate("2021-07-13T12:18:06.388+07:00"),
    "channel" : "loket",
    "createdAt" : ISODate("2021-01-13T02:35:17.254+07:00"),
    "vaccination" :
        {
            "vaccineCode" : "W-8F132142",
            "vaccineDate" : "2021-03-13",
            "vaccineLocation" : {
                "name" : "KLINIK WASPADA (PASPAMPRES)",
                "faskesCode" : "N123456"
            },
            "vaccineStatus" : 2,
            "type" : "first"
        }
  }]);

db.vaksin_covid.find({
    'updatedAt' :{
        $gte:ISODate('2016-06-05T00:00:00.163Z'),
        $lte:ISODate('2022-06-05T23:59:59.163Z')
    }
}).pretty();

//mongoexport --db codex -c vaksin_covid -q '{"updatedAt" :{$gte:ISODate("2016-06-05T00:00:00.163Z"),$lte:ISODate("2022-06-05T23:59:59.163Z")}' --out vaksin.json
//'''mongoexport --collection=vaksin --db=codex --out=/home/bagas/events.json'''
//mongoexport --collection=vaksin --db=codex --out=events.json
//docker exec -u 0 ba32fb19252c mongoexport --db codex -c vaksin --out dataexport2.json
//docker cp ba32fb19252c:/dataexport.json /home/bagas
//docker cp ba32fb19252c:/dataexport.json '/mnt/c/diary ngoding/Test Telkom/pipeline mongo to mysql/JsonOutput'
//mongoexport --db codex -c vaksin_covid -q '{ "updatedAt" :{"$gte":  {"$date": "2016-06-05T00:00:00.163Z"}, "$lte":  {"$date": "2022-06-05T23:59:59.163Z"}}}' --out vaksin.json