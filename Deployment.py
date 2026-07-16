import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# ==========================
# Load Model
# ==========================

@st.cache_resource
def load_model():
    return YOLO("yolov8s.pt")   # ضع اسم الموديل عندك

model = load_model()

# ==========================
# Class Names
# ==========================

class_names = {
    0: "Longitudinal Crack",
    1: "Transverse Crack",
    2: "Alligator Crack",
    3: "other",
    4: "Pothole"
}

# ==========================
# UI
# ==========================

st.title("Road Damage Detection")
st.write("Upload a road image to detect road damages.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Detect Damages"):

        results = model.predict(
            source=np.array(image),
            conf=0.25,
            verbose=False
        )

        annotated_image = results[0].plot()

        st.image(
            annotated_image,
            caption="Detection Result",
            use_container_width=True
        )

        st.subheader("Detected Objects")

        boxes = results[0].boxes

        if len(boxes) == 0:
            st.warning("No road damage detected.")

        else:
            for box in boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0]) * 100

                st.write(
                    f"**{class_names[class_id]}** "
                    f"({confidence:.2f}%)"
                )