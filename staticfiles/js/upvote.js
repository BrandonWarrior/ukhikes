document.addEventListener("DOMContentLoaded", function () {
    function updateLike(button, url, likeClass) {
        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "X-Requested-With": "XMLHttpRequest"
            },
            credentials: "include"
        })
        .then(response => response.json())
        .then(data => {
            if (data.liked) {
                button.classList.add("btn-success");
                button.classList.remove("btn-outline-primary");
            } else {
                button.classList.remove("btn-success");
                button.classList.add("btn-outline-primary");
            }
            button.querySelector(likeClass).innerText = data.total_likes;
        })
        .catch(error => console.error("Error:", error));
    }

    document.querySelectorAll(".like-post").forEach(button => {
        button.addEventListener("click", function () {
            let postId = this.getAttribute("data-post-id");
            updateLike(this, `/post/${postId}/like/`, ".like-text");
        });
    });

    document.querySelectorAll(".like-comment").forEach(button => {
        button.addEventListener("click", function () {
            let commentId = this.getAttribute("data-comment-id");
            updateLike(this, `/comment/${commentId}/like/`, ".comment-like-text");
        });
    });
});
