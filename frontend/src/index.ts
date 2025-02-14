import * as React from 'react';
import ReactDOM from 'react-dom';
import { AppBar, Toolbar, Typography, Drawer, List, ListItem, ListItemText, CssBaseline, Container, TextField, Button } from '@mui/material';

const drawerWidth = 240;

const audioApiUrl = 'http://localhost:5000/api/audio'; // Replace with your backend API URL

function App() {
    const [searchQuery, setSearchQuery] = React.useState('');
    const [audioFiles, setAudioFiles] = React.useState([]);

    const handleSearch = async () => {
        if (searchQuery) {
            const response = await fetch(`${audioApiUrl}/search?query=${encodeURIComponent(searchQuery)}`);
            const audioFiles = await response.json();
            setAudioFiles(audioFiles);
        }
    };

    return (
        <div style={{ display: 'flex' }}>
            <CssBaseline />
            <AppBar position="fixed" style={{ zIndex: 1201 }}>
                <Toolbar>
                    <Typography variant="h6" noWrap>
                        Mindful Sounds
                    </Typography>
                </Toolbar>
            </AppBar>
            <Drawer
                variant="permanent"
                style={{ width: drawerWidth, flexShrink: 0 }}
                PaperProps={{ style: { width: drawerWidth } }}
            >
                <Toolbar />
                <div style={{ overflow: 'auto' }}>
                    <List>
                        {['Option 1', 'Option 2', 'Option 3'].map((text, index) => (
                            <ListItem button key={text}>
                                <ListItemText primary={text} />
                            </ListItem>
                        ))}
                    </List>
                </div>
            </Drawer>
            <main style={{ flexGrow: 1, padding: '24px', marginLeft: drawerWidth }}>
                <Toolbar />
                <Container>
                    <TextField
                        id="search-input"
                        label="Search for audio files"
                        variant="outlined"
                        fullWidth
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        style={{ marginBottom: '16px' }}
                    />
                    <Button variant="contained" color="primary" onClick={handleSearch}>
                        Search
                    </Button>
                    <ul id="audio-list">
                        {audioFiles.map((file) => (
                            <li key={file.name} onClick={() => playAudio(file.url)}>
                                {file.name}
                            </li>
                        ))}
                    </ul>
                    <audio id="audio-player" controls style={{ marginTop: '16px', width: '100%' }} />
                </Container>
            </main>
        </div>
    );
}

function playAudio(url) {
    const audioPlayer = document.getElementById('audio-player') as HTMLAudioElement;
    audioPlayer.src = url;
    audioPlayer.play();
}

ReactDOM.render(<App />, document.getElementById('app'));