document.getElementById("drive").addEventListener("input", function (e) {
    if (e.target.value === "") {
        e.target.value = "1";
    }
});

document.getElementById("driveDecrement").addEventListener("click", function () {
    const input = document.getElementById("drive");
    if (parseInt(input.value) > 1) {
        input.value = parseInt(input.value) - 1;
    }
});

document.getElementById("driveIncrement").addEventListener("click", function () {
    const input = document.getElementById("drive");
    input.value = parseInt(input.value) + 1;
});
