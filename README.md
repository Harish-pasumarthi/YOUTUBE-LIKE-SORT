## ![YouTube Logo](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)  YT LIKE-SORT 
 LIKE-SORT is a web-based application that allows users to search for YouTube videos on any topic and displays the top results sorted by the number of likes. This project utilizes the YouTube Data API to fetch video details and provides an easy-to-use interface for accessing the most liked videos.
## Demo

<a href="https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE">
    <img src="output/thumbnail.png" alt="YT LIKE-SORT Demo" width="200">
    <h4>CLICK ON 👆🏻 YOUTUBE LOGO TO 👀 WATCH DEMO 📽️</h4>
</a>

## Project Aim
The aim of YT LIKE-SORT is to provide a platform where users can easily find the most appreciated YouTube videos on a given topic. This ensures high-quality content discovery based on community feedback in the form of likes.

## Real World Scenario
- Users can search for popular tutorials or reviews on any topic.
- YT LIKE-SORT sorts videos based on the number of likes, showing the most liked first.
- It helps users quickly find high-quality, community-approved content.
- The sorting approach ensures valuable resources are easily discoverable.

![Placeholder for Video Info Display](output/1.png)

## Key Features
- **Search YouTube Videos:** Users can search for videos on any topic and receive a list of relevant results.
- **Like-based Sorting:** Results are sorted based on the number of likes, with the most liked videos appearing first.
- **Responsive Design:** The user interface is designed to work seamlessly across different devices.
- **Video Thumbnails and Titles:** Displays video thumbnails and titles, along with a link to watch the video on YouTube.

## Technologies Used

![Python Logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YouTube Logo](https://img.shields.io/badge/YouTube%20Data%20API-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![HTML/CSS/JavaScript Logo](https://img.shields.io/badge/HTML/CSS/JS-F7DF1E?style=for-the-badge&logo=html5&logoColor=white)
![Google API Logo](https://img.shields.io/badge/Google%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)

- **Python (Flask):** Backend server and API integration.
- **YouTube Data API:** Fetching video information and statistics.
- **HTML/CSS/JavaScript:** Frontend interface design.
- **Google API Client Library:** To connect with YouTube's API.

## Example Outputs

![Placeholder for Most Liked Videos List](output/2.png)
 -USER ENTERED 
 ```bash
    Apple 16 pro review
```
![Placeholder for Video Thumbnail Display](output/3.png)
-USER GET RESULTS
 ![Placeholder for Video Info Display](output/4.png)


## Setup Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install flask google-api-python-client
   ```
3. Replace `api_key` in `app.py` with your YouTube Data API key.
4. Run the Flask server:
   ```bash
   python app.py
   ```
   ![Placeholder for Play Button Overlay](output/5.png)
5. Open a web browser and navigate to `http://127.0.0.1:5000`.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

