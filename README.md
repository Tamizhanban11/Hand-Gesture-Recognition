# Hand Gesture Recognition

## Overview
This project implements a Hand Gesture Recognition system that detects and classifies hand gestures using a webcam or an image input. The system can be integrated with a laptop to open applications based on specific gestures.

## Features
- Real-time gesture recognition using a webcam.
- Predefined gesture mapping to gesture actions 
- Model trained using  Mediapipe Library
- Integration with system commands to trigger actions.

## Technologies Used
- Python
- OpenCV
- Mediapipe
- NumPy
- PyAutoGUI (for automating application opening)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/hand-gesture-recognition.git
   cd hand-gesture-recognition
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- Launch the script, and it will open a webcam feed.
- Show predefined gestures (e.g., thumbs up, palm, fist).
- The system will detect the gesture and trigger the assigned action.
- Modify `gesture_mapping.py` to customize gestures and actions.

## Model Training (Optional)
If using a deep learning model:
1. Collect gesture images and label them.
2. Train the model using a CNN architecture.
3. Save the trained model and load it for real-time predictions.

## Customization
- Modify `config.py` to adjust parameters like detection confidence.
- Add new gestures by training a new dataset.

## Contribution
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes.
4. Push the branch and create a pull request.



## Future Enhancements
- Improve accuracy with better models.
- Support dynamic gestures.
- Integrate voice commands with gestures.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, reach out to:
- Email: your-email@example.com
- GitHub Issues

## Acknowledgments
- OpenCV for image processing.
- Mediapipe for hand tracking.
- TensorFlow/Keras for deep learning models.

