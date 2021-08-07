var container = document.getElementById("container");
var width = container.clientWidth;
var height = container.clientHeight;
var aspect = width / height;
var renderer = new THREE.WebGLRenderer();
renderer.setSize(width, height);
container.appendChild(renderer.domElement);

var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera(50, aspect, 0.1, 1000);
camera.position.z = 500

system = new THREE.Group();   system

scene.add(
  new THREE.AmbientLight(0x444444, 0.2)
);

var light = new THREE.DirectionalLight(0xf8f8f8, 2.5);
light.position.set(1500, 1500, 1500);
scene.add(light);

var material = new THREE.MeshLambertMaterial({
  color: 0x666666
});

var planet = new THREE.Mesh(
  new THREE.IcosahedronGeometry(90, 3),
  material
);

for (var i = 0; i < planet.geometry.vertices.length; i++)
  planet.geometry.vertices[i].multiplyScalar(
    Math.random() * 0.05 + 0.95
  );

planet.geometry.computeFlatVertexNormals();
system.add(planet);



var asteroid0 = new THREE.Group();

for (var p = 0; p < Math.PI * 5; p = p + Math.random() * 0.1) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

  rand1 = Math.random() * 40 - 20;
 rand2 = Math.random() * 40 - 20; rand3 = Math.random() * 12 - 6;asteroid.position.set(200 * Math.sin(p) + rand1 , rand3 , 200 * Math.cos(p) + rand2  );

  asteroid.geometry.computeFlatVertexNormals();
  asteroid0.add(asteroid);
}

system.add(asteroid0);



var asteroid1 = new THREE.Group();

for (var p = 0; p < Math.PI * 5; p = p + Math.random() * 0.1) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

  rand1 = Math.random() * 40 - 20;
 rand2 = Math.random() * 40 - 20; rand3 = Math.random() * 10 - 5;asteroid.position.set(230 * Math.sin(p) + rand1 , rand3 , 230 * Math.cos(p) + rand2  );

  asteroid.geometry.computeFlatVertexNormals();
  asteroid1.add(asteroid);
}

system.add(asteroid1);



var asteroid2 = new THREE.Group();

for (var p = 0; p < Math.PI * 5; p = p + Math.random() * 0.1) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

  rand1 = Math.random() * 40 - 20;
 rand2 = Math.random() * 40 - 20; rand3 = Math.random() * 20 - 10;asteroid.position.set(260 * Math.sin(p) + rand1, rand3 , 260 * Math.cos(p) + rand2  );

  asteroid.geometry.computeFlatVertexNormals();
  asteroid2.add(asteroid);
}

system.add(asteroid2);



var asteroid3 = new THREE.Group();

for (var p = 0; p < Math.PI * 5; p = p + Math.random() * 0.1) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

  rand1 = Math.random() * 40 - 20;
 rand2 = Math.random() * 40 - 20; rand3 = Math.random() * 10 - 5;asteroid.position.set(290 * Math.sin(p) + rand1 , rand3 , 290 * Math.cos(p) + rand2  );

  asteroid.geometry.computeFlatVertexNormals();
  asteroid3.add(asteroid);
}

system.add(asteroid3);



var asteroid4 = new THREE.Group();

for (var p = 0; p < Math.PI * 5; p = p + Math.random() * 0.1) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

  rand1 = Math.random() * 40 - 20;
 rand2 = Math.random() * 40 - 20; rand3 = Math.random() * 20 - 10;asteroid.position.set(310 * Math.sin(p) + rand1, rand3 , 310 * Math.cos(p) + rand2  );

  asteroid.geometry.computeFlatVertexNormals();
  asteroid4.add(asteroid);
}

system.add(asteroid4);



/* var asteroidx = new THREE.Group();

for (var p = 0; p < Math.PI * 1; p = p + Math.random() * 0.15) 

for (var q = - Math.PI; q < Math.PI * 1; q = q + Math.random() * 0.15) {
  var asteroid = new THREE.Mesh(
    new THREE.IcosahedronGeometry(4, 0),
    material
  );

  var size = Math.random() * 0.3 + 0.1;
  for (var i = 0; i < asteroid.geometry.vertices.length; i++)
    asteroid.geometry.vertices[i].multiplyScalar(
      Math.random() * 0.2 + size
    );

 asteroid.position.set(120 * Math.sin(p) * Math.cos(q), 120 * Math.cos(p) * Math.cos(q), 120 *  Math.sin(q));

  asteroid.geometry.computeFlatVertexNormals();
  asteroidx.add(asteroid);
}

system.add(asteroidx);

 */

system.rotation.x = 0.15;
system.rotation.y = -0.5;
system.rotation.z = -0.3;

scene.add(system);

for (i = 0; i < 100; i++) {
  particles = new THREE.Points(
    new THREE.Geometry(),
    new THREE.PointsMaterial({
      size: Math.random() * 5
    })
  );
  for (j = 0; j < 20; j++) {
    var vertex = new THREE.Vector3();
    vertex.x = Math.random() * width * 1.1 - width * 1.1 / 2;
    vertex.y = Math.random() * height * 1.1 - height * 1.1 / 2;
    vertex.z = -300;
    particles.geometry.vertices.push(vertex);
    particles.material.color.setScalar(Math.random() * 0.4 + 0.2);
  }
  scene.add(particles);
}

function render() {
  requestAnimationFrame(render);

  planet.rotation.y += 0.003;
  planet.rotation.z -= 0.0015;

  

asteroid0.rotation.y += 0.005;
asteroid1.rotation.y += 0.004;
asteroid2.rotation.y += 0.003;
asteroid3.rotation.y += 0.002;
asteroid4.rotation.y += 0.001;

renderer.render(scene, camera);
}

render();