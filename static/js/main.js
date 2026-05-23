document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });

    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    const currentPath = window.location.pathname;
    navLinks.forEach(function (link) {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
            link.style.color = "#fff";
        }
    });
});
