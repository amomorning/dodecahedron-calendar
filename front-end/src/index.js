import * as ARCH from '@inst-aaa/archiweb-core'


function main() {

  let viewport = new ARCH.Viewport('container', true, {'dimension': '3d'})

  new ARCH.Cuboid(viewport, [0, 0, 0], [100, 100, 100]);
  new ARCH.Sphere(viewport, [0, 100, 0], 10)
}

export default {main}
