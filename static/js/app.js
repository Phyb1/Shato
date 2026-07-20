/**
 * Shato Sports Bar — front-end behaviour
 *
 * Two small, dependency-free features:
 *   1. Dark/light theme toggle, persisted in localStorage.
 *   2. Mobile hamburger menu (shown under the 768px breakpoint;
 *      see static/css/style.css).
 *
 * This script is loaded WITHOUT `defer` in base.html so the saved
 * theme is applied before first paint, avoiding a flash of the
 * wrong theme. Because of that, DOM elements below <script> in the
 * document may not exist yet — theme application happens
 * immediately, while menu/toggle wiring waits for DOMContentLoaded.
 */

(function applyStoredTheme() {
    var savedTheme = localStorage.getItem("shato-theme") || "dark";
    document.documentElement.setAttribute("data-theme", savedTheme);
})();

document.addEventListener("DOMContentLoaded", function () {
    var themeToggle = document.getElementById("theme-toggle");
    var hamburger = document.getElementById("hamburger");
    var navLinks = document.getElementById("nav-links");
    var html = document.documentElement;

    function updateToggleIcon() {
        var isDark = html.getAttribute("data-theme") === "dark";
        themeToggle.textContent = isDark ? "🌙" : "☀️";
        themeToggle.setAttribute(
            "aria-label",
            isDark ? "Switch to light theme" : "Switch to dark theme"
        );
    }

    if (themeToggle) {
        updateToggleIcon();
        themeToggle.addEventListener("click", function () {
            var newTheme = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
            html.setAttribute("data-theme", newTheme);
            localStorage.setItem("shato-theme", newTheme);
            updateToggleIcon();
        });
    }

    if (hamburger && navLinks) {
        hamburger.addEventListener("click", function () {
            var isOpen = navLinks.classList.toggle("is-open");
            hamburger.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        // Close the mobile menu after a link is tapped.
        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                navLinks.classList.remove("is-open");
                hamburger.setAttribute("aria-expanded", "false");
            });
        });
    }
});
