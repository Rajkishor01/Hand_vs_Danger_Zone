import cv2
import numpy as np
import random
import math

cap = cv2.VideoCapture(0)

# STEP 1: CREATEING RANDOM DANGER ZONE (SAME AS BEFORE)
#-------------------------------------------------------
ret, frame = cap.read()
h, w, _ = frame.shape

box_w = random.randint(int(w * 0.15), int(w * 0.30))
box_h = random.randint(int(h * 0.15), int(h * 0.30))

x1 = random.randint(0, w - box_w)
y1 = random.randint(0, h - box_h)
x2 = x1 + box_w
y2 = y1 + box_h

box_cx = (x1 + x2) // 2
box_cy = (y1 + y2) // 2

# Motion detector state
prev_gray = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display = frame.copy()

    
    # STEP 2: PREPROCESS (GRAY, HSV, MOTION)
    #-------------------------------------------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    #Initialization of previous frame for motion detection 
    if prev_gray is None:
        prev_gray = blur
        continue

    #MOTION MASK (WHERE THINGS ARE MOVING) 
    diff = cv2.absdiff(prev_gray, blur)
    _, motion = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
    motion = cv2.medianBlur(motion, 7)
    motion = cv2.morphologyEx(motion, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    #SKIN COLOR MASK (YCrCb) 
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    cr = ycrcb[:,:,1]
    cb = ycrcb[:,:,2]

    lower = np.array([0, 133, 77])
    upper = np.array([255, 173, 127])

    skin_mask = cv2.inRange(ycrcb, lower, upper)

    # Small blur to smooth the mask
    skin_mask = cv2.GaussianBlur(skin_mask, (7, 7), 0)

    # HAND CANDIDATE MASK = MOTION AND SKIN 
    hand_mask = cv2.bitwise_and(motion, skin_mask)

    # hand mask cleaning: remove noise and fill small gaps
    hand_mask = cv2.morphologyEx(hand_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    hand_mask = cv2.morphologyEx(hand_mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    prev_gray = blur

    # STEP 3: GETTING HAND CONTOUR (FILTER BY AREA & SHAPE)
    #-------------------------------------------------------
    contours, _ = cv2.findContours(hand_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    state = "SAFE"
    state_color = (0, 255, 0)
    closest_point = None
    closest_dist = float("inf")

    hand_contour = None

    if contours:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 1000 or area > 15000:
                continue

            x, y, cw, ch = cv2.boundingRect(cnt)
            aspect_ratio = cw / float(ch + 1e-6)    # avoiding division by zero

            # Simple hand shape filter: not the extremely long part 
            if 0.3 < aspect_ratio < 3.0:
                # Keeping the largest plausible "hand-like" contour
                if area > (cv2.contourArea(hand_contour) if hand_contour is not None else 0):
                    hand_contour = cnt

    # STEP 4: CONVEX HULL + CLOSEST POINT TO DANGER BOX
    #-------------------------------------------------------
    if hand_contour is not None:
        cv2.drawContours(display, [hand_contour], -1, (255, 0, 0), 2)
        hull = cv2.convexHull(hand_contour)

        for pt in hull:
            px, py = pt[0]

            # Drawing hull points
            cv2.circle(display, (px, py), 4, (0, 255, 255), -1)

            # Distance from this point to danger-box boundary
            dx = max(x1 - px, 0, px - x2)
            dy = max(y1 - py, 0, py - y2)
            dist = math.sqrt(dx * dx + dy * dy)

            if dist < closest_dist:
                closest_dist = dist
                closest_point = (px, py)

    # STEP 5: SAFE / WARNING /DANGER LOGIC 
    #-------------------------------------------------------
    danger_threshold = 10   # touching/very close to box
    warning_threshold = 60  # approaching

    if closest_point is not None:
        if closest_dist <= danger_threshold:
            state = "DANGER DANGER"
            state_color = (0, 0, 255)
        elif closest_dist <= warning_threshold:
            state = "WARNING"
            state_color = (0, 255, 255)

        else:
            state = "SAFE"
            state_color = (0, 255, 0)

        # Marking the closest hand boundary point
        cv2.circle(display, closest_point, 10, state_color, -1)

    # STEP 6: DRAW DANGER BOX + SHOW STATE
    # -------------------------------------------------------
    cv2.rectangle(display, (x1, y1), (x2, y2), state_color, 3)

    cv2.putText(
        display,
        f"STATE: {state}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        state_color,
        2
    )


    cv2.imshow("Danger Detection", display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
