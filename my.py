import streamlit as st
import av
import numpy as np
import streamlit_webrtc as webrtc


def app():
    # Define the callback function to process the video frames
    def handle_frame(frame):
        # Convert the video frame to a NumPy array
        img = frame.to_ndarray(format='bgr24')

        # Process the image here...

        # Display the processed image
        st.image(img, channels='BGR')

    # Create the WebRTC camera widget
    webrtc_ctx = webrtc.Streamer(
        key='camera',
        video_transformer_factory=lambda: webrtc.VideoTransformer(callback=handle_frame),
        constraints={'video': True, 'audio': False},
    )

    # Display the camera widget
    st.write('Camera')
    webrtc_ctx


if __name__ == '__main__':
    app()

