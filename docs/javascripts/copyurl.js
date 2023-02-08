const wrapper = document.getElementById("gallery-container");

wrapper.addEventListener("click", (event) => {
  const isButton = event.target.nodeName === "BUTTON";
  if (!isButton) {
    return;
  }

  var datalink = event.target.getAttribute("data-link");
  navigator.clipboard.writeText(datalink);

  var copybuttons = document.getElementsByClassName("copy-button");
  for (var i = 0; i < copybuttons.length; ++i) {
    var item = copybuttons[i];
    item.innerHTML = "Copy image URL";
  }

  event.target.innerHTML = "Copied to clipboard!";
});
