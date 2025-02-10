from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

# Initialize S3 client
s3_client = boto3.client('s3')
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

@app.route('/search', methods=['GET'])
def search_audio():
    query = request.args.get('query')
    # Logic to search for audio files in S3
    # This is a placeholder for actual search implementation
    audio_files = []  # Replace with actual search results
    return jsonify(audio_files)

@app.route('/play/<filename>', methods=['GET'])
def play_audio(filename):
    # Logic to generate a presigned URL for the audio file
    try:
        url = s3_client.generate_presigned_url('get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': filename},
            ExpiresIn=3600)  # URL valid for 1 hour
        return jsonify({'url': url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)