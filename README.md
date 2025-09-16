# QA Mini-Project: Video Upload & Playback

## Project Overview
This project tests a simple video-hosting dashboard. The main objective is to ensure that users can:

- Sign in successfully
- Upload video files through the dashboard
- Add metadata (title, description, privacy settings)
- See processing progress and final status
- Play uploaded videos (thumbnail + playback)
- Share or delete videos

## Manual Test Cases

| #  | Test Scenario | Steps | Expected Result |
|----|---------------|-------|----------------|
| 1  | Happy Path Upload | 1. Login → 2. Upload valid video → 3. Add metadata → 4. Wait for processing → 5. Check thumbnail/playback | Video uploads successfully, thumbnail visible, playback works |
| 2  | Negative File Format | Upload unsupported file (e.g., .txt) | Error message appears, upload rejected |
| 3  | File Size Limit | Upload video larger than allowed | Upload rejected with clear error |
| 4  | Resume/Interrupted Upload | Simulate connection drop during upload | Either upload resumes or clear retry/error message appears |
| 5  | Edit Metadata | After upload, edit title/description | Changes persist and reflect in UI/API |
| 6  | Privacy/Share | Set video to private/public,generate share link | Access rules follow privacy setting |
| 7  | Deletion | Delete uploaded video | Video removed from UI/API |
| 8  | Invalid Metadata | Enter blank/invalid characters in metadata | Error shown, metadata not saved |
| 9  | Multiple File Upload | Upload multiple videos sequentially | All videos uploaded successfully, thumbnails/playback work for each |
| 10 | Cancel Upload | Start upload and cancel midway | Upload stops, no file saved |
| 11 | Playback on Different Devices | Play uploaded video on desktop/mobile | Video plays correctly without distortion/errors |
| 12 | Share Link Expiration | Generate share link with time limit | Link works during allowed time, inaccessible after expiry |
| 13 | Thumbnail Generation | Check if auto-generated thumbnail matches video | Correct thumbnail generated and displayed |
| 14 | Repeated Upload | Upload same video twice | System handles duplicate gracefully (reject or create new entry with notice) |
| 15 | Network Fluctuation | Upload video with slow/intermittent network | Upload retries/resumes or fails with clear error |
| 16 | Privacy Change After Upload | Change video privacy setting | Access rules update correctly in UI and share link | 


## Automation Tests

**1. Smoke Happy Path** – Upload valid video, check thumbnail & playback  
**2. Negative Upload** – Upload unsupported file, assert error  
**3. Metadata Verification** – Update/fetch metadata, assert values match  
