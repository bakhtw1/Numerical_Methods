document.addEventListener("DOMContentLoaded", function(){
    
    var b = JXG.JSXGraph.initBoard('calculator', {boundingbox: [-4, 2, 7, -2], axis: true});
    b.create('functiongraph', [function(x){return Math.sin(x);},-Math.PI,2*Math.PI]);
    
});

