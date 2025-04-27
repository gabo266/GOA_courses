let count = 0;

function update() {
    if (document.getElementById("plus").checked) count++;
    if (document.getElementById("minus").checked) count--;
    document.getElementById("count").textContent = count;
}