let container1 = document.querySelector(
  "div.top-10-songs .song-data__wrapper p"
);
let text1 = document.querySelector("#one span");

if (container1.clientWidth < text1.clientWidth) {
  text1.classList.add("animate");
}
