# My Web App

This project is a web application that allows users to search for and play audio files. It consists of a Python backend and a feature-rich frontend framework, hosted in a Docker container on AWS. Audio files are stored in an S3 bucket.

## Project Structure

```
my-web-app
├── backend
│   ├── app.py               # Main entry point for the backend application
│   ├── requirements.txt      # Python dependencies for the backend
│   └── Dockerfile            # Dockerfile for building the backend image
├── frontend
│   ├── src
│   │   ├── index.html       # Main HTML file for the frontend
│   │   ├── index.js         # JavaScript code for the frontend
│   │   └── styles.css       # CSS styles for the frontend
│   ├── package.json         # npm configuration for the frontend
│   └── webpack.config.js    # Webpack configuration for bundling the frontend
├── aws
│   ├── s3_setup.py          # Code to set up and manage S3 bucket
│   └── ecs_setup.py         # Code to set up AWS ECS for deployment
├── README.md                # Project documentation
└── .gitignore               # Git ignore file
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-web-app
   ```

2. **Backend Setup:**
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```
   - Build the Docker image:
     ```
     docker build -t my-backend .
     ```
   - Run the Docker container:
     ```
     docker run -p 5000:5000 my-backend
     ```

3. **Frontend Setup:**
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```
   - Start the frontend application:
     ```
     npm start
     ```

4. **AWS Setup:**
   - Configure the S3 bucket using `aws/s3_setup.py`.
   - Deploy the application using `aws/ecs_setup.py`.

## Usage Guidelines

- Access the web application at `http://localhost:5000`.
- Use the search functionality to find audio files and play them directly from the web app.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.