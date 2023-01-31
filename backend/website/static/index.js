function like(profileId) {
  const likeCount = document.getElementById(`likes-count-${profileId}`);
  const likeButton = document.getElementById(`like-button-${profileId}`);

  fetch(`/like-profile/${profileId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.className = "fas fa-thumbs-up";
      } else {
        likeButton.className = "far fa-thumbs-up";
      }
    })
    .catch((e) => alert("Could not like profile."));
}
