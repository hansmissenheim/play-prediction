const dropdown = document.getElementById("dropdown");
const dropdownMenu = document.getElementById("dropdownMenu");
const seasonButton = document.getElementById("seasonButton");
const seasonList = document.getElementById("seasonList");
const seasonInput = document.getElementById("seasonInput");
const selectedSeason = document.getElementById("selectedSeason");

for (let year = 2024; year >= 1999; year--) {
    const li = document.createElement("li");
    li.textContent = year;
    li.classList.add("px-4", "py-0.5", "cursor-pointer", "hover:underline", "underline-offset-2");
    li.onclick = function () {
        seasonInput.value = year;
        selectedSeason.textContent = year;
        dropdownMenu.style.display = "none";
    };
    seasonList.appendChild(li);
}


seasonButton.onclick = function () {
    dropdownMenu.style.display = dropdownMenu.style.display === "none" ? "block" : "none";
};

dropdownMenu.style.display = "none";
