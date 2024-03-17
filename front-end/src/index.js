import * as ARCH from '@inst-aaa/archiweb-core'
import * as THREE from 'three';
let viewport;

function initGUI(){
  component.GUICard.show = true;
  component.GUICard.options = {
    type: 'option', label: 'Options', items: [
      {
        type: 'color', label: 'color', value: '0xffffff', onChange: () => {

        }
      }
    ]
  }
}



function getGraph(vertices){
  console.log(vertices.coordinates.length)
  let points = ARCH.coordinatesToPoints(vertices.coordinates, vertices.size)
  // console.log(points.length)
  let ptset = []
  for(let i = 0; i < points.length; ++ i) {
    let flag = true;
    for (let pt of ptset) {
      if(points[i].distanceTo(pt) < 0.001) flag = false;
    }
    if(flag) {
      ptset.push(points[i]);
    }
  }

  for(let i = 0; i < 20; ++ i) {
    for(let j = 0; j < i; ++ j) {
      if (ptset[i].distanceTo(ptset[j]) < 150) {
        console.log(i, j)
      }
    }
  }
  // for(let i = 0; i < points.length/2; ++ i) {
  //   for (let j = 0; j < i; ++j) {
  //     console.log(points[i].distanceTo(points[j]))
  //     // if(points[i].distanceTo(points[j]))
  //   }
  // }

  viewport.addObject(vertices)

}

function main() {

  viewport = new ARCH.Viewport('container', true, {dimension: '3d'})
  let mesh = new ARCH.Mesh(viewport, {geometry: new THREE.DodecahedronGeometry(200)})
  initGUI();
  console.log(mesh.children[1].geometry)
  getGraph(mesh.vertices)
}

export default {main}
