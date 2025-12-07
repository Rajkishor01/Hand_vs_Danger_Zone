<svg width="1200" height="650" xmlns="http://www.w3.org/2000/svg">
  <!-- Styles -->
  <style>
    .box { fill: #f5f5f5; stroke: #333; stroke-width: 2; }
    .arrow { stroke: #000; stroke-width: 2; marker-end: url(#arrowhead); }
    .text { font-family: monospace; font-size: 16px; }
  </style>

  <!-- Arrowhead Marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
  </defs>

  <!-- Boxes -->
  <rect x="50" y="50" width="250" height="60" class="box"/>
  <text x="75" y="90" class="text">Frame</text>

  <rect x="350" y="50" width="250" height="60" class="box"/>
  <text x="380" y="90" class="text">Gray / Blur</text>

  <rect x="650" y="50" width="350" height="60" class="box"/>
  <text x="670" y="90" class="text">Motion Mask + Skin Mask</text>

  <rect x="350" y="180" width="250" height="60" class="box"/>
  <text x="380" y="220" class="text">Hand Mask</text>

  <rect x="350" y="300" width="250" height="60" class="box"/>
  <text x="365" y="340" class="text">Contour Filtering</text>

  <rect x="350" y="420" width="350" height="60" class="box"/>
  <text x="370" y="460" class="text">Convex Hull (Hand Boundary)</text>

  <rect x="450" y="540" width="450" height="60" class="box"/>
  <text x="470" y="580" class="text">Closest Hand-Point to Danger Box</text>

  <rect x="450" y="640" width="350" height="60" class="box"/>
  <text x="470" y="680" class="text">SAFE / WARNING / DANGER</text>

  <!-- Main Arrows -->
  <line x1="300" y1="80" x2="350" y2="80" class="arrow"/>
  <line x1="600" y1="80" x2="650" y2="80" class="arrow"/>
  <line x1="825" y1="110" x2="475" y2="180" class="arrow"/>

  <line x1="475" y1="240" x2="475" y2="300" class="arrow"/>
  <line x1="475" y1="360" x2="475" y2="420" class="arrow"/>

  <line x1="525" y1="480" x2="525" y2="540" class="arrow"/>
  <line x1="675" y1="600" x2="675" y2="640" class="arrow"/>

  <!-- Side Join -->
  <line x1="825" y1="110" x2="825" y2="450" class="arrow"/>
  <line x1="825" y1="450" x2="700" y2="450" class="arrow"/>

</svg>
