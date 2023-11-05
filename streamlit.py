import streamlit as st
import cv2
import numpy as np

st.title("Image Transformation App")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Transformation options
    transformation = st.selectbox(
        "Select a transformation",
        ["None", "Rotate", "Scale", "Translate", "Shear"]
    )

    if transformation == "Rotate":
        angle = st.slider("Select an angle for rotation", -180, 180, 0)
        dsize = (image.shape[1], image.shape[0])
        rotated_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1), dsize)
        st.image(rotated_image, caption="Rotated Image", use_column_width=True)

    if transformation == "Scale":
        scale_factor = st.number_input("Scale factor", min_value=0.1, value=1.0, step=0.1)
        dsize = (image.shape[1], image.shape[0])
        scaled_image = cv2.resize(image, dsize, fx=scale_factor, fy=scale_factor)
        st.image(scaled_image, caption="Scaled Image", use_column_width=True)

    if transformation == "Translate":
        dx = st.slider("Horizontal translation (pixels)", -image.shape[1], image.shape[1], 0)
        dy = st.slider("Vertical translation (pixels)", -image.shape[0], image.shape[0], 0)
        dsize = (image.shape[1], image.shape[0])
        translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
        translated_image = cv2.warpAffine(image, translation_matrix, dsize)
        st.image(translated_image, caption="Translated Image", use_column_width=True)

    if transformation == "Shear":
        shear_factor = st.slider("Shear factor", -1.0, 1.0, 0.0)
        dsize = (image.shape[1], image.shape[0])
        shear_matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
        sheared_image = cv2.warpAffine(image, shear_matrix, dsize)
        st.image(sheared_image, caption="Sheared Image", use_column_width=True)
