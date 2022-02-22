var canvas = document.getElementById("renderCanvas");

var engine = null;
        var scene = null;
        var sceneToRender = null;
        var createDefaultEngine = function() { return new BABYLON.Engine(canvas, true, { preserveDrawingBuffer: true, stencil: true }); };

var createScene = function () {
    var scene = new BABYLON.Scene(engine);
    var camera = new BABYLON.ArcRotateCamera("Camera", 0, 0, 10, new BABYLON.Vector3(0, 0, 0), scene);
    camera.setPosition(new BABYLON.Vector3(20, 200, 400));
    camera.attachControl(canvas, true);
    scene.clearColor = new BABYLON.Color3(0, 0, 0);

    camera.upperBetaLimit = (Math.PI / 2) * 0.99;

    // Light
    var light = new BABYLON.PointLight("omni", new BABYLON.Vector3(50, 200, 0), scene);
    var light2 = new BABYLON.HemisphericLight("HemiLight", new BABYLON.Vector3(0, 1, 0), scene);

    //Materials
    var groundMaterial = new BABYLON.StandardMaterial("ground", scene);
    groundMaterial.diffuseTexture = new BABYLON.Texture("https://cdn.vox-cdn.com/thumbor/C4zAScX0-oQm7W9ou4r3wl3u_s8=/0x0:3992x2992/2120x1413/filters:focal(1677x1177:2315x1815):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/66567299/GettyImages_875403094.0.jpg", scene);
    groundMaterial.specularColor = BABYLON.Color3.Black();
    groundMaterial.wireframe = false;

    var redMat = new BABYLON.StandardMaterial("ground", scene);
    redMat.diffuseColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    redMat.specularColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    redMat.emissiveColor = BABYLON.Color3.Red();

    var greenMat = new BABYLON.StandardMaterial("ground", scene);
    greenMat.diffuseColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    greenMat.specularColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    greenMat.emissiveColor = BABYLON.Color3.Green();

    var blueMat = new BABYLON.StandardMaterial("ground", scene);
    blueMat.diffuseColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    blueMat.specularColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    blueMat.emissiveColor = BABYLON.Color3.Blue();

    var purpleMat = new BABYLON.StandardMaterial("ground", scene);
    purpleMat.diffuseColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    purpleMat.specularColor = new BABYLON.Color3(0.4, 0.4, 0.4);
    purpleMat.emissiveColor = BABYLON.Color3.Purple();

    /*************************************Meshes****************************************/
    // Ground
    var ground = BABYLON.MeshBuilder.CreateGround("ground", {width:412, height:341}, scene, false);
    ground.material = groundMaterial;
    ground.receiveShadows = true;

    // Meshes
    var redSphere = BABYLON.MeshBuilder.CreateSphere("red", {diameter:20}, scene);
    redSphere.material = redMat;
    redSphere.position.y = 10;
    redSphere.position.x -= 100;

    var greenBox = BABYLON.MeshBuilder.CreateBox("green", {size:20}, scene);
    greenBox.material = greenMat;
    greenBox.position.z -= 100;
    greenBox.position.y = 10;

    var blueBox = BABYLON.MeshBuilder.CreateBox("blue", {size:20}, scene);
    blueBox.material = blueMat;
    blueBox.position.x += 0;
    blueBox.position.y = 10;

    var gizmo5 = new BABYLON.ScaleGizmo(utilLayer);
    gizmo5.attachedMesh = greenBox;
    gizmo5.updateGizmoRotationToMatchAttachedMesh = true;
    gizmo5.updateGizmoPositionToMatchAttachedMesh = true;

    var gizmo3 = new BABYLON.RotationGizmo(utilLayer);
    gizmo3.attachedMesh = blueBox;
    gizmo3.updateGizmoRotationToMatchAttachedMesh = false;
    gizmo3.updateGizmoPositionToMatchAttachedMesh = true;

    var gizmo2 = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"))
    gizmo2.ignoreChildren = true;

    BABYLON.SceneLoader.ImportMesh('',"https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/CesiumMilkTruck/glTF/CesiumMilkTruck.gltf", "", scene, function (container) {
        var gltfMesh = container[0]
        gltfMesh.scaling = new BABYLON.Vector3(3, 3, 3);
        var bb = BABYLON.BoundingBoxGizmo.MakeNotPickableAndWrapInBoundingBox(gltfMesh)

        gizmo2.attachedMesh = bb;
        gizmo2.updateScale = false;
        gizmo2.fixedDragMeshBoundsSize = true;
        bb.position.x += 150;
        bb.position.y = 4;
        var multiPointerScaleBehavior2 = new BABYLON.MultiPointerScaleBehavior()
        bb.addBehavior(multiPointerScaleBehavior2)
        gizmo2.fixedDragMeshScreenSize = true;
        gizmo2.updateGizmoPositionToMatchAttachedMesh = true;

        var manager = new BABYLON.GUI.GUI3DManager(scene);

        var button = new BABYLON.GUI.HolographicButton("down");
        manager.addControl(button);
        button.linkToTransformNode(bb);
        button.position.z = -0.5;
        button.color = "red";
        button.text = "on/off";
        button.scaling = new BABYLON.Vector3(0.3, 0.3, 0.3);

        button.onPointerClickObservable.add(()=>{
        if(gizmo2.attachedMesh){
            gizmo2.attachedMesh = null;
            bb.removeBehavior(multiPointerScaleBehavior2)
        }else{
            gizmo2.attachedMesh = bb;
            bb.addBehavior(multiPointerScaleBehavior2)
        }
    })


    });

    // Dragging events
    gizmo2.onScaleBoxDragObservable.add(()=>{
        console.log("scaleDrag")
    });
     gizmo2.onScaleBoxDragEndObservable.add(()=>{
        console.log("scaleEnd")
    });
    gizmo2.onRotationSphereDragObservable.add(()=>{
        console.log("rotDrag")
    });
     gizmo2.onRotationSphereDragEndObservable.add(()=>{
        console.log("rotEnd")
    });

    var gizmo99 = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"))
    gizmo99.ignoreChildren = true;

    BABYLON.SceneLoader.ImportMesh('',"https://raw.githubusercontent.com/s-ai-kia/gltf_test/main/bicycle/scene.gltf", "", scene, function (container) {
        var gltfMesh99 = container[0]
        gltfMesh99.scaling = new BABYLON.Vector3(0.05, 0.05, 0.05);
        var bb99 = BABYLON.BoundingBoxGizmo.MakeNotPickableAndWrapInBoundingBox(gltfMesh99)

        gizmo99.attachedMesh = bb99;
        gizmo99.updateScale = false;
        gizmo99.fixedDragMeshBoundsSize = true;
        bb99.position.x += 150;
        bb99.position.y = 3;
        bb99.position.z -= 45;
        var multiPointerScaleBehavior99 = new BABYLON.MultiPointerScaleBehavior()
        bb99.addBehavior(multiPointerScaleBehavior99)
        gizmo99.fixedDragMeshScreenSize = true;
        gizmo99.updateGizmoPositionToMatchAttachedMesh = true;
    });


    var gizmo7 = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"))
    gizmo7.ignoreChildren = true;

    BABYLON.SceneLoader.ImportMesh('',"https://raw.githubusercontent.com/s-ai-kia/gltf_test/main/tree_for_games/scene.gltf", "", scene, function (container) {
        var gltfMesh2 = container[0]
        gltfMesh2.scaling = new BABYLON.Vector3(0.02, 0.02, 0.02);
        var bb2 = BABYLON.BoundingBoxGizmo.MakeNotPickableAndWrapInBoundingBox(gltfMesh2)

        gizmo7.attachedMesh = bb2;
        gizmo7.updateScale = false;
        var multiPointerScaleBehavior3 = new BABYLON.MultiPointerScaleBehavior()
        bb2.addBehavior(multiPointerScaleBehavior3)
        gizmo7.fixedDragMeshScreenSize = true;
        gizmo7.updateGizmoPositionToMatchAttachedMesh = true;
        bb2.position.x += 120;
        bb2.position.y = 20;
        bb2.position.z += 55;
        
    });

    var gizmo9 = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"))
    gizmo9.ignoreChildren = true;

    BABYLON.SceneLoader.ImportMesh('',"https://raw.githubusercontent.com/s-ai-kia/gltf_test/main/tesla_cybertruck/scene.gltf", "", scene, function (container) {
        var gltfMesh4 = container[0]
        gltfMesh4.scaling = new BABYLON.Vector3(0.03, 0.03, 0.03);
        var bb4 = BABYLON.BoundingBoxGizmo.MakeNotPickableAndWrapInBoundingBox(gltfMesh4)

        gizmo9.attachedMesh = bb4;
        gizmo9.updateScale = false;
        var multiPointerScaleBehavior4 = new BABYLON.MultiPointerScaleBehavior()
        bb4.addBehavior(multiPointerScaleBehavior4)
        gizmo9.fixedDragMeshScreenSize = true;
        gizmo9.updateGizmoPositionToMatchAttachedMesh = true;
        bb4.position.y = 2.5;
        bb4.position.z += 95;
        bb4.position.x -= 40;
        
    });

    var gizmo21 = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"))
    gizmo21.ignoreChildren = true;

    BABYLON.SceneLoader.ImportMesh('',"https://raw.githubusercontent.com/s-ai-kia/gltf_test/main/parking_sign/scene.gltf", "", scene, function (container) {
        var gltfMesh21 = container[0]
        gltfMesh21.scaling = new BABYLON.Vector3(0.03, 0.03, 0.03);
        var bb21 = BABYLON.BoundingBoxGizmo.MakeNotPickableAndWrapInBoundingBox(gltfMesh21)

        gizmo21.attachedMesh = bb21;
        gizmo21.updateScale = false;
        var multiPointerScaleBehavior21 = new BABYLON.MultiPointerScaleBehavior()
        bb21.addBehavior(multiPointerScaleBehavior21)
        gizmo21.fixedDragMeshScreenSize = true;
        gizmo21.updateGizmoPositionToMatchAttachedMesh = true;
        bb21.position.x += 170;
        bb21.position.y = 3;
        bb21.position.z -= 35;
        
    });

    
    var purpleDonut = BABYLON.MeshBuilder.CreateTorus("red", {diameter:10, thickness:3}, scene);
    purpleDonut.material = purpleMat;
    purpleDonut.position.y = 10;
    purpleDonut.position.z += 100;
    purpleDonut.position.x -= 60;

    var utilLayer = new BABYLON.UtilityLayerRenderer(scene)
    utilLayer.utilityLayerScene.autoClearDepthAndStencil = false;
    var gizmo = new BABYLON.BoundingBoxGizmo(BABYLON.Color3.FromHexString("#0984e3"), utilLayer)

    // Create behaviors to drag and scale with pointers in VR
    var sixDofDragBehavior = new BABYLON.SixDofDragBehavior()
    purpleDonut.addBehavior(sixDofDragBehavior)
    gizmo.attachedMesh = purpleDonut;
    var multiPointerScaleBehavior = new BABYLON.MultiPointerScaleBehavior()
    purpleDonut.addBehavior(multiPointerScaleBehavior)


    // Toggle gizmo on keypress
    document.onkeydown = ()=>{
        gizmo.attachedMesh = !gizmo.attachedMesh ? purpleDonut : null
        gizmo3.attachedMesh = !gizmo3.attachedMesh ? blueBox : null
        gizmo5.attachedMesh = !gizmo5.attachedMesh ? greenBox : null
    }

    

    var startingPoint;
    var currentMesh;

    var getGroundPosition = function () {
        var pickinfo = scene.pick(scene.pointerX, scene.pointerY, function (mesh) { return mesh == ground; });
        if (pickinfo.hit) {
            return pickinfo.pickedPoint;
        }

        return null;
    }

    var pointerDown = function (mesh) {
            currentMesh = mesh;
            startingPoint = getGroundPosition();
            if (startingPoint) { // we need to disconnect camera from canvas
                setTimeout(function () {
                    camera.detachControl(canvas);
                }, 0);
            }
    }

    var pointerUp = function () {
        if (startingPoint) {
            camera.attachControl(canvas, true);
            startingPoint = null;
            return;
        }
    }

    var pointerMove = function () {
        if (!startingPoint) {
            return;
        }
        var current = getGroundPosition();
        if (!current) {
            return;
        }

        var diff = current.subtract(startingPoint);
        currentMesh.position.addInPlace(diff);

        startingPoint = current;

    }

    scene.onPointerObservable.add((pointerInfo) => {      		
        switch (pointerInfo.type) {
			case BABYLON.PointerEventTypes.POINTERDOWN:
				if(pointerInfo.pickInfo.hit && pointerInfo.pickInfo.pickedMesh != ground) {
                    pointerDown(pointerInfo.pickInfo.pickedMesh)
                }
				break;
			case BABYLON.PointerEventTypes.POINTERUP:
                    pointerUp();
				break;
			case BABYLON.PointerEventTypes.POINTERMOVE:          
                    pointerMove();
				break;
        }
    });
    
    scene.createDefaultVRExperience({createDeviceOrientationCamera: false})


    return scene;
};

var engine;
try {
engine = createDefaultEngine();
} catch(e) {
console.log("the available createEngine function failed. Creating the default engine instead");
engine = createDefaultEngine();
}
if (!engine) throw 'engine should not be null.';
scene = createScene();;
sceneToRender = scene

engine.runRenderLoop(function () {
    if (sceneToRender && sceneToRender.activeCamera) {
        sceneToRender.render();
    }
});

// Resize
window.addEventListener("resize", function () {
    engine.resize();
});