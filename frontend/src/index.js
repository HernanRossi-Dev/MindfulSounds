const audioApiUrl = 'http://localhost:5000/api/audio'; // Replace with your backend API URL

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const audioList = document.getElementById('audio-list');

    searchButton.addEventListener('click', async () => {
        const query = searchInput.value;
        if (query) {
            const response = await fetch(`${audioApiUrl}/search?query=${encodeURIComponent(query)}`);
            const audioFiles = await response.json();
            displayAudioFiles(audioFiles);
        }
    });

    function displayAudioFiles(audioFiles) {
        audioList.innerHTML = '';
        audioFiles.forEach(file => {
            const listItem = document.createElement('li');
            listItem.textContent = file.name;
            listItem.addEventListener('click', () => playAudio(file.url));
            audioList.appendChild(listItem);
        });
    }

    function playAudio(url) {
        const audioPlayer = document.getElementById('audio-player');
        audioPlayer.src = url;
        audioPlayer.play();
    }
});