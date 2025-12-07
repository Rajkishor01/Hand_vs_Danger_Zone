# Hand_vs_Danger_Zone

A real-time system that tracks the user’s hand and evaluates its distance to a virtual danger box.

## Threshold Logic
DANGER   : distance ≤ 10  
WARNING  : 10 < distance ≤ 60  
SAFE     : distance > 60


## System Pipeline

```mermaid
graph TD
    A[Frame] --> B[Gray / Blur]
    B --> C[Motion Mask + Skin Mask]
    C --> D[Hand Mask]
    D --> E[Contour Filtering]
    E --> F[Convex Hull/Hand Boundary]
    F --> G[Closest Hand-Point to Danger Box]
    G --> H{SAFE / WARNING / DANGER}
