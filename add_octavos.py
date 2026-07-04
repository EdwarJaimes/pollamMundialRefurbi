import json
import urllib.request
import urllib.error
import ssl

matches = [
    ("2026-07-04T12:00:00-05:00", "Canada", "Morocco"),
    ("2026-07-04T16:00:00-05:00", "Paraguay", "France"),
    ("2026-07-05T15:00:00-05:00", "Brazil", "Norway"),
    ("2026-07-05T19:00:00-05:00", "Mexico", "England"),
    ("2026-07-06T14:00:00-05:00", "Portugal", "Spain"),
    ("2026-07-06T19:00:00-05:00", "USA", "Belgium"),
    ("2026-07-07T11:00:00-05:00", "Argentina", "Egypt"),
    ("2026-07-07T15:00:00-05:00", "Switzerland", "Colombia")
]

for idx, (dt, home, away) in enumerate(matches, 1):
    doc_id = f"octavos_{idx}"
    payload = {
        "fields": {
            "idEvent": {"stringValue": doc_id},
            "fecha": {"timestampValue": dt},
            "local": {"stringValue": home},
            "visitante": {"stringValue": away},
            "ronda": {"stringValue": "Octavos de Final"},
            "procesado": {"booleanValue": False}
        }
    }
    
    url = f"https://firestore.googleapis.com/v1/projects/results-9212d/databases/(default)/documents/octavos/{doc_id}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='PATCH')
    
    try:
        context = ssl._create_unverified_context()
        urllib.request.urlopen(req, context=context)
        print(f"Patched {home} vs {away}")
    except urllib.error.HTTPError as e:
        print(f"Error {e.code}: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")
