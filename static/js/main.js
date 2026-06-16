
const observer = new IntersectionObserver((entries) => {

    entries.forEach((entry) => {

        if (entry.isIntersecting) {

            entry.target.classList.add("active");

        }

    });

},{
    threshold: 0.1
});

document.querySelectorAll(".reveal").forEach((el) => {
    observer.observe(el);
});


//Form submission with AJAX
const form = document.getElementById("contactForm");
const submitBtn = document.getElementById("submitBtn");
const btnText = document.getElementById("btnText");
const btnSpinner = document.getElementById("btnSpinner");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    // START LOADING
    submitBtn.disabled = true;
    btnText.innerText = "Sending...";
    btnSpinner.classList.remove("d-none");

    let formData = new FormData(this);

    fetch("", {
        method: "POST",
        body: formData,
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })

    .then(res => res.json())
    .then(data => {

        if (data.status === "success") {

            let toast = new bootstrap.Toast(
                document.getElementById("successToast")
            );

            toast.show();

            form.reset();

        } else {
            alert("Something went wrong!");
        }

    })

    .catch(error => {
        console.error(error);
        alert("Server error. Try again.");
    })

    .finally(() => {

        // RESET BUTTON
        submitBtn.disabled = false;
        btnText.innerText = "Send Message";
        btnSpinner.classList.add("d-none");

    });

});