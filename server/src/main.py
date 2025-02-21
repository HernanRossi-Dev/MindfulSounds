import os
import boto3
import uvicorn
from fastapi import FastAPI

app = FastAPI()
s3_client = boto3.client('s3')
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

@app.get("/")
async def root():
    return {"message": "Default Route"}

@app.get('/search')
async def search_audio():
    # query = request.args.get('query')
    # Logic to search for audio files in S3
    # This is a placeholder for actual search implementation
    audio_files = []  # Replace with actual search results
    return {"message": 'Searched Audio Files'}

@app.get('/play/<filename>')
async def play_audio(filename):
    # Logic to generate a presigned URL for the audio file
    # try:
    #     url = s3_client.generate_presigned_url('get_object',
    #         Params={'Bucket': BUCKET_NAME, 'Key': filename},
    #         ExpiresIn=3600)  # URL valid for 1 hour
    #     return jsonify({'url': url})
    # except Exception as e:
    return {"message": 'Playing Audio files'}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="0.0.0.0", port=9000, reload=True)