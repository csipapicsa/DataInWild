import os
import pandas as pd
# https://github.com/serengil/deepface
from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image

# https://github.com/serengil/deepface

# Ping the downloader 
demography = DeepFace.analyze("datasets/demo.webp")

print(demography)


def analyze_faces_in_directory(directory, emotion_folder):
    # Create a DataFrame to store the analysis results
    results_df = pd.DataFrame(columns=["Image", "Age", "Gender", "Race", "Emotion"])
    results = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add more extensions if needed
            file_path = os.path.join(directory, filename)
            try:
                # Analyze the face in the image with enforce_detection=False
                print(f"Processing {filename}")
                analysis = DeepFace.analyze(img_path=file_path, actions=['age', 'gender', 'race', 'emotion'], enforce_detection=False)

                # DeepFace returns a list, so access the first dictionary in the list
                analysis = analysis[0]

                # Extract data from the analysis dictionary
                
                #age = analysis.get('age', 'N/A')  # Use .get() to handle missing keys
                #gender = analysis.get('dominant_gender', 'N/A')  # Correct key for gender
                #race = analysis.get('dominant_race', 'N/A')  # Correct key for race
                #emotion = analysis.get('dominant_emotion', 'N/A')  # Correct key for emotion
                #print(analysis)

                result_dict = {
                    "Image": f"{emotion_folder}_-_{filename}",
                    "Age": analysis.get('age', 'N/A'),
                    "Gender": analysis.get('dominant_gender', 'N/A'),
                    "Race": analysis.get('dominant_race', 'N/A'),
                    "Emotion": analysis.get('dominant_emotion', 'N/A')
                }
                
                # Append dictionary to results list
                results.append(result_dict)

                # Print the results for the current image
                # print(f"Processed {filename}: Age: {age}, Gender: {gender}, Race: {race}")

            except Exception as e:
                # Handle the error gracefully and continue processing
                print(f"Error processing {filename}: {e}")
                continue

    # Save results to CSV for further use
    # Convert results list to DataFrame only at the end
    if results:  # Check if we have any results
        results_df = pd.DataFrame(results)
        output_file = f'face_analysis_results_{emotion_folder}.csv'
        results_df.to_csv(output_file, index=False)
        print(f"Analysis completed! Results saved to {output_file}")
    else:
        print("No results to save!")


# Example usage
directory_path = 'datasets/AffectNet/Test'
emotion_folders = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise', 'contempt']
for e in emotion_folders:
    analyze_faces_in_directory(f"{directory_path}/{e}", e)  
