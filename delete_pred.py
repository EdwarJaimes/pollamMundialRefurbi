import json
import urllib.request
import urllib.error
import os

# Load matches
try:
    with open('matches.json', 'r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error reading matches.json: {e}")
    exit(1)

match_id = None
for doc in data.get('documents', []):
    fields = doc.get('fields', {})
    local = fields.get('local', {}).get('stringValue')
    visitante = fields.get('visitante', {}).get('stringValue')
    
    if (local == 'Argentina' and visitante == 'Jordan') or (local == 'Jordan' and visitante == 'Argentina'):
        if not fields.get('procesado', {}).get('booleanValue'):
            match_id = fields.get('idEvent', {}).get('stringValue')
            break

if not match_id:
    print("Match not found or already processed.")
    exit(1)

print(f"Found match ID: {match_id}")

users = ['julian', 'Julian']

for u in users:
    pred_id = f"{u}_{match_id}"
    url = f"https://firestore.googleapis.com/v1/projects/results-9212d/databases/(default)/documents/predicciones/{pred_id}"
    
    req = urllib.request.Request(url, method='DELETE')
    try:
        urllib.request.urlopen(req)
        print(f"Deleted prediction {pred_id}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Prediction {pred_id} not found (already deleted or never existed)")
        else:
            print(f"Error deleting {pred_id}: {e.code}")
    except Exception as e:
        print(f"Exception deleting {pred_id}: {e}")
