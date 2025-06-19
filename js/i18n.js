document.addEventListener("DOMContentLoaded", function () {
    const langSelector = document.getElementById("lang-select");
  
    // Idioma por defecto
    let currentLang = localStorage.getItem("lang") || "es";
  
    function loadLangFile(lang) {
      fetch(`./lang/${lang}.json`)
        .then((res) => res.json())
        .then((translations) => {
          document.querySelectorAll("[data-i18n]").forEach((element) => {
            const key = element.getAttribute("data-i18n");
            if (translations[key]) {
              element.innerText = translations[key];
            }
          });
          localStorage.setItem("lang", lang);
        });
    }
  
    // Cargar idioma inicial
    loadLangFile(currentLang);
  
    // Listener para cambiar idioma
    langSelector.addEventListener("change", (e) => {
      loadLangFile(e.target.value);
    });
  });
  