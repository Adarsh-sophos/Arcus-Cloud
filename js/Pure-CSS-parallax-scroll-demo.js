var debugInput = document.querySelector("input");
function updateDebugState() {
document.body.classList.toggle('debug-on', debugInput.checked);
}
debugInput.addEventListener("click", updateDebugState);
updateDebugState();