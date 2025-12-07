# Hand_vs_Danger_Zone

A real-time system that uses a camera feed to track the user's hand and detect when it approaches a virtual danger zone on the screen.

When the hand reaches this boundary, the system triggers an on-screen alert: **DANGER DANGER**.


## System Pipeline

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


## Threshold Logic

DANGER   : distance ≤ 10  
WARNING  : 10 < distance ≤ 60  
SAFE     : distance > 60
