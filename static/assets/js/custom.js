// afficher ou cacher le mdp
document.querySelectorAll('i[id^="toggle"]').forEach(toggleIcon => {
  toggleIcon.addEventListener('click', function() {
    // Sélection du champ de mot de passe associé
    const passwordInput = this.previousElementSibling;
    
    // Bascule du type de champ entre 'password' et 'text'
    const passwordType = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', passwordType);
    
    // Bascule de l'icône entre 'fa-eye' et 'fa-eye-slash'
    this.classList.toggle('fa-eye');
    this.classList.toggle('fa-eye-slash');
  });
});  

$(document).ready(function () {
  // Vérifie si les cookies ont déjà été acceptés
  if (!document.cookie.includes('cookies_accepted=true')) {
    // Affiche la modal si les cookies n'ont pas été acceptés
    $('#cookieModal').modal('show')
  }

  // Au clic du bouton "Accepter"
  $('#acceptCookies').click(function () {
    // Définit un cookie indiquant que l'utilisateur a accepté les cookies
    document.cookie = 'cookies_accepted=true; path=/; max-age=' + 60 * 60 * 24 * 30 // Expiration de 30 jours
    // Masque la modal
    $('#cookieModal').modal('hide')
  })
})
const player = fluidPlayer('my-video', {
  layoutControls: {
    controlBar: {
      autoHideTimeout: 3,
      animated: true,
      autoHide: true
    },
    htmlOnPauseBlock: {
      html: null,
      height: null,
      width: null
    },
    autoPlay: false,
    mute: false,
    allowTheatre: true,
    playPauseAnimation: false,
    playbackRateEnabled: false,
    allowDownload: false,
    playButtonShowing: true,
    fillToContainer: true,
    posterImage: ''
  },
  vastOptions: {
    adList: [],
    adCTAText: false,
    adCTATextPosition: ''
  }
});
let firstPlay = true;
let currentTime = 0; // Variable to store the current time
const videoElement = document.getElementById("my-video");
  

  // Listen for time updates
  videoElement.addEventListener('timeupdate', function() {
      currentTime = videoElement.currentTime.toFixed(0);  // Log the current time
  });

  // Listen for the play event
  player.on("play", function () {
  if (firstPlay) {
    const savedTime = getCookie("videoTime");

    if (savedTime && savedTime > 0) {
      // Show the modal if saved time is available
      $("#resumeModal").modal("show");

      // When user clicks to resume video
      document
        .getElementById("resumeVideo")
        .addEventListener("click", function () {
          player.skipTo(savedTime);
          $("#resumeModal").modal("hide");
        });

      // When user clicks to start from the beginning
      document
        .getElementById("startFresh")
        .addEventListener("click", function () {
          player.skipTo(0);
          console.log("Video started from the beginning");
          $("#resumeModal").modal("hide");
        });
    }

    // On click of "Accept" button
    $('#acceptCookies').click(function() {
        // Set a cookie indicating the user accepted the cookies
        document.cookie = "cookies_accepted=true; path=/; max-age=" + (60 * 60 * 24 * 30); // 30 days expiration

        // Hide the modal
        $('#cookieModal').modal('hide');
    });
  }
  firstPlay = false;
});
// Save the current time in cookies when the video is paused
player.on("pause", function () {
  setCookie("videoTime", currentTime, 1); // Use the stored current time
  console.log("Cookie set to: " + currentTime); // Log for debugging
});

// Save time on page unload as well
window.addEventListener("beforeunload", function () {
  setCookie("videoTime", currentTime, 1);
});

// Cookie helper functions
function setCookie(name, value, days) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie =
    name +
    "=" +
    encodeURIComponent(value) +
    "; expires=" +
    expires +
    "; path=/";
}

function getCookie(name) {
  return document.cookie.split("; ").reduce((r, v) => {
    const parts = v.split("=");
    return parts[0] === name ? decodeURIComponent(parts[1]) : r;
  }, "");
}
