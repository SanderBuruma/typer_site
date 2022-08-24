let typeHereInput = document.getElementById("type-here")

typeHereInput.addEventListener("keyup", handleKeyUpDown);
typeHereInput.addEventListener("keydown", handleKeyUpDown);

function handleKeyUpDown(event) {
    console.log(typeHereInput.value)
}
