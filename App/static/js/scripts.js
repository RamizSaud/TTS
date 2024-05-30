const btn = document.getElementById("btn");
const indication = document.getElementById("indication");

function sendTextToSpeech() {
  const text = document.getElementById("urdu-text").value;
  indication.style.display = "block";

  fetch("/text-to-speech", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  })
    .then((response) => response.blob())
    .then((blob) => {
      const audio = document.getElementById("audio");
      const url = URL.createObjectURL(blob);
      audio.src = url;
      indication.style.display = "none";
      audio.style.display = "block";
      audio.hidden = false;
      audio.play();
    })
    .catch((error) => console.error("Error:", error));
}

btn.addEventListener("click", sendTextToSpeech);
