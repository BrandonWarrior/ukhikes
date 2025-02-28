document.addEventListener("DOMContentLoaded", function () {
    function updateUpvote(button, url, upvoteClass) {
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
            if (data.upvoted) {
                button.classList.add("btn-success");
                button.classList.remove("btn-outline-primary");
            } else {
                button.classList.remove("btn-success");
                button.classList.add("btn-outline-primary");
            }
            button.querySelector(upvoteClass).innerText = data.total_upvotes;
        })
        .catch(error => console.error("Error:", error));
    }

    function getCSRFToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
    }

    // Upvote Post
    document.querySelectorAll(".upvote-post").forEach(button => {
        button.addEventListener("click", function () {
            let postId = this.getAttribute("data-post-id");
            let url = `/post/${postId}/upvote/`;
            console.log("Upvoting post:", url);
            updateUpvote(this, url, ".upvote-text");
        });
    });

    // Upvote Comment
    document.querySelectorAll(".upvote-comment").forEach(button => {
        button.addEventListener("click", function () {
            let commentId = this.getAttribute("data-comment-id");
            let url = `/comment/${commentId}/upvote/`;
            console.log("Upvoting comment:", url);
            updateUpvote(this, url, ".comment-upvote-text");
        });
    });
});
