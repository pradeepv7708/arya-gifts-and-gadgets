const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");
const searchToggle = document.getElementById("searchToggle");
const searchBar = document.getElementById("searchBar");
const closeSearch = document.getElementById("closeSearch");
const productSearch = document.getElementById("productSearch");

menuToggle?.addEventListener("click", () => mainNav.classList.toggle("nav-open"));
searchToggle?.addEventListener("click", () => {
  searchBar.classList.toggle("search-open");
  if (searchBar.classList.contains("search-open")) productSearch.focus();
});
closeSearch?.addEventListener("click", () => searchBar.classList.remove("search-open"));

productSearch?.addEventListener("input", () => {
  const term = productSearch.value.toLowerCase().trim();
  document.querySelectorAll(".product-card").forEach(card => {
    card.hidden = !card.dataset.name.includes(term);
  });
  document.getElementById("products")?.scrollIntoView({ behavior: "smooth", block: "nearest" });
});

document.querySelectorAll(".heart-button").forEach(button => {
  button.addEventListener("click", () => {
    const active = button.classList.toggle("is-favourite");
    button.textContent = active ? "♥" : "♡";
  });
});

setTimeout(() => {
  document.querySelectorAll(".flash").forEach(el => {
    el.style.opacity = "0";
    setTimeout(() => el.remove(), 350);
  });
}, 3500);
