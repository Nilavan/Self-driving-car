from model import build_model, checkpoint_path
import cv2

model = build_model()
model.compile(optimizer='adam', loss="mse")

model.load_weights(filepath=checkpoint_path)

wheel = cv2.imread('steering_wheel_image.jpg')
