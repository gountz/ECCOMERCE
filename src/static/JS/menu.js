
const $menu = document.getElementById('menu-hamburger-js');
const $categorias = document.getElementById('menu-category-js');

function desplegarMenu(){
    $menu.classList.toggle('menu-activate-toggle');
    if($categorias.classList.contains('menu-category-toggle')){
        $categorias.classList.toggle('menu-category-toggle');
    }
}
function desplegarCategorias(){
    $categorias.classList.toggle('menu-category-toggle');
}
