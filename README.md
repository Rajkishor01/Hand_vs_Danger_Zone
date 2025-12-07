# Hand_vs_Danger_Zone

A real-time system that tracks the user’s hand and evaluates its distance to a virtual danger box.


## System Pipeline (Unicode Diagram)

┌─────────┐      ┌────────────┐      ┌────────────────────────────┐
│  Frame  │ ───▶ │ Gray/Blur  │ ───▶ │ Motion Mask + Skin Mask    │
└─────────┘      └────────────┘      └────────────────────────────┘
                                         │
                                         │
                                         ▼
                               ┌───────────────────┐
                               │    Hand Mask      │
                               └───────────────────┘
                                         │
                                         ▼
                               ┌───────────────────┐
                               │ Contour Filtering │
                               └───────────────────┘
                                         │
                                         ▼
                         ┌──────────────────────────────────────┐
                         │   Convex Hull (Hand Boundary)        │
                         └──────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │  Closest Hand-Point to Danger Box            │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                      ┌────────────────────────────────────────┐
                      │        SAFE / WARNING / DANGER         │
                      └────────────────────────────────────────┘


## Threshold Logic
DANGER   : distance ≤ 10  
WARNING  : 10 < distance ≤ 60  
SAFE     : distance > 60
