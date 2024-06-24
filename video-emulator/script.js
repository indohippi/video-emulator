const categories = [
    'classes',
    'techniques',
    'concepts',
    'people'
];

async function fileExists(url) {
    try {
        const response = await fetch(url, { method: 'HEAD' });
        return response.ok;
    } catch (error) {
        return false;
    }
}

async function loadThumbnails() {
    const categoriesContainer = document.getElementById('categories');

    for (const category of categories) {
        const categoryDiv = document.createElement('div');
        categoryDiv.classList.add('category');
        
        const categoryTitle = document.createElement('h2');
        categoryTitle.textContent = capitalizeFirstLetter(category);
        categoryDiv.appendChild(categoryTitle);
        
        const thumbnailsDiv = document.createElement('div');
        thumbnailsDiv.classList.add('thumbnails');
        
        for (let i = 1; i <= 20; i++) {
            const thumbnailPath = `thumbnails/${category}/${category}_th${i.toString().padStart(2, '0')}.jpg`;
            const videoPath = `videos/${category}/${category}${i.toString().padStart(2, '0')}.mp4`;

            const thumbnailExists = await fileExists(thumbnailPath);
            const videoExists = await fileExists(videoPath);

            if (thumbnailExists && videoExists) {
                const thumbnail = document.createElement('img');
                thumbnail.src = thumbnailPath;
                thumbnail.alt = `${category} thumbnail ${i}`;
                thumbnail.addEventListener('click', () => {
                    loadVideo(category, i);
                });
                thumbnailsDiv.appendChild(thumbnail);
            }
        }
        
        if (thumbnailsDiv.childElementCount > 0) {
            categoryDiv.appendChild(thumbnailsDiv);
            categoriesContainer.appendChild(categoryDiv);
        }
    }
}

function loadVideo(category, index) {
    const videoPath = `videos/${category}/${category}${index.toString().padStart(2, '0')}.mp4`;
    const videoSource = document.getElementById('video-source');
    videoSource.src = videoPath;
    const videoPlayer = document.getElementById('main-video');
    videoPlayer.load();
    videoPlayer.play();
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

document.addEventListener('DOMContentLoaded', loadThumbnails);
