function setDetailsHeight(selector, wrapper = document) {
    const setHeight = (detail, open = false) => {
      detail.open = open;
      const rect = detail.getBoundingClientRect();
      detail.dataset.width = rect.width;
      detail.style.setProperty(
        open ? `--expanded` : `--collapsed`,
        `${rect.height}px`
      );
    };
    const details = wrapper.querySelectorAll(selector);
    const RO = new ResizeObserver((entries) => {
      return entries.forEach((entry) => {
        const detail = entry.target;
        const width = parseInt(detail.dataset.width, 10);
        if (width !== entry.contentRect.width) {
          detail.removeAttribute("style");
          setHeight(detail);
          setHeight(detail, true);
          detail.open = false;
        }
      });
    });
    details.forEach((detail) => {
      RO.observe(detail);
    });
  }
  
  /* Run it */
  setDetailsHeight("details");

const targetDiv2 = document.getElementById("filter");
const btn2 = document.getElementById("hideshow");
btn2.onclick = function () {
  if (targetDiv2.style.display !== "none") {
    targetDiv2.style.display = "none";
  } else {
    targetDiv2.style.display = "block";
  }
};