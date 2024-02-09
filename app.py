import streamlit as st
import pandas as pd
import random
import joblib
import pickle

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)


# Load the model
model = joblib.load('finalized_model.pkl')

# Load the dataset
data = pd.read_csv('Data/cleaned_dataset.csv')

# Streamlit app
def main():
    st.title("Halal or Haram Video Prediction")

    # User input
    video_id = st.text_input("Enter Video ID:")

    if st.button("Predict"):
        prediction = predict_halal_haram(video_id)

        if prediction:
            st.write(f"The video with ID {video_id} is {prediction}")
            if prediction.lower() == 'halal':
                try:
                    recommended_videos = recommend_halal_videos()
                    st.write("Recommended Halal Videos:")
                    for vid in recommended_videos:
                        st.write(vid)
                except KeyError as e:
                    st.error(f"An error occurred: {e}. Please check the dataset columns.")
        else:
            st.write("Prediction not available. Please check the video ID.")

def predict_halal_haram(video_id):
    # Assuming 'data' is your DataFrame and 'model' is your trained logistic regression model
    # Also assuming 'tfidf_vectorizer' is the TF-IDF vectorizer used during model training

    # Find the video in the dataset
    video = data[data['ID'] == video_id]
    if video.empty:
        return "Video not found"

    # Get the title of the video
    title = video['Title'].iloc[0]

    # Preprocess the title, if necessary
    # title = preprocess_title(title) # Define this function based on your preprocessing logic

    # Vectorize the title
    title_vectorized = tfidf_vectorizer.transform([title])

    # Predict using the model
    prediction = model.predict(title_vectorized)

    # Map the prediction to 'Halal' or 'Haram'
    if prediction[0] == 1:
        return 'Halal'
    else:
        return 'Haram'

def recommend_halal_videos():
    # Implement logic to randomly select five Halal videos
    if 'Is Halal' in data.columns and 'ID' in data.columns:  # Updated to use 'ID'
        halal_videos = data[data['Is Halal'] == 1]
        return random.sample(list(halal_videos['ID']), min(len(halal_videos), 5))  # Updated to use 'ID'
    else:
        raise KeyError("One of the required columns ('Is Halal' or 'ID') is missing in the dataset.")

if __name__ == "__main__":
    main()
