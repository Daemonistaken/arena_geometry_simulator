<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Obround + Dome Editor</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.2.4/fabric.min.js"></script>
  <style>
    body { display: flex; font-family: sans-serif; }
    #controls { width: 250px; padding: 10px; background: #f4f4f4; }
    #canvas-container { flex: 1; }
    label { display: block; margin-top: 10px; }
  </style>
</head>
<body>
  <div id="controls">
    <h3>Controls</h3>
    <label>Obround Width <input type="number" id="obroundWidth" value="6" step="0.1"></label>
    <label>Obround Height <input type="number" id="obroundHeight" value="7" step="0.1"></label>
    <label>Dome Radius <input type="number" id="domeRadius" value="2.6" step="0.1"></label>
    <button id="update">Update Shapes</button>
  </div>
  <div id="canvas-container">
    <canvas id="c" width="1000" height="800" style="border:1px solid #ccc"></canvas>
  </div>

<script>
  const canvas = new fabric.Canvas('c');

  // Function to draw obround (racetrack shape)
  function makeObround(w, h) {
    let r = w/2;
    let straight = h - 2*r;
    let pathData = [
      `M ${-w/2},${-straight/2}`, 
      `a ${r},${r} 0 0 1 ${w},0`, 
      `v ${straight}`, 
      `a ${r},${r} 0 0 1 -${w},0`, 
      `z`
    ].join(" ");
    return new fabric.Path(pathData, {
      left: 500, top: 400, stroke: "red", fill: "transparent", strokeWidth: 2, originX:"center", originY:"center"
    });
  }

  // Dome (circle)
  function makeDome(r) {
    return new fabric.Circle({
      radius: r, stroke: "yellow", fill: "transparent", strokeWidth: 2,
      left: 500, top: 400, originX: "center", originY: "center"
    });
  }

  // Initialize shapes
  let obround = makeObround(6*50, 7*50); // scaled (1m=50px)
  let dome = makeDome(2.6*50);
  canvas.add(obround, dome);

  // Update button
  document.getElementById('update').onclick = () => {
    let w = parseFloat(document.getElementById('obroundWidth').value)*50;
    let h = parseFloat(document.getElementById('obroundHeight').value)*50;
    let r = parseFloat(document.getElementById('domeRadius').value)*50;

    canvas.remove(obround, dome);
    obround = makeObround(w,h);
    dome = makeDome(r);
    canvas.add(obround, dome);
  };

  // Enable dragging + rotating
  canvas.on('object:modified', (e) => {
    let obj = e.target;
    console.log("Moved/rotated:", obj);
  });
</script>
</body>
</html>
