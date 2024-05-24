document.getElementById("spreadLine").addEventListener("input", function (e) {
    if (e.target.value === "") {
        e.target.value = "0.0";
    }
});

document.getElementById("spreadLineDecrement").addEventListener("click", function () {
    const input = document.getElementById("spreadLine");
    let value = parseFloat(input.value);
    if (value != Math.floor(value * 2) / 2) {
        input.value = (Math.floor(value * 2) / 2).toFixed(1);
    } else {
        input.value = (value - 0.5).toFixed(1);
    }
});

document.getElementById("spreadLineIncrement").addEventListener("click", function () {
    const input = document.getElementById("spreadLine");
    let value = parseFloat(input.value);
    if (value != Math.ceil(value * 2) / 2) {
        input.value = (Math.ceil(value * 2) / 2).toFixed(1); // Round up
    } else {
        input.value = (value + 0.5).toFixed(1);
    }
});
