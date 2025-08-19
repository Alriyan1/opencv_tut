## OpenCV Tutorials (Python)

### Overview
This repository is a collection of small, focused OpenCV and Computer Vision demos in Python. It includes basic image/video I/O, filtering and morphology, perspective warping, image joining, color/shape detection, document scanning, real‑time hand tracking and interactive demos with MediaPipe, monocular depth estimation, and a full tennis analytics pipeline using YOLO and PyTorch.

All scripts are self‑contained and can be run directly. Image assets live in `Images/` and sample videos in `Videos/` unless otherwise noted.

### Requirements
- Python 3.9–3.12 (Windows tested)
- Recommended: a virtual environment (venv)

Core packages used across demos:
- `opencv-python`
- `numpy`

Additional packages used in specific folders:
- `mediapipe` (hand tracking and gesture demos)
- `ultralytics` (YOLO for object/ball/player detection)
- `torch`, `torchvision` (required by Ultralytics and keypoint model)
- `pandas` (tennis analytics stats aggregation)
- Optional for the depth notebook: `depth-pro`, `timm` (see the notebook for exact versions)

### Setup (Windows PowerShell)
```powershell
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate

# 2) Install core dependencies
pip install --upgrade pip
pip install opencv-python numpy

# 3) Install MediaPipe (for folders 08, 09, 10)
pip install mediapipe

# 4) Install Ultralytics + PyTorch (for folders 11, 12)
pip install ultralytics

# PyTorch CPU (fallback if needed):
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# PyTorch CUDA 12.1 (if you have a compatible NVIDIA GPU/driver):
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# 5) Tennis analytics extra
pip install pandas
```

Notes:
- Ultralytics will try to install a compatible Torch automatically, but explicitly installing Torch as above can resolve environment issues.
- If `cv2.imshow` opens but you see no window content, ensure you’re not running in a terminal without GUI support.

### Project structure
- `01Reading/`: Read images, videos, and webcam frames with OpenCV
- `02BasicFunctions/`: Grayscale, blur, edge detection, dilation, erosion, cropping, drawing figures/text
- `03WrapPerspective/`: Perspective transform (bird’s‑eye/warp)
- `04JoiningImages/`: Concatenate/combine images into grids
- `05ColorDetection/`: HSV thresholding and color masking demos
- `06ShapeDetection/`: Contour‑based shape detection
- `07DocumentScanner/`: Simple document scanner pipeline
- `08HandTracking/`: Real‑time hand landmark detection with MediaPipe
- `09MathGesture/`: Gesture‑based drawing/math canvas using MediaPipe
- `10SpinWheel/`: Interactive spin‑wheel controlled by hand landmarks
- `11DepthPro/`: Depth estimation and related experiments (includes a Colab‑style notebook)
- `12TennisAnalysis/`: End‑to‑end tennis analytics: player/ball detection and mini‑court visualization using YOLO and a keypoint model
- `Images/`: Sample images used by various scripts
- `Videos/`: Sample videos used by various scripts

### How to run
Run any script from the repository root. Use `python` on Windows (or `python3` on other OSes).

- 01 — Reading
```powershell
python 01Reading/read_image.py
python 01Reading/read_video.py
python 01Reading/read_webcam.py
```

- 02 — Basic Functions
```powershell
python 02BasicFunctions/image_grayscale.py
python 02BasicFunctions/image_blur.py
python 02BasicFunctions/edge_detector.py
python 02BasicFunctions/image_dialation.py
python 02BasicFunctions/image_erosion.py
python 02BasicFunctions/image_crop.py
python 02BasicFunctions/figure&textImage.py
```

- 03 — Wrap Perspective
```powershell
python 03WrapPerspective/wrap_perspective.py
```

- 04 — Joining Images
```powershell
python 04JoiningImages/join_images.py
```

- 05 — Color Detection
```powershell
python 05ColorDetection/colordetection.py
python 05ColorDetection/colordetection2.py
```

- 06 — Shape Detection
```powershell
python 06ShapeDetection/shape_detection.py
```

- 07 — Document Scanner
```powershell
python 07DocumentScanner/document_scanner.py
```

- 08 — Hand Tracking (webcam required; press 'q' to quit)
```powershell
python 08HandTracking/main.py
```

- 09 — Math Gesture (webcam)
```powershell
python 09MathGesture/math_gesture.py
```

- 10 — Spin Wheel (webcam)
```powershell
python 10SpinWheel/spin_wheel.py
```

- 11 — Depth Pro
```powershell
python 11DepthPro/depth_test.py
```
The notebook `11DepthPro/realTimeDistanceMeasure.ipynb` may require additional packages (`depth-pro`, `timm`) as prompted inside the notebook.

- 12 — Tennis Analysis
```powershell
# Uses models and stubs already placed under 12TennisAnalysis/models and 12TennisAnalysis/tracker_stubs
python 12TennisAnalysis/main.py
```
Outputs to `12TennisAnalysis/output_videos/output.avi`. If you want to run raw YOLO tracking on the sample input, there is also:
```powershell
python 12TennisAnalysis/yolo_inference.py
```

### Assets and models
- Images are in `Images/`. Update paths in scripts if you use your own images.
- Videos are in `Videos/`. Update paths to test with your own clips.
- Tennis models are in `12TennisAnalysis/models/`:
  - `yolo11m.pt` (players)
  - `tennis_ball_best.pt` (ball)
  - `keypoints_model_50.pth` (court keypoints)
- Precomputed detection stubs for faster runs are in `12TennisAnalysis/tracker_stubs/`.

### Troubleshooting
- Webcam not opening: try changing the device index in scripts (e.g., `cv2.VideoCapture(1)`), ensure no other app is using the camera, and grant camera permissions.
- `cv2.imshow` freezes: avoid running in environments without GUI. Press `q` in the display window to exit.
- Torch/Ultralytics install issues: install Torch explicitly (CPU or CUDA variant), then reinstall `ultralytics`.
- Video writing issues: OpenCV writes AVI by default; ensure you have the proper codecs. Try a different FourCC or path if needed.

### Acknowledgements
- OpenCV team and contributors
- Google MediaPipe
- Ultralytics YOLO
- PyTorch


