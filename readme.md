### OPEN ALPR SERVER 
It contains OPEN ALPR tool + python env, the server is built on fastapi and only takes a few seconds to give you the places which have been found on the picture.

# Run  :running:

    docker-compose up  :)

# Docs  :books:

Go to localhost:8080/docs and you'll get the swagger info.


# Testing :white_check_mark:

![Testing picture](./image/OML670.jpg)


Checking the response you'll get the next one :heavy_check_mark:


    {
    "message": "Everything ok",
    "code": 200,
    "result": [
        {
        "plate": "0ML670",
        "confidence": 91.889153,
        "matches_template": 0,
        "plate_index": 0,
        "region": "wa",
        "region_confidence": 0,
        "processing_time_ms": 14.4907,
        "requested_topn": 7,
        "coordinates": [
            {
            "x": 847,
            "y": 567
            },
            {
            "x": 946,
            "y": 560
            },
            {
            "x": 948,
            "y": 630
            },
            {
            "x": 847,
            "y": 638
            }
        ],
        "candidates": [
            {
            "plate": "0ML670",
            "confidence": 91.889153,
            "matches_template": 0
            },
            {
            "plate": "0HL670",
            "confidence": 90.16832,
            "matches_template": 0
            },
            {
            "plate": "0NL670",
            "confidence": 89.01165,
            "matches_template": 0
            },
            {
            "plate": "0L670",
            "confidence": 86.896095,
            "matches_template": 0
            },
            {
            "plate": "OML670",
            "confidence": 82.758476,
            "matches_template": 0
            },
            {
            "plate": "QML670",
            "confidence": 82.09388,
            "matches_template": 0
            },
            {
            "plate": "DML670",
            "confidence": 81.866592,
            "matches_template": 0
            }
        ]
        }
    ]
    }