import requests
UPLOAD_STATUS_API = "http://example.com/api/upload/status"
METADATA_API = "http://example.com/api/video/metadata"
PLAYBACK_METADATA_API = "http://example.com/api/video/playback"

def test_upload_status():
    video_id = "12345" 
    response = requests.get(f"{UPLOAD_STATUS_API}?video_id={video_id}")
    assert response.status_code == 200, "Upload status API failed"
    data = response.json()
    assert "status" in data,"Status key missing in response"
    print("Upload status:", data["status"])

def test_metadata_fetch():
    video_id = "12345"
    response = requests.get(f"{METADATA_API}?video_id={video_id}")
    assert response.status_code == 200, "Metadata API failed"
    data = response.json()
    assert "title" in data and "description" in data,"Metadata fields missing"
    print("Metadata fetched:", data)

def test_playback_metadata():
    video_id = "12345"
    response = requests.get(f"{PLAYBACK_METADATA_API}?video_id={video_id}")
    assert response.status_code == 200, "Playback metadata API failed"
    data = response.json()
    assert "duration" in data and "thumbnail" in data,"Playback metadata missing"
    print("Playback metadata:", data)
