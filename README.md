Project Description: Halal Video Recommendation System
Overview
In the digital age, content recommendation systems have become essential for enhancing user experience by providing personalized content suggestions. My project, the Halal Video Recommendation System, is designed to cater to a specific need within the vast landscape of online video content. It aims to recommend videos that are Halal, meaning permissible under Islamic law, to users seeking content that aligns with their ethical and religious beliefs. This system is particularly useful for platforms hosting a diverse range of videos, ensuring that users can easily find content that meets their Halal criteria.

Objective
The primary objective of this project is to develop a machine learning-based recommendation system that can accurately identify and suggest Halal videos to users. This involves classifying videos into Halal and non-Halal categories and then recommending Halal videos based on the user's viewing history and preferences.

Data Collection and Preprocessing
The foundation of my recommendation system is a robust dataset obtained from a variety of online video platforms. This dataset includes video IDs, titles, descriptions, tags, and a binary indicator denoting whether a video is Halal or not. To prepare this data for analysis, I performed several preprocessing steps:

Text Normalization: All textual data (titles, descriptions, tags) were converted to lowercase to maintain consistency.
Missing Value Handling: Missing titles were filled with a placeholder text "no title", and missing descriptions were handled similarly.
Text Vectorization: I used the TF-IDF (Term Frequency-Inverse Document Frequency) technique to convert text data into numerical vectors, facilitating machine learning model training.
Model Development
I experimented with two machine learning models: Logistic Regression and Random Forest Classifier. Logistic Regression was chosen for its effectiveness in binary classification tasks, making it suitable for distinguishing between Halal and non-Halal videos. The Random Forest Classifier was selected for its ability to handle the high dimensionality of text data and improve classification accuracy through ensemble learning.

Logistic Regression Model: Trained on the TF-IDF vectors of video titles, this model aimed to predict the Halal status of videos. It demonstrated a balanced performance in terms of accuracy, precision, recall, and F1 score.
Random Forest Classifier: This model was trained on a combination of video titles and descriptions to capture a broader context. It was further optimized through hyperparameter tuning using GridSearchCV, leading to improved classification accuracy.
Recommendation Logic
The recommendation engine utilizes cosine similarity to measure the similarity between the TF-IDF vectors of videos. For a given video, the system identifies other Halal videos with similar content (based on titles, descriptions, and tags) and recommends the top matches to the user. This approach ensures that the recommendations are not only Halal but also relevant to the user's interests.

Evaluation and Validation
The effectiveness of the recommendation system was evaluated using standard metrics such as accuracy, precision, recall, and F1 score. Additionally, I implemented a verification step to ensure that all recommended videos are indeed Halal, addressing any potential misclassifications by the models.

Implementation and Future Work
The final system was implemented in a Jupyter Notebook, with models trained and evaluated on a split dataset. The models and the TF-IDF vectorizer were saved using pickle for future use. Going forward, I plan to integrate this recommendation system into a web application, allowing users to receive personalized Halal video recommendations in real-time. Further improvements will focus on expanding the dataset, refining the models, and exploring advanced natural language processing techniques for better understanding video content.

Conclusion
The Halal Video Recommendation System represents a significant step towards creating a more inclusive and respectful online environment. By leveraging machine learning and natural language processing, I have developed a system that not only respects users' religious and ethical preferences but also enhances their content discovery experience.
