var sliders = document.getElementsByClassName("slider");
var inputs = document.getElementsByClassName("input");

for (let i = 0; i < sliders.length; i++) {
    sliders[i].addEventListener("input", function () {
        inputs[i].value = sliders[i].value;
    });

    inputs[i].addEventListener("input", function () {
        sliders[i].value = inputs[i].value;
    });
}
