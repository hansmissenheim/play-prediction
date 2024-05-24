document.getElementById("scoreDifferential").addEventListener("input", function (e) {
    if (e.target.value === "") {
        e.target.value = "0";
    }
});

document.getElementById("scoreDifferentialDecrement").addEventListener("click", function () {
    const input = document.getElementById("scoreDifferential");
    if (parseInt(input.value) > 0) {
        input.value = parseInt(input.value) - 1;
    }
});

document.getElementById("scoreDifferentialIncrement").addEventListener("click", function () {
    const input = document.getElementById("scoreDifferential");
    input.value = parseInt(input.value) + 1;
});
