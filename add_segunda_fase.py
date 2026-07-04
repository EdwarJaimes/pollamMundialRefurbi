import json
import urllib.request
import urllib.error
import ssl

matches = [
    ("2026-06-28T14:00:00-05:00", "South Africa", "Canada"),
    ("2026-06-29T12:00:00-05:00", "Brazil", "Japan"),
    ("2026-06-29T15:30:00-05:00", "Germany", "Paraguay"),
    ("2026-06-29T20:00:00-05:00", "Netherlands", "Morocco"),
    ("2026-06-30T12:00:00-05:00", "Ivory Coast", "Norway"),
    ("2026-06-30T16:00:00-05:00", "France", "Sweden"),
    ("2026-06-30T20:00:00-05:00", "Mexico", "Ecuador"),
    ("2026-07-01T11:00:00-05:00", "England", "DR Congo"),
    ("2026-07-01T15:00:00-05:00", "Belgium", "Senegal"),
    ("2026-07-01T19:00:00-05:00", "USA", "Bosnia-Herzegovina"),
    ("2026-07-02T14:00:00-05:00", "Spain", "Austria"),
    ("2026-07-02T18:00:00-05:00", "Portugal", "Croatia"),
    ("2026-07-02T22:00:00-05:00", "Switzerland", "Algeria"),
    ("2026-07-03T13:00:00-05:00", "Australia", "Egypt"),
    ("2026-07-03T17:00:00-05:00", "Argentina", "Cape Verde"),
    ("2026-07-03T20:30:00-05:00", "Colombia", "Ghana")
]

for idx, (dt, home, away) in enumerate(matches, 1):
    doc_id = f"sf_{idx}"
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

