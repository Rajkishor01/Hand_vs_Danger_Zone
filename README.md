# Hand_vs_Danger_Zone

camera feed to track the position of the user’s hand in real time and detect when the hand approaches a virtual object on the screen.

When the hand reaches this boundary, the system should trigger a clear on-screen warning: DANGER DANGER

Frame ---> Gray/Blur ---> Motion Mask + Skin Mask ---> Hand Mask ---> Contour Filtering
                        |                                  |
                        |                                  v
                        |                        Convex Hull (Hand Boundary)
                        |                                  |
                        +----------------------------------+
                                                           |
                                                           v
                                        Closest Hand-Point to Danger Box
                                                           |
                                                           v
                                           SAFE / WARNING / DANGER

DANGER : distance ≤ 10
WARNING : 10 < distance ≤ 60
SAFE : distance > 60
