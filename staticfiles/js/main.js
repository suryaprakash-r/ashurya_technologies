const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
      }
    });
  },
  {
    threshold: 0.1,
  },
);



// run safely
document.addEventListener("DOMContentLoaded", initScrollTopButton);
console.log("Checking page:", window.location.pathname);

document.querySelectorAll(".reveal").forEach((el) => {
  observer.observe(el);
});

//Form submission with AJAX
const form = document.getElementById("contactForm");

if (form) {

    const submitBtn =
        document.getElementById("submitBtn");

    const btnText =
        document.getElementById("btnText");

    const btnSpinner =
        document.getElementById("btnSpinner");

    form.addEventListener(
        "submit",
        function (e) {

            e.preventDefault();

            submitBtn.disabled = true;

            btnText.innerText =
                "Sending Message...";

            btnSpinner.classList.remove(
                "d-none"
            );

            const formData =
                new FormData(this);

            fetch("", {

                method: "POST",

                body: formData,

                headers: {
                    "X-Requested-With":
                        "XMLHttpRequest",

                    "X-CSRFToken":
                        document.querySelector(
                            "[name=csrfmiddlewaretoken]"
                        ).value
                }

            })

            .then((response) => {

                if (!response.ok) {

                    throw new Error(
                        "Request Failed"
                    );
                }

                return response.json();

            })

            .then((data) => {

                if (
                    data.status ===
                    "success"
                ) {

                    new bootstrap.Toast(
                        document.getElementById(
                            "successToast"
                        )
                    ).show();

                    form.reset();

                }

            })

            .catch((error) => {

                console.error(error);

                new bootstrap.Toast(
                    document.getElementById(
                        "errorToast"
                    )
                ).show();

            })

            .finally(() => {

                submitBtn.disabled =
                    false;

                btnText.innerText =
                    "Send Message";

                btnSpinner.classList.add(
                    "d-none"
                );

            });

        }
    );

}

const commentForm = document.getElementById("commentForm");

if (commentForm) {
  commentForm.addEventListener("submit", function (e) {
    e.preventDefault();

    console.log("AJAX triggered");

    let formData = new FormData(this);

    fetch(window.location.href, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === "success") {

          let newComment = `
            <div class="comment-box mb-3 p-3 border rounded">
              <h6>${data.name}</h6>
              <small class="text-muted">${data.created_at}</small>
              <p class="mt-2">${data.message}</p>
            </div>
          `;

          document.getElementById("commentList")
            .insertAdjacentHTML("afterbegin", newComment);

          commentForm.reset();

          let empty = document.getElementById("noComments");
          if (empty) empty.remove();
        }
      })
      .catch(err => console.error(err));
  });
}



function initScrollTopButton() {
  const scrollBtn = document.getElementById("scrollTopBtn");

  if (!scrollBtn) return;

  console.log("Scroll button initialized ✔");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 200) {
      scrollBtn.classList.add("show");
    } else {
      scrollBtn.classList.remove("show");
    }
  });

  scrollBtn.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}


// const themeToggle = document.getElementById("themeToggle");

// if (themeToggle) {
//     const currentTheme = localStorage.getItem("theme");

//     if (currentTheme === "dark") {
//         document.body.classList.add("dark-mode");
//     }

//     themeToggle.addEventListener("click", () => {
//         document.body.classList.toggle("dark-mode");

//         if (document.body.classList.contains("dark-mode")) {
//             localStorage.setItem("theme", "dark");
//         } else {
//             localStorage.setItem("theme", "light");
//         }
//     });
// }

// const icon = themeToggle.querySelector("i");

// if (document.body.classList.contains("dark-mode")) {
//     icon.classList.remove("bi-moon-stars-fill");
//     icon.classList.add("bi-sun-fill");
// }

// themeToggle.addEventListener("click", () => {
//     icon.classList.toggle("bi-moon-stars-fill");
//     icon.classList.toggle("bi-sun-fill");
// });

const themeBtn = document.getElementById("themeToggle");

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
  document.body.classList.add("dark-mode");
  themeBtn.innerHTML = '<i class="bi bi-sun-fill"></i>';
}

themeBtn.addEventListener("click", () => {

  document.body.classList.toggle("dark-mode");

  const isDark =
    document.body.classList.contains("dark-mode");

  localStorage.setItem(
    "theme",
    isDark ? "dark" : "light"
  );

  themeBtn.innerHTML = isDark
    ? '<i class="bi bi-sun-fill"></i>'
    : '<i class="bi bi-moon-stars-fill"></i>';
});