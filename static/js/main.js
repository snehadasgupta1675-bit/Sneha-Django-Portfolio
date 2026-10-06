document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "✕" : "☰";
    });
    nav.querySelectorAll("a").forEach(link => link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.textContent = "☰";
    }));
  }

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const words = ["web experiences", "useful applications", "creative interfaces", "new possibilities"];
  const target = document.getElementById("typed-word");
  if (target && window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
    let wordIndex = 0;
    setInterval(() => {
      wordIndex = (wordIndex + 1) % words.length;
      target.classList.add("word-out");
      setTimeout(() => {
        target.textContent = words[wordIndex];
        target.classList.remove("word-out");
      }, 180);
    }, 2400);
  }

  const revealItems = document.querySelectorAll(".reveal, .project-card, .timeline-card, .experience-card, .skill-group");
  if ("IntersectionObserver" in window && window.matchMedia("(prefers-reduced-motion: no-preference)").matches) {
    revealItems.forEach(item => item.classList.add("will-reveal"));
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    revealItems.forEach(item => observer.observe(item));
  }
});